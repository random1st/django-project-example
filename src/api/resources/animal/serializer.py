from django.http import HttpResponseForbidden
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from db.auction.models import Animal, Lot


class AnimalSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def update(self, instance, validated_data):
        if self.user != instance.owner:
            raise ValidationError('Can\'t update other user\'s animals')

        if hasattr(instance, 'lots') and instance.lots.filter(status=Lot.Status.PUBLISHED).exists():
            raise ValidationError('Can\'t change animals for sale')

        super().update(instance, validated_data)

    class Meta:
        model = Animal
        fields = '__all__'
