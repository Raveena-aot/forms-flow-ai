"""empty message

Revision ID: c8e7baa093ba
Revises: 77d8b68e6c1f
Create Date: 2024-06-12 15:16:54.882030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8e7baa093ba'
down_revision = '77d8b68e6c1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    conn.execute(sa.text('''
    UPDATE public."filter" f SET criteria = (f.criteria::jsonb - 'processDefinitionNameLike') || 
    jsonb_build_object('processDefinitionKey', fpm.process_key) FROM public.form_process_mapper fpm
    WHERE f.criteria IS NOT NULL AND f.criteria::jsonb->>'processDefinitionNameLike' LIKE '%' || SPLIT_PART(fpm.process_name, ' (', 1) || '%';
 '''))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
