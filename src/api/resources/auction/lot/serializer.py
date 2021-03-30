from rest_framework import serializers

from db.animals.models import Animal


class LotSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    animal = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.none())
    price = serializers.DecimalField(max_digits=12, decimal_places=2)


class LotForSaleSerializer(serializers.Serializer):
    animal = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.none())
    price = serializers.DecimalField(max_digits=12, decimal_places=2)
