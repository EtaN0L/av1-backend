from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import friendslist

# Create your views here.

@login_required
def add_friend(request, friend_id):
    friend = User.objects.get(id=friend_id)
    friendslist.objects.create(user1=request.user, user2=friend)
    return redirect('profile', user_id=friend.id)

@login_required
def remove_friend(request, friend_id):
    friend = User.objects.get(id=friend_id)
    friendslist.objects.filter(user1=request.user, user2=friend)
    return redirect('profile', user_id=friend.id)

@login_required
def get_friend_amount(request, user_id):
    user = User.objects.get(id=user_id)
    friend_count = friendslist.objects.filter(user1=user).count()
    return JsonResponse({'friend_count': friend_count})