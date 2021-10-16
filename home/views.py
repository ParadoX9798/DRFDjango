from rest_framework.views import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Person
from .serializers import PersonSerializer


@api_view(['GET', 'POST'])
def one(request):
    if request.method == "POST":
        name = request.data['name']
        return Response({'name': f"hello {name}"})

    else:
        return Response(data={'name': 'amir', 'family': 'reza'})


@api_view()
def persons(request):
    persons = Person.objects.all()
    ser_data = PersonSerializer(persons, many=True)
    return Response(ser_data.data)


@api_view()
def get_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    ser_data = PersonSerializer(person)
    return Response(ser_data.data)


@api_view(["POST"])
def create_person(request):
    info = PersonSerializer(data=request.data)
    if info.is_valid():
        person = Person(name=info.validated_data['name'], age=info.validated_data['age'],
                        email=info.validated_data['email'])
        person.save()
        return Response({'status': 'ok'})
    else:
        return Response(info.errors)


@api_view()
def delete_person(request, person_id):
    person = Person.objects.filter(id=person_id)
    if person.exists():
        person.delete()
        return Response({"status": "ok"})
    else:
        return Response({"status": "does not exist"})
