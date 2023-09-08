from pydantic import BaseModel


class TaskSubset(BaseModel):
    task_id: int
    description: str
