"""

    using Django_pbkdf2_sha256 to hash the password ! 


"""

from passlib.context import CryptContext

pwsd_context = CryptContext(schemes=["django_pbkdf2_sha256"],deprecated = "auto")

def Hash_password(password:str)->str:
    return pwsd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str)->str:
    return pwsd_context.verify(plain_password,hashed_password)
