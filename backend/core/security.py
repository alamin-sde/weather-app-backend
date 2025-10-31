from passlib.context import CryptContext
pass_context =CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password:str)->str:
    return pass_context.hash(password)
    
def verify_password(normal_password:str,hashed_password)-> bool:
    return pass_context.verify(normal_password,hashed_password)