import sqlalchemy
from db_data.db_session import SqlAlchemyBase


class Greeting(SqlAlchemyBase):
    __tablename__ = 'Greeting'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    thumbnail = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    info_channel = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    send_channel = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    role = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    color_embed = sqlalchemy.Column(sqlalchemy.String, nullable=True)


class Agreement(SqlAlchemyBase):
    __tablename__ = 'Agreement'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    color_embed = sqlalchemy.Column(sqlalchemy.String, nullable=True)


class Helper(SqlAlchemyBase):
    __tablename__ = 'Helper'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speech_1 = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    image_1 = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)
    speech_2 = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    image_2 = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)
    speech_3 = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    image_3 = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)
    color_embed = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    icon = sqlalchemy.Column(sqlalchemy.BLOB, nullable=True)