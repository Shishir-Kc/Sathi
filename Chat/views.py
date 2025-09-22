from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import httpx
import asyncio


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Chat(request):
        
        prompt = request.data.get('prompt')
        payload = {"prompt": prompt}
        async def response():
         async with httpx.AsyncClient() as client:
            response = await client.post('http://127.0.0.1:9000/chat/', json=payload)
            return response.json()
        data = asyncio.run(response())    
        

        return Response({'Message': data.get('response')}, status=status.HTTP_200_OK)

