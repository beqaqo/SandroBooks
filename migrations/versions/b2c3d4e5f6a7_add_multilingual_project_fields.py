"""add multilingual project fields

Revision ID: b2c3d4e5f6a7
Revises: a1b2c3d4e5f6
Create Date: 2026-04-26 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = 'b2c3d4e5f6a7'
down_revision = 'a1b2c3d4e5f6'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title_ka', sa.String(128), nullable=True))
        batch_op.add_column(sa.Column('title_en', sa.String(128), nullable=True))
        batch_op.add_column(sa.Column('title_it', sa.String(128), nullable=True))
        batch_op.add_column(sa.Column('description_ka', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('description_en', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('description_it', sa.Text(), nullable=True))

    op.execute("UPDATE projects SET title_ka = title, title_en = title, title_it = title")
    op.execute("UPDATE projects SET description_ka = description, description_en = description, description_it = description")

    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.alter_column('title_ka', nullable=False)
        batch_op.alter_column('title_en', nullable=False)
        batch_op.alter_column('title_it', nullable=False)
        batch_op.alter_column('description_ka', nullable=False)
        batch_op.alter_column('description_en', nullable=False)
        batch_op.alter_column('description_it', nullable=False)
        batch_op.drop_column('title')
        batch_op.drop_column('description')


def downgrade():
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(128), nullable=True))
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=True))

    op.execute("UPDATE projects SET title = title_ka, description = description_ka")

    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.alter_column('title', nullable=False)
        batch_op.alter_column('description', nullable=False)
        batch_op.drop_column('title_ka')
        batch_op.drop_column('title_en')
        batch_op.drop_column('title_it')
        batch_op.drop_column('description_ka')
        batch_op.drop_column('description_en')
        batch_op.drop_column('description_it')