from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    class Meta:
        model = Person
        fields = ('name', 'age', 'email')
