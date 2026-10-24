from pydantic import BaseModel, EmailStr


class UsuarioCreate(BaseModel):
    email: EmailStr
    senha: str


class UsuarioRead(BaseModel):
    id: int
    email: EmailStr
