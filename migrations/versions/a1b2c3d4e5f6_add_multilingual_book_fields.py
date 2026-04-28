"""add multilingual book fields

Revision ID: a1b2c3d4e5f6
Revises: 2679fcd9900f
Create Date: 2026-04-26 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = 'a1b2c3d4e5f6'
down_revision = ('2679fcd9900f', '98cc45eb1df4')
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title_ka', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('title_en', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('title_it', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('description_ka', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('description_en', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('description_it', sa.String(), nullable=True))

    op.execute("UPDATE books SET title_ka = title, title_en = title, title_it = title")
    op.execute("UPDATE books SET description_ka = description, description_en = description, description_it = description")

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.alter_column('title_ka', nullable=False)
        batch_op.alter_column('title_en', nullable=False)
        batch_op.alter_column('title_it', nullable=False)
        batch_op.alter_column('description_ka', nullable=False)
        batch_op.alter_column('description_en', nullable=False)
        batch_op.alter_column('description_it', nullable=False)
        batch_op.drop_column('title')
        batch_op.drop_column('description')


def downgrade():
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    op.execute("UPDATE books SET title = title_ka, description = description_ka")

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.alter_column('title', nullable=False)
        batch_op.alter_column('description', nullable=False)
        batch_op.drop_column('title_ka')
        batch_op.drop_column('title_en')
        batch_op.drop_column('title_it')
        batch_op.drop_column('description_ka')
        batch_op.drop_column('description_en')
        batch_op.drop_column('description_it')