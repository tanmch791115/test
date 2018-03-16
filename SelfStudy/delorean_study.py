__author__ = 'tanmch791115'

from datetime import datetime
import pytz

est=pytz.timezone('US/Eastern')
d=datetime.now(pytz.utc)
d=est.normalize(d.astimezone(est))


from delorean import Delorean

d=Delorean()
d=d.shift('US/Eastern')
d.next_day(1)
d.next_tuesday()
