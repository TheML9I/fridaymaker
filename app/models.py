import datetime

from peewee import *
from playhouse.postgres_ext import *


db = PostgresqlExtDatabase(
    database='steamdb',
    user='steamdb',
    password='steamdb',
    port=5432
)


class BaseModel(Model):
    class Meta:
        database = db


class Game(BaseModel):
    class Meta:
        db_table = 'games'

    id = PrimaryKeyField()
    appid = IntegerField(null=True)
    name = CharField(null=True)
    is_free = BooleanField(null=True)
    detailed_description = TextField(null=True)
    about_the_game = TextField(null=True)
    pc_requirements = JSONField(null=True)
    mac_requirements = JSONField(null=True)
    linux_requirements = JSONField(null=True)
    price = DecimalField(null=True)
    price_currency = CharField(null=True)
    windows_compatible = BooleanField(null=True)
    mac_compatible = BooleanField(null=True)
    linux_compatible = BooleanField(null=True)
    genres = JSONField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
