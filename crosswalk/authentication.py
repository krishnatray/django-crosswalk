from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication, exceptions

from .models import ApiUser


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Of format "TOKEN <SOME TOKEN>"
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if not token:
            raise exceptions.AuthenticationFailed(
                'Missing authorization header'
            )
        try:
            user = ApiUser.objects.get(token=token.split(' ')[1]).user
        except ObjectDoesNotExist:
            raise exceptions.AuthenticationFailed('Unauthorized')
        return (user, None)
