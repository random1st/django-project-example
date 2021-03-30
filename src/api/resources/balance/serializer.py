from rest_framework import serializers


class UserBalanceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)
