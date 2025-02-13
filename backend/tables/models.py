from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class friendslist(models.Model):
    user1 = models.ForeignKey(User, related_name='friendship_creator_set', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='friend_set', on_delete=models.CASCADE)
    dateAdded = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f"{self.user1} is friends with {self.user2}"