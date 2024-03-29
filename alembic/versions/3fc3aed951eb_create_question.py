"""create question

Revision ID: 3fc3aed951eb
Revises: c5861c12f746
Create Date: 2019-11-02 16:12:21.085287

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '3fc3aed951eb'
down_revision = 'c5861c12f746'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'Question',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('message', sa.String(), nullable=True),
        sa.Column('answer', sa.String(), nullable=True),
        sa.Column('bot_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['bot_id'], ['Bot.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Question')
    # ### end Alembic commands ###
