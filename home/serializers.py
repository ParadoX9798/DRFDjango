from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'email')
        extra_kwargs = {
            'email': {'write_only': True}
        }

    def validate_name(self, value):
        if value == "younes":
            raise serializers.ValidationError("name can not be younes")
        return value

