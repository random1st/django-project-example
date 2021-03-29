from rest_framework import viewsets, permissions

from db.core.models import UserBalance


class UserBalanceViewset(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin, viewsets.mixins.UpdateModelMixin):
    queryset = UserBalance.objects.none()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return UserBalance.objects.filter(user=user).all()

    class Meta:
        model = UserBalance
        fields = '__all__'
