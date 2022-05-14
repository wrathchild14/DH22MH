from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

@api_view(['GET', 'POST', ])
def test(request):
    if request.method == 'GET':
        print("Test")

        d = {"test" : 5}

        response = json.dumps(d)
        return Response(response)