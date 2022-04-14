"""empty message

Revision ID: 0981bb47e7c3
Revises: 9ede4eebf8e1
Create Date: 2022-04-14 00:56:35.854352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0981bb47e7c3'
down_revision = '9ede4eebf8e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rsvp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rsvp',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event_posts.id'], name='rsvp_event_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='rsvp_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='rsvp_pkey')
    )
    # ### end Alembic commands ###