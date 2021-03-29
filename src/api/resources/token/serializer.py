from rest_framework_jwt.serializers import JSONWebTokenSerializer, \
    VerifyJSONWebTokenSerializer, RefreshJSONWebTokenSerializer


class JSONWebTokenSerializerCustom(JSONWebTokenSerializer):
    pass


class VerifyJSONWebTokenSerializerCustom(VerifyJSONWebTokenSerializer):
    pass


class RefreshJSONWebTokenSerializerCustom(RefreshJSONWebTokenSerializer):
    pass
