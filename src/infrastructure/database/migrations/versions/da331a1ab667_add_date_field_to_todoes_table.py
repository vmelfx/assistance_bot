"""Add date field to Todoes table

Revision ID: da331a1ab667
Revises: 8445969f42ce
Create Date: 2023-07-21 21:10:39.273598+03:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "da331a1ab667"
down_revision = "8445969f42ce"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("todoes", sa.Column("creation_date", sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("todoes", "creation_date")
    # ### end Alembic commands ###
