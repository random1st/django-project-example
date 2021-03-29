from .views import ObtainJSONWebTokenCustom, VerifyJSONWebTokenCustom, RefreshJSONWebTokenCustom

obtain_jwt_token = ObtainJSONWebTokenCustom.as_view()
verify_jwt_token = VerifyJSONWebTokenCustom.as_view()
refresh_jwt_token = RefreshJSONWebTokenCustom.as_view()
