from rest_framework import serializers


class BidSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    bidder = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    price = serializers.DecimalField(max_digits=12, decimal_places=2)
    lot = serializers.PrimaryKeyRelatedField(read_only=True)
    accepted = serializers.NullBooleanField()


class UpdatePriceBidSerializer(serializers.Serializer):
    price = serializers.DecimalField(max_digits=12, decimal_places=2)


class AcceptBidSerializer(serializers.Serializer):
    pass


class LotBidSerializer(serializers.Serializer):
    price = serializers.DecimalField(max_digits=12, decimal_places=2)
    lot = serializers.PrimaryKeyRelatedField(read_only=True)
