"""intial migration

Revision ID: 60471cdbe0db
Revises: 
Create Date: 2021-06-13 18:28:54.039061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60471cdbe0db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo_path', sa.String(), nullable=True),
    sa.Column('userBio', sa.String(length=255), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('pitchesCreated', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitchesCreated'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('pitches_postedBy_fkey', 'pitches', type_='foreignkey')
    op.create_foreign_key(None, 'pitches', 'profiles', ['postedBy'], ['id'])
    op.drop_constraint('users_pitchesCreated_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'userBio')
    op.drop_column('users', 'photo_path')
    op.drop_column('users', 'pitchesCreated')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pitchesCreated', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('photo_path', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('userBio', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.create_foreign_key('users_pitchesCreated_fkey', 'users', 'pitches', ['pitchesCreated'], ['id'])
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.create_foreign_key('pitches_postedBy_fkey', 'pitches', 'users', ['postedBy'], ['id'])
    op.drop_table('profiles')
    # ### end Alembic commands ###