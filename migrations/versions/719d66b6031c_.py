"""empty message

Revision ID: 719d66b6031c
Revises: 
Create Date: 2023-12-26 10:26:23.423054

"""
from alembic import op
import sqlalchemy as sa


revision = '719d66b6031c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('folder', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])



def downgrade():
    with op.batch_alter_table('folder', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

