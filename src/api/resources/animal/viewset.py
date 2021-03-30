from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from api.resources.animal.serializer import AnimalSerializer
from api.wrapped_errors import wrap_exceptions
from db.animals.models import Animal
from operations.animal.create import create_animal
from operations.animal.delete import delete_animal
from operations.animal.get_by_id import get_by_id


class AnimalViewSet(viewsets.GenericViewSet):
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Animal.objects.none()

    @wrap_exceptions
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.data)
        if serializer.is_valid(raise_exception=True):
            instance = create_animal(
                owner_id=request.user.id,
                animal_type=serializer.validated_data['animal_type'],
                breed=serializer.validated_data['breed'],
                nickname=serializer.validated_data['nickname'],
            )
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

    @wrap_exceptions
    def destroy(self, request, pk=None, *args, **kwargs):
        delete_animal(
            owner_id=request.user.id,
            animal_id=pk,
        )
        return Response(status=status.HTTP_204_NO_CONTENT)

    @wrap_exceptions
    def retrieve(self, request, pk=None, *args, **kwargs):
        instance = get_by_id(pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
