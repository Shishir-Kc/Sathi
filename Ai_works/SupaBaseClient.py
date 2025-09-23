from decouple import config
from supabase import create_client 
from datetime import datetime
import uuid
from Password_Hash import Hash_password

url: str =config('SUPABASE_URL')
key: str = config('SUPABASE_API_KEY')

supabase =  create_client(url,key)
 

insertaded_data = supabase.table('Validation_sathi_user').insert(
    {
        'username':'',
        'first_name':'',
        'last_name':'',
        'email':'',
        'password':Hash_password(''),
        'is_superuser':True,
        'is_staff':True,
        'is_active':True,
        'date_joined':datetime.now().isoformat(),
        'id':str(uuid.uuid4()),
        'User_image':'null'

        }
).execute()


data = supabase.table('Validation_sathi_user').select('*').execute()
print(data)

# deleted_data = supabase.table('Validation_sathi_user')
