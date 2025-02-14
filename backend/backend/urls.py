from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from tables import views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

#ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('addFriend/<int:friend_id>/', views.add_friend, name='add_friend'),
    path('removeFriend/<int:friend_id>/', views.remove_friend, name='remove_friend'),
    path('getFriendAmount/<int:user_id>/', views.get_friend_amount, name='get_friend_amount'),
    path('getFriends/<int:user_id>/', views.get_friends, name='get_friends'),
]
