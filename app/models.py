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

    appid = IntegerField(primary_key=True)
    name = CharField()
    is_free = BooleanField()
    detailed_description = TextField()
    about_the_game = TextField()
    pc_requirements = JSONField()
    mac_requirements = JSONField()
    linux_requirements = JSONField()
    price = DecimalField()
    price_currency = CharField()
    windows_compatible = BooleanField()
    mac_compatible = BooleanField()
    linux_compatible = BooleanField()
    genres = JSONField()

    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(Game, self).save(*args, **kwargs)
