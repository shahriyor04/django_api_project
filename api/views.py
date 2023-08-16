from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from api.models import Category
from .permission import *


# Create your views here.


# class CategoryListCreateAPIViewSet(ModelViewSet):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()
#     permission_classes = (CategoryPermission,)
#     http_method_names = ('post', 'get')


class CategoryListAPIView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (CategoryPermission,)
    http_method_names = ('post', 'get')


class PostListAPIView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes =(PostPermission, )
    parser_classes = [MultiPartParser]


class PostChangeViewSet(ModelViewSet):
    queryset = Post.objects.filter(active=True)
    serializer_class = ChangeSerializer
    permission_classes = (ChangePermission, )
    http_method_names = ('patch', )
