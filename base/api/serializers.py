from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Post
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )

    posts = serializers.SerializerMethodField()

    def validate_password(self, value: str) -> str:
        return make_password(value)

    def get_posts(self, obj):
        total = Post.objects.filter(author_id=obj.id).count()
        return total

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'posts']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = Post
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token
