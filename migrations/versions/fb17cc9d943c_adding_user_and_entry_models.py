"""Adding user and entry models

Revision ID: fb17cc9d943c
Revises: 
Create Date: 2023-05-22 11:58:37.789707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb17cc9d943c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=70), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city_name', sa.String(length=70), nullable=False),
    sa.Column('weather', sa.String(length=70), nullable=False),
    sa.Column('humidity', sa.Float(), nullable=False),
    sa.Column('temp', sa.Float(), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entries')
    op.drop_table('users')
    # ### end Alembic commands ###
