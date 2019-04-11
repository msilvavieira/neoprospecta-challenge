from rest_framework import serializers
from api.models import Entry, Kingdom, Species


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'access_id', 'kingdom', 'species', 'sequence',)

class KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kingdom
        fields = ('id', 'label',)

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('id', 'label',)

