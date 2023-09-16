from django.shortcuts import render
from rest_framework.views import status, APIView, Request, Response
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .permissions import IsUserOwner


class UserView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOwner]

    def get(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, user)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def patch(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, user)
        serializer = UserSerializer(user, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
