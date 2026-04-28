"""add multilingual series fields

Revision ID: d4e5f6a7b8c9
Revises: c3d4e5f6a7b8
Create Date: 2026-04-26 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = 'd4e5f6a7b8c9'
down_revision = 'c3d4e5f6a7b8'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('series', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title_ka', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('title_en', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('title_it', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('description_ka', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('description_en', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('description_it', sa.Text(), nullable=True))

    op.execute("UPDATE series SET title_ka = title, title_en = title, title_it = title")
    op.execute("UPDATE series SET description_ka = description, description_en = description, description_it = description")

    with op.batch_alter_table('series', schema=None) as batch_op:
        batch_op.alter_column('title_ka', nullable=False)
        batch_op.alter_column('title_en', nullable=False)
        batch_op.alter_column('title_it', nullable=False)
        batch_op.alter_column('description_ka', nullable=False)
        batch_op.alter_column('description_en', nullable=False)
        batch_op.alter_column('description_it', nullable=False)
        batch_op.drop_column('title')
        batch_op.drop_column('description')


def downgrade():
    with op.batch_alter_table('series', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=True))

    op.execute("UPDATE series SET title = title_ka, description = description_ka")

    with op.batch_alter_table('series', schema=None) as batch_op:
        batch_op.alter_column('title', nullable=False)
        batch_op.alter_column('description', nullable=False)
        batch_op.drop_column('title_ka')
        batch_op.drop_column('title_en')
        batch_op.drop_column('title_it')
        batch_op.drop_column('description_ka')
        batch_op.drop_column('description_en')
        batch_op.drop_column('description_it')