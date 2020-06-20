"""settings

Revision ID: 77870ae5b560
Revises: d5d1163f33a3
Create Date: 2020-06-19 21:35:33.523394

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '77870ae5b560'
down_revision = 'd5d1163f33a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('setting',
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('welcome_speech', sa.String(length=1000), nullable=False),
    sa.Column('color_button', sa.String(length=6), nullable=False),
    sa.Column('community_id', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('manager', sa.Column('is_blocked', sa.Boolean(), nullable=False))
    op.drop_column('manager', 'community_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('manager', sa.Column('community_id', mysql.BIGINT(), autoincrement=False, nullable=False))
    op.drop_column('manager', 'is_blocked')
    op.drop_table('setting')
    # ### end Alembic commands ###