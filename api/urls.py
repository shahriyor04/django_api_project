from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostListAPIView, CategoryListAPIView


router = DefaultRouter()
router.register('posts', PostListAPIView, basename='posts')
router.register('category', CategoryListAPIView, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
