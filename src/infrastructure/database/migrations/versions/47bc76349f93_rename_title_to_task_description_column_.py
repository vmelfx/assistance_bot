"""Rename title to task_description column in  Todoes table

Revision ID: 47bc76349f93
Revises: 87d8c8ec1b19
Create Date: 2023-07-23 19:18:00.908625+03:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "47bc76349f93"
down_revision = "87d8c8ec1b19"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "todoes",
        "title",
        new_column_name="task_description",
        existing_nullable=True,
        existing_type=sa.String(),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "todoes",
        "task_description",
        new_column_name="title",
        existing_nullable=True,
        existing_type=sa.String(),
    )
    # ### end Alembic commands ###
