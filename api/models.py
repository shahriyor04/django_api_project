from django.contrib.auth.models import User
from django.db.models import Model, CharField, IntegerField, DateTimeField, ImageField, ForeignKey, BooleanField, \
    CASCADE


class Category(Model):
    title = CharField(max_length=200)

    def __str__(self):
        return self.title


class Post(Model):
    image = ImageField('pics/', blank=True, null=True)
    name = CharField(max_length=200)
    kilo = IntegerField()
    price = IntegerField()
    data = DateTimeField(auto_now_add=True)
    to_category = ForeignKey(Category, CASCADE)
    to_author = ForeignKey(User, CASCADE)
    active = BooleanField(default=False)

    def __str__(self):
        return self.name
