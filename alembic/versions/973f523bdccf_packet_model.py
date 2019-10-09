"""packet model

Revision ID: 973f523bdccf
Revises: 
Create Date: 2019-10-09 16:51:27.805902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '973f523bdccf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Packet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('request_header', sa.JSON(), nullable=True),
    sa.Column('request_body', sa.JSON(), nullable=True),
    sa.Column('response_header', sa.JSON(), nullable=True),
    sa.Column('response_body', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Packet')
    # ### end Alembic commands ###