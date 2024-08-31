from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken
from users.models import User
from users.paginations import UserSearchPagination
from users.serializers import UserSerializer, LoginSerializer, UserSearchSerializer
from django.db.models import Q


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AccessToken.for_user(user)

        return Response({
            'access_token': str(token),
        })


class UserSearchView(generics.ListAPIView):
    serializer_class = UserSearchSerializer
    pagination_class = UserSearchPagination

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword', '')
        user = User.objects.filter(
            Q(email__iexact=keyword)
        )
        if user:
            return user
        else:
            return User.objects.filter(Q(name__icontains=keyword))
