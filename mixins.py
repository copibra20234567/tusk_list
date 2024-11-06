from django.core.exception import PermissionDenied


class UserIsOwnerMixin(object):
    def dispatch(self, requests, *args, **kwargs):