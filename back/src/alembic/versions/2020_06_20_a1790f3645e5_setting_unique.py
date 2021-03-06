"""setting_unique

Revision ID: a1790f3645e5
Revises: 89630777d5b5
Create Date: 2020-06-20 07:51:03.360312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1790f3645e5'
down_revision = '89630777d5b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'setting', ['community_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'setting', type_='unique')
    # ### end Alembic commands ###
