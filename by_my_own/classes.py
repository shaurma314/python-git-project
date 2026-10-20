from pydantic import BaseModel, Field
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
class CreateUser(BaseModel):
    name: str = Field(min_length=2, max_length=15)
    age: int = Field(ge= 0, le = 100)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(nullable= False)

class PatchUser(BaseModel):
    name: str | None = Field(default = None, min_length=2, max_length=15)
    age: int | None = Field(default = None, ge= 0, le = 100)


    