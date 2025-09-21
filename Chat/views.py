from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
import requests
from rest_framework import status


class Chat(APIView):


    async def post(self,request):
        prompt = request.data.get('prompt')
        payload = {
      "prompt": prompt    
        }

        response = requests.request('POST','http://127.0.0.1:9000/chat/',json=payload)
        data = response.json()
        return Response(
            {
                'Message':data.get('response')
            },
            status= status.HTTP_200_OK
        )


