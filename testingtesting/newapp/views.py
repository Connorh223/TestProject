from .models import Person, Address
from rest_framework import viewsets, permissions
from testingtesting.newapp.serializers import PersonSerializer, RandomPersonSerializer, AddressSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that shows a list of people
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]

class RandomPersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows people to be viewed or edited randomly.
    """
    serializer_class = RandomPersonSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Person.objects.all()
        gender = self.request.query_params.get('gender')
        if gender is not None:
            queryset = queryset.filter(gender=gender.lower())
        return queryset.filter(pk__in=[queryset.order_by('?').first().pk])


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that displays addresses of People.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.AllowAny]

