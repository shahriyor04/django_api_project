from rest_framework.fields import HiddenField, CurrentUserDefault

from rest_framework.serializers import ModelSerializer

from api.models import Category, Post


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(ModelSerializer):
    to_author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Post
        fields = ("name", "image", "kilo", "price", "to_category", "to_author")


class ChangeSerializer(ModelSerializer):
    class Meta:
        modul = Post
        fields = ("active",)


