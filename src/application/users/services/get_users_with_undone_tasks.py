from src.application.database import transaction
from src.infrastructure.database.schemas import Todoes, User


@transaction
def get_users_with_undone_tasks(session):
    users_with_undone_tasks = session.query(User).join(User.tasks).filter(Todoes.complete.is_(False)).distinct().all()
    print("Users with undone tasks:", users_with_undone_tasks)
    return users_with_undone_tasks


users_with_undone_tasks = get_users_with_undone_tasks()

for user in users_with_undone_tasks:
    print(user.tasks)
