"""empty message

Revision ID: 33dc40a1e6b3
Revises: c4d9324867c
Create Date: 2015-06-11 22:20:32.182176

"""

# revision identifiers, used by Alembic.
revision = '33dc40a1e6b3'
down_revision = 'c4d9324867c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stream_tag')
    op.drop_table('tag')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('name', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('name', name=u'tag_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('stream_tag',
    sa.Column('stream_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tag_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['stream_id'], [u'stream.id'], name=u'stream_tag_stream_id_fkey'),
    sa.ForeignKeyConstraint(['tag_name'], [u'tag.name'], name=u'stream_tag_tag_name_fkey')
    )
    ### end Alembic commands ###