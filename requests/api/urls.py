from rest_framework import routers

from requests.api.views import RequestViewSet

router = routers.SimpleRouter()
router.register('http_request', RequestViewSet, basename='http_request')

urlpatterns = router.urls
