from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.validators import ValidationError

from users.models import FriendRequest, User
from users.serializers import FriendRequestSerializer, UserSearchSerializer
from django.db.models import Q


class SendFriendRequestView(generics.CreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]


class AcceptFriendRequestView(generics.UpdateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.to_user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if instance.is_accepted:
            raise ValidationError({"error": "Request Already Accepted"})
        instance.is_accepted = True
        instance.save()
        return Response(self.get_serializer(instance).data)


class RejectFriendRequestView(generics.DestroyAPIView):
    queryset = FriendRequest.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.to_user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListFriendsView(generics.ListAPIView):
    serializer_class = UserSearchSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(
            Q(sent_requests__to_user=self.request.user, sent_requests__is_accepted=True) |
            Q(received_requests__from_user=self.request.user, received_requests__is_accepted=True)
        ).distinct()


class ListPendingRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, is_accepted=False)
