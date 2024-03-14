"""added select_all_field in mapper for task_variable

Revision ID: d833f3edc621
Revises: 76ee53eb640a
Create Date: 2024-03-06 15:57:28.788294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd833f3edc621'
down_revision = '76ee53eb640a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('form_process_mapper', sa.Column('selected_all_field', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('form_process_mapper', 'selected_all_field')
    # ### end Alembic commands ###
