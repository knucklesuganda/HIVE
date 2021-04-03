from django.contrib.auth.models import User
from rest_framework import serializers
from requests.models import HTTPRequest
from users.api.serializers import UserSerializer


class HTTPRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HTTPRequest
        fields = [
            'id',
            'content_type',
            'encoding',
            'connection',
            'cache_control',
            'user_agent',
            'accept_language',
            'http_method',
            'url',
            'scheme',
            'user',
            'is_ajax',
            'load_time',
        ]

    def to_representation(self, instance):
        data = super(HTTPRequestSerializer, self).to_representation(instance)
        data['user'] = UserSerializer(instance=User.objects.get(id=data['user'])).data
        return data
