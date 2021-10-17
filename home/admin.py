from django.contrib import admin
from .models import Person, Car


class CarInline(admin.TabularInline):
    model = Person


@admin.register(Car)
class PersonAdmin(admin.ModelAdmin):
    class Meta:
        model = Car
        fields = "__all__"

    inlines = (CarInline,)
