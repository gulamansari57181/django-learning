from django.shortcuts import render
# Create your views here.

# We will create django-rest framework view

from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreate(generics.ListAPIView):
    queryset= BlogPost.objects.all()
    serializer_class=BlogPostSerializer
