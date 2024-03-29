"""empty message

Revision ID: 0ef5c646deca
Revises: 8cfc03dea077
Create Date: 2019-10-26 16:38:36.659802

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0ef5c646deca'
down_revision = '8cfc03dea077'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Chatroom_owner_id_fkey', 'Chatroom', type_='foreignkey')
    op.drop_column('Chatroom', 'owner_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'Chatroom',
        sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.create_foreign_key(
        'Chatroom_owner_id_fkey', 'Chatroom', 'User', ['owner_id'], ['id']
    )
    # ### end Alembic commands ###
