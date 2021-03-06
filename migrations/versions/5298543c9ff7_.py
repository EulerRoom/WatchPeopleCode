"""empty message

Revision ID: 5298543c9ff7
Revises: 3e8403e6cdf1
Create Date: 2015-05-07 21:19:26.417832

"""

# revision identifiers, used by Alembic.
revision = '5298543c9ff7'
down_revision = '3e8403e6cdf1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stream', 'need_to_notify_subscribers')
    op.add_column('streamer', sa.Column('need_to_notify_subscribers', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('streamer', 'need_to_notify_subscribers')
    op.add_column('stream', sa.Column('need_to_notify_subscribers', sa.BOOLEAN(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
