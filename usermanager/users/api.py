from rest_framework import viewsets, permissions
from users.models import SystemUser
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = SystemUser.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]
    
    serializer_class = UserSerializer
