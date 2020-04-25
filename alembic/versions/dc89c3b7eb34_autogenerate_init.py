"""Autogenerate Init

Revision ID: dc89c3b7eb34
Revises: 
Create Date: 2020-04-25 18:56:38.454466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc89c3b7eb34'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('receipts')
    op.drop_table('events')
    op.drop_table('users')
    op.drop_constraint(None, 'enrollment', type_='foreignkey')
    op.drop_constraint(None, 'enrollment', type_='foreignkey')
    op.create_foreign_key(None, 'enrollment', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'enrollment', 'event', ['event_id'], ['id'])
    op.drop_column('event', 'event_id')
    op.add_column('user', sa.Column('uid', sa.Integer(), nullable=True))
    op.drop_column('user', 'file_id')
    op.drop_column('user', 'file_type')
    op.drop_column('user', 'user_id')
    op.drop_column('user', 'is_registered')
    op.drop_column('user', 'admin_check')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('admin_check', sa.BOOLEAN(), nullable=True))
    op.add_column('user', sa.Column('is_registered', sa.BOOLEAN(), nullable=True))
    op.add_column('user', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.add_column('user', sa.Column('file_type', sa.VARCHAR(length=10), nullable=True))
    op.add_column('user', sa.Column('file_id', sa.VARCHAR(length=1000), nullable=True))
    op.drop_column('user', 'uid')
    op.add_column('event', sa.Column('event_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'enrollment', type_='foreignkey')
    op.drop_constraint(None, 'enrollment', type_='foreignkey')
    op.create_foreign_key(None, 'enrollment', 'user', ['user_id'], ['user_id'])
    op.create_foreign_key(None, 'enrollment', 'event', ['event_id'], ['event_id'])
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('username', sa.VARCHAR(length=255), nullable=True),
    sa.Column('name_surname', sa.VARCHAR(length=255), nullable=True),
    sa.Column('is_registered', sa.BOOLEAN(), nullable=True),
    sa.Column('admin_check', sa.BOOLEAN(), nullable=True),
    sa.Column('file_type', sa.VARCHAR(length=10), nullable=True),
    sa.Column('file_id', sa.VARCHAR(length=1000), nullable=True),
    sa.Column('edit_datetime', sa.DATETIME(), nullable=True),
    sa.CheckConstraint('admin_check IN (0, 1)'),
    sa.CheckConstraint('is_registered IN (0, 1)'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('event_id', sa.INTEGER(), nullable=True),
    sa.Column('title', sa.VARCHAR(length=100), nullable=True),
    sa.Column('description', sa.VARCHAR(length=1000), nullable=True),
    sa.Column('hello_message', sa.VARCHAR(length=1000), nullable=True),
    sa.Column('edit_datetime', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receipts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('event_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('complete', sa.BOOLEAN(), nullable=True),
    sa.Column('admin_check', sa.BOOLEAN(), nullable=True),
    sa.Column('file_type', sa.VARCHAR(length=10), nullable=True),
    sa.Column('file_id', sa.VARCHAR(length=1000), nullable=True),
    sa.Column('edit_datetime', sa.DATETIME(), nullable=True),
    sa.CheckConstraint('admin_check IN (0, 1)'),
    sa.CheckConstraint('complete IN (0, 1)'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
