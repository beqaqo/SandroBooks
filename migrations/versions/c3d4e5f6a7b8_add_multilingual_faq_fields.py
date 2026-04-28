"""add multilingual faq fields

Revision ID: c3d4e5f6a7b8
Revises: b2c3d4e5f6a7
Create Date: 2026-04-26 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = 'c3d4e5f6a7b8'
down_revision = 'b2c3d4e5f6a7'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('faqs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question_ka', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('question_en', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('question_it', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('answer_ka', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('answer_en', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('answer_it', sa.String(), nullable=True))

    op.execute("UPDATE faqs SET question_ka = question, question_en = question, question_it = question")
    op.execute("UPDATE faqs SET answer_ka = answer, answer_en = answer, answer_it = answer")

    with op.batch_alter_table('faqs', schema=None) as batch_op:
        batch_op.alter_column('question_ka', nullable=False)
        batch_op.alter_column('question_en', nullable=False)
        batch_op.alter_column('question_it', nullable=False)
        batch_op.alter_column('answer_ka', nullable=False)
        batch_op.alter_column('answer_en', nullable=False)
        batch_op.alter_column('answer_it', nullable=False)
        batch_op.drop_column('question')
        batch_op.drop_column('answer')


def downgrade():
    with op.batch_alter_table('faqs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('answer', sa.String(), nullable=True))

    op.execute("UPDATE faqs SET question = question_ka, answer = answer_ka")

    with op.batch_alter_table('faqs', schema=None) as batch_op:
        batch_op.alter_column('question', nullable=False)
        batch_op.alter_column('answer', nullable=False)
        batch_op.drop_column('question_ka')
        batch_op.drop_column('question_en')
        batch_op.drop_column('question_it')
        batch_op.drop_column('answer_ka')
        batch_op.drop_column('answer_en')
        batch_op.drop_column('answer_it')