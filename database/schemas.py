from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    chat_id = Column(Integer, primary_key=True)
    tasks = relationship("Todoes", back_populates="user")


class Todoes(Base):
    __tablename__ = "todoes"

    task_id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.chat_id"))
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
