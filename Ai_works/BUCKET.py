from supabase import create_client
from decouple import config


URL = config("SUPABASE_URL")
KEY = config("SUPABASE_API_KEY")

supabase = create_client(URL,KEY)




async def upload_to_bucket(bucket_name:str,file_name:str,file_bytes,file_type):
    
    response = supabase.storage.from_(bucket_name).upload(file_name,file_bytes,{
        'content-type':file_type
    })
    url = recive_image(bucket_name=bucket_name,image_name=file_name)

    return {
        'message':'file uploaded Sucessfully',
        'url':url
    }

def recive_image(bucket_name:str,image_name:str):
    response = supabase.storage.from_(bucket_name,).get_public_url(image_name)
    return response


if __name__ == "__main__":
    print("Use Wisely ! ")