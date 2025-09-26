from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import httpx
import asyncio
import base64
from Validation.models import Images
import uuid

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Chat(request):
        
        prompt = request.data.get('prompt')
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        payload = {"prompt": prompt}
        # print(auth_header)
        header = {"Authorization":auth_header}
        async def response():
           async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post('http://127.0.0.1:9000/chat/', json=payload,headers=header)
            return response.json()
        data = asyncio.run(response())
        
        return Response({'response': data.get('response')}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Upload(request):
    auth_headers = request.META.get('HTTP_AUTHORIZATION')
    user = request.user
    print(user)
    image = request.FILES['file']
    print("================================ FILE RECIVED ! ==============================")
    print(image.name)

    print(image.content_type)

    print('payload Sent ! ')
    b64_content = base64.b64encode(image.read()).decode('utf-8')
    async def upload_image():
     async with httpx.AsyncClient() as client:
            PAYLOAD = {
                'filename':str(uuid.uuid4()),
                'file_content':b64_content,
                'file_type':image.content_type
            }
            headers = {"Authorization":auth_headers}
            response = await client.post('http://127.0.0.1:9000/upload/',json=PAYLOAD,headers=headers)
            return response
    response = asyncio.run(upload_image())

    data = response.json()
    url = data['url']
    image_DB = Images.objects.create(user=user,image_url=url,image_name = image.name)
    image_DB.save()


    

    return Response({
        'message':'uploaded',
        'url':url
    })
