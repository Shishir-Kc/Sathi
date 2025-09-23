from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Sathi_User
import requests

@api_view(['Get'])
def users(request):
    for i in Sathi_User.objects.all():
        print(i.first_name)
    data = Sathi_User.objects.filter(username = 'mrkc')
    print(data)

    return Response(
        {
            'message':'Hello ! '
        }
    )

@api_view(['Get'])
def get_content(request):
    url = ('http://127.0.0.1:9000/hello')
    response = requests.request("GET",url)
    data = response.json()['message']
    return Response({
        'data':data,
    })






