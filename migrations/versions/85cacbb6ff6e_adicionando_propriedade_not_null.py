"""adicionando propriedade not null

Revision ID: 85cacbb6ff6e
Revises: 276ce945c473
Create Date: 2022-04-13 14:16:11.880952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85cacbb6ff6e'
down_revision = '276ce945c473'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vaccine_cards', 'health_unit_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vaccine_cards', 'health_unit_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###