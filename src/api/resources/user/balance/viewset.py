from rest_framework import viewsets, permissions
from rest_framework.response import Response

from api.resources.user.balance import UserBalanceSerializer
from api.wrapped_errors import wrap_exceptions
from db.core.models import UserBalance
from operations.user.balance.get_balance import get_balance


class UserBalanceViewset(viewsets.GenericViewSet):
    serializer_class = UserBalanceSerializer
    queryset = UserBalance.objects.none()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @wrap_exceptions
    def list(self, request, *args, **kwargs):
        instance = get_balance(request.user.id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
