from rest_framework import serializers
from .models import User, FriendRequest
from django.contrib.auth import authenticate
from django.utils import timezone
from datetime import timedelta


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")


class UserSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'name']  # Assuming you have these fields


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['id', 'from_user', 'to_user', 'is_accepted', 'created_at']
        read_only_fields = ['from_user', 'is_accepted', 'created_at']

    def create(self, validated_data):
        to_user = validated_data['to_user']
        from_user = self.context['request'].user
        validated_data["from_user"] = from_user
        if from_user == to_user:
            raise serializers.ValidationError("Can't send friend request to yourself")
        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
            raise serializers.ValidationError("Friend request already sent.")
        one_minute_ago = timezone.now() - timedelta(minutes=1)
        request_count = FriendRequest.objects.filter(from_user=from_user, created_at__gte=one_minute_ago).count()
        if request_count >= 3:
            raise serializers.ValidationError("You can't send more than 3 friend requests within a minute.")
        return super(FriendRequestSerializer, self).create(validated_data)



