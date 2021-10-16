from rest_framework.views import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def one(request):
    if request.method == "POST":
        name = request.data['name']
        return Response({'name': f"hello {name}"})

    else:
        return Response(data={'name': 'amir', 'family': 'reza'})
