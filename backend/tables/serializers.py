from rest_framework import serializers
from .models import friendslist

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = friendslist
        fields = ['user2']