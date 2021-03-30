from rest_framework import serializers


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    breed = serializers.CharField()
    nickname = serializers.CharField()
    animal_type = serializers.IntegerField()
