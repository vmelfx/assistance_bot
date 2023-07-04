from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from src.infrastructure.database.services.session import engine

Base = declarative_base()


def create_db():
    Base.metadata.create_all(bind=engine)


class User(Base):
    __tablename__ = "user"
    chat_id = Column(Integer, primary_key=True)
    tasks = relationship("Todoes", back_populates="user")

    def __repr__(self):
        return f"User(chat_id={self.chat_id})"


class Todoes(Base):
    __tablename__ = "todoes"

    task_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.chat_id"))
    user = relationship("User", back_populates="tasks")
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)

    def __repr__(self):
        return (
            f"Tasks [ID: {self.task_id}, User: {self.user_id}, Title: {self.title},"
            f"Description: {self.description}, Priority: {self.priority}, Completed: {self.complete}]",
        )