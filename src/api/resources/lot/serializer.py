from rest_framework import serializers

from db.auction.models import Lot


class LotSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lot
        fields = '__all__'
