from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'username', 'last_name')
