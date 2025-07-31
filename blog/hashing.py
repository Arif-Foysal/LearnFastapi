from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def bcrypt(password:str):
    hashed_pwd = pwd_context.hash(password)
    return hashed_pwd
