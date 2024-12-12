
from django.urls import path,include
from . import views

urlpatterns = [
    
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create")
]