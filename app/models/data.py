import uuid
import datetime

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Data(Model):
  id = columns.UUID(primary_key=True, default=uuid.uuid4)
  measid = columns.Integer(index=True)
  datavalue = columns.Text()
  datetime = columns.DateTime(default=datetime.datetime.now,index=True)
  flags = columns.Text()
  def __repr__(self):
    return '%d %s %s %s' % (self.measid, self.datavalue, self.datetime, self.flags)
