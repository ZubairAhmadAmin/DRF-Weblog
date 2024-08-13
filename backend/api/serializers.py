from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Articale


class ArticaleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Articale
        # fields = ('title', 'slug', 'author', 'content', 'publish', 'status')
        fields = '__all__'
        # exclude = ('updated', 'created')
        
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'