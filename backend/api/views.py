from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Articale
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .serializers import ArticaleSerializer, UserSerializer



class ArticaleList(ListCreateAPIView):
    queryset = Articale.objects.all()
    serializer_class = ArticaleSerializer
    

class ArticaleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Articale.objects.all()
    serializer_class = ArticaleSerializer
    lookup_field = 'slug'
    
    
    
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)