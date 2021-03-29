from rest_framework import serializers

from db.core.models import UserBalance


class UserBalanceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserBalance
        fields = '__all__'
