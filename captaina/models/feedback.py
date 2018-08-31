import pymodm as modm
import pymongo as mongo
from datetime import datetime

class Feedback(modm.MongoModel):
    message = modm.fields.CharField(required = True)
    created = modm.fields.DateTimeField(default = datetime.now)
    modified  = modm.fields.DateTimeField(default = datetime.now)

    def save(self, *args, **kwargs):
        self.modified = datetime.now()
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
