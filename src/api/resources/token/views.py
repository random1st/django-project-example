from rest_framework_jwt.views import ObtainJSONWebToken

from .serializer import JSONWebTokenSerializerCustom, \
    VerifyJSONWebTokenSerializerCustom, RefreshJSONWebTokenSerializerCustom


class ObtainJSONWebTokenCustom(ObtainJSONWebToken):
    serializer_class = JSONWebTokenSerializerCustom


class VerifyJSONWebTokenCustom(ObtainJSONWebToken):
    serializer_class = VerifyJSONWebTokenSerializerCustom


class RefreshJSONWebTokenCustom(ObtainJSONWebToken):
    serializer_class = RefreshJSONWebTokenSerializerCustom
