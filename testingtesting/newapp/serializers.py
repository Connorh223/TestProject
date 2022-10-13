from .models import Person, Address
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['firstname', 'lastname', 'age', 'gender']

class RandomPersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['firstname', 'lastname', 'age', 'gender']

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['firstname', 'lastname', 'address']

