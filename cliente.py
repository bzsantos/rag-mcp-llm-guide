from pydantic import BaseModel, EmailStr


class ClienteCreate(BaseModel):
    nome: str
    email: EmailStr


from pydantic import BaseModel, EmailStr


class ClienteCreate(BaseModel):
    nome: str
    email: EmailStr


class ClienteRead(BaseModel):
    id: int
    nome: str
    email: EmailStr
