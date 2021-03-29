from rest_framework import viewsets, permissions

from db.auction.models import Animal


class AnimalViewset(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    class Meta:
        model = Animal
        fields = '__all__'
