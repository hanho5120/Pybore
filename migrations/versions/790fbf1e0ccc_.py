"""empty message

Revision ID: 790fbf1e0ccc
Revises: 7e8590815d20
Create Date: 2021-05-10 13:28:26.516838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '790fbf1e0ccc'
down_revision = '7e8590815d20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
