from urllib import response
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers, status, generics, views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.contrib.auth.models import User
from base.api.models import Post
from .serializers import (
    MyTokenObtainPairSerializer,
    PostSerializer,
    UserSerializer
)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def getUserDetail(request, pk):
    post = User.objects.get(id=pk)
    serializer = UserSerializer(post, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def createUser(request):
    serializer = UserSerializer(data=request.data)

    if User.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This user already exists')

    if not serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, pk):
    authenticatedUser = request.user

    if not authenticatedUser.id == pk:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUser(request, pk):
    authenticatedUser = request.user

    if not authenticatedUser.id == pk:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    user = User.objects.get(id=pk)
    user.delete()

    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def getPostDetail(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPost(request):
    authenticatedUser = request.user
    post = {
        'author': authenticatedUser.id,
        'body': request.data.get('body')
    }
    serializer = PostSerializer(data=post)

    if not serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updatePost(request, pk):
    authenticatedUser = request.user
    post = Post.objects.get(id=pk)

    if not authenticatedUser.id == post.author.id:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    serializer = PostSerializer(instance=post, data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletePost(request, pk):
    authenticatedUser = request.user
    post = Post.objects.get(id=pk)

    if not authenticatedUser.id == post.author.id:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    post.delete()

    return Response(status=status.HTTP_200_OK)
