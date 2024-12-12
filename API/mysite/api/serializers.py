# Take the blogpost model data and convert it into JSON Compatabale data
from rest_framework import serializers

# importing BlogPost from models from API directory

from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields= ["id", "title","content","published_date"]
        
        

