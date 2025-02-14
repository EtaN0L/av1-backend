from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import friendslist
from .serializers import FriendSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
def add_friend(request, friend_id):
    friend = User.objects.get(id=friend_id)
    friendslist.objects.create(user1=request.user, user2=friend)
    return redirect('profile', user_id=friend.id)

@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
def remove_friend(request, friend_id):
    friend = User.objects.get(id=friend_id)
    friendslist.objects.filter(user1=request.user, user2=friend)
    return redirect('profile', user_id=friend.id)

@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
def get_friend_amount(request, user_id):
    user = User.objects.get(id=user_id)
    friend_count = friendslist.objects.filter(user1=user).count()
    return JsonResponse({'friend_count': friend_count})

@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, ))
def get_friends(request, user_id):
    user = User.objects.get(id=user_id)
    friends = friendslist.objects.filter(user1=user)
    serializer = FriendSerializer(friends, many=True)
    return JsonResponse(serializer.data, safe=False)