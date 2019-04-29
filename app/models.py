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
    app_type = CharField(null=True)
    name = CharField(null=True)
    is_free = BooleanField(null=True)
    detailed_description = TextField(null=True)
    about_the_game = TextField(null=True)
    pc_requirements = JSONField(null=True)
    mac_requirements = JSONField(null=True)
    linux_requirements = JSONField(null=True)
    initial_price = IntegerField(null=True)
    final_price = IntegerField(null=True)
    discount_percent = IntegerField(null=True)
    price_currency = CharField(null=True)
    windows_compatible = BooleanField(null=True)
    mac_compatible = BooleanField(null=True)
    linux_compatible = BooleanField(null=True)
    genres = JSONField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    is_junk = BooleanField(default=False)
