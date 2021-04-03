from rest_framework.viewsets import ModelViewSet

from requests.api.serializers import HTTPRequestSerializer
from requests.models import HTTPRequest


class RequestViewSet(ModelViewSet):
    queryset = HTTPRequest.objects.all()
    serializer_class = HTTPRequestSerializer
