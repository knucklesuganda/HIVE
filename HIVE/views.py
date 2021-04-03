import logging

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, CreateAPIView

from requests.api.serializers import HTTPRequestSerializer
from requests.models import HTTPRequest


logger = logging.getLogger(settings.DJANGO_LOGGER_NAME)


def base_error_handler(exception_str: str, status_code: int):
    logger.info(f"Error occurred: '{exception_str}'. Status code: {status_code}")
    return JsonResponse({"error": exception_str, "status_code": status_code})


def error_handler404(request, exception=None):
    return base_error_handler(exception_str="Not found", status_code=404)


def error_handler500(request, exception=None):
    return base_error_handler(exception_str="Error in the HIVE", status_code=500)


def error_handler403(request, exception=None):
    return base_error_handler(exception_str="Forbidden", status_code=403)


def error_handler400(request, exception=None):
    return base_error_handler(exception_str="Bad request", status_code=400)

