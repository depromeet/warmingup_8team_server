"""update user

Revision ID: 814478712e18
Revises: 34540160d4c7
Create Date: 2019-10-26 23:27:54.114111

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '814478712e18'
down_revision = '34540160d4c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('gender', sa.Boolean(), nullable=True))
    op.add_column('User', sa.Column('profile_url', sa.String(), nullable=True))
    op.add_column(
        'User', sa.Column('thumbnail_url', sa.String(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'thumbnail_url')
    op.drop_column('User', 'profile_url')
    op.drop_column('User', 'gender')
    # ### end Alembic commands ###
