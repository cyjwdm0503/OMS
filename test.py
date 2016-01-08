import os
import sys
import  time

import django
from django.test import  Client

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trade_sys.settings")
django.setup()

newtime = 0
for page in range(1,100):
    client = Client()
    begintime = time.time()
    name  = '/%d/' % (1)
    response = client.get(name)
    endtime  = time.time()
    print ((endtime-begintime)*1000)