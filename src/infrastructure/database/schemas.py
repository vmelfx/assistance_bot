from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


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
    date = Column("creation_date", Date)
    task_description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)

    def __repr__(self):
        return (
            f"Tasks [ID: {self.task_id}, User: {self.user_id}, "
            f"Description: {self.task_description}, Priority: {self.priority}, Completed: {self.complete}]"
        )
