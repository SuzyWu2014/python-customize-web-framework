import StringField
import Model


class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()
