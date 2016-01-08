# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class FillCreate(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=16)
    pid = models.IntegerField()
    osuid = models.CharField(max_length=16)
    app = models.CharField(max_length=16)
    uid = models.CharField(max_length=8)
    tstamp = models.DateTimeField()
    ofid = models.IntegerField()
    pfid = models.IntegerField()
    ooid = models.IntegerField()
    qty = models.IntegerField()
    px = models.DecimalField(max_digits=12, decimal_places=6)
    exch = models.CharField(max_length=4)
    exid = models.CharField(max_length=32)
    cbrk = models.CharField(max_length=8)
    ebrk = models.CharField(max_length=8)
    smsg = models.CharField(max_length=32)

    def getStr(self):
        msg = "%s\thostname:%s\tooid:%d\tqty:%d\tpx:%lf" % (self._meta.db_table,self.hostname,self.ooid,self.qty,self.px)
        return msg

    def getooidStr(self):
        return str(self.ooid)

    class Meta:
        managed = False
        db_table = 'fill_create'


class FillTransactionLog(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    ofid = models.IntegerField()
    errmsg = models.TextField(blank=True, null=True)
    tstamp = models.DateTimeField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)

    def getStr(self):
        msg = "%s\thostname:%s\tooid:%d\tquery:%s" % (self._meta.db_table,self.hostname,self.ooid,self.query)
        return msg

    def getooidStr(self):
        return str(self.ooid)

    class Meta:
        managed = False
        db_table = 'fill_transaction_log'


class Fills(models.Model):
    ofid = models.IntegerField(primary_key=True)
    seqnum = models.IntegerField()
    pfid = models.IntegerField()
    ooid = models.IntegerField()
    qty = models.IntegerField()
    px = models.DecimalField(max_digits=12, decimal_places=6)
    exch = models.CharField(max_length=4)
    exid = models.CharField(max_length=32)
    cbrk = models.CharField(max_length=8)
    ebrk = models.CharField(max_length=8)
    smsg = models.CharField(max_length=32)
    fstate = models.TextField()  # This field type is a guess.
    cstamp = models.DateTimeField()
    lstamp = models.DateTimeField()

    def getStr(self):
        msg = "%s\tooid:%d\tqty:%d\tpx:%lf\tfstate:%s" % (self._meta.db_table,self.ooid,self.qty,self.px,self.fstate)
        return msg

    def getooidStr(self):
        return str(self.ooid)

    class Meta:
        managed = False
        db_table = 'fills'


class OrderAcceptReplace(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=16)
    pid = models.IntegerField()
    osuid = models.CharField(max_length=16)
    app = models.CharField(max_length=16)
    uid = models.CharField(max_length=8)
    tstamp = models.DateTimeField()
    ooid = models.IntegerField()
    def getStr(self):
        msg = "%s\thostname:%s\tooid:%d\t" % (self._meta.db_table,self.hostname,self.ooid)
        return msg

    def getooidStr(self):
        return str(self.ooid)
    class Meta:
        managed = False
        db_table = 'order_accept_replace'


class OrderAck(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=16)
    pid = models.IntegerField()
    osuid = models.CharField(max_length=16)
    app = models.CharField(max_length=16)
    uid = models.CharField(max_length=8)
    tstamp = models.DateTimeField()
    ooid = models.IntegerField()
    def getStr(self):
        msg = "%s\thostname:%s\tooid:%d\t" % (self._meta.db_table,self.hostname,self.ooid)
        return msg

    def getooidStr(self):
        return str(self.ooid)
    class Meta:
        managed = False
        db_table = 'order_ack'


class OrderCancel(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=16)
    pid = models.IntegerField()
    osuid = models.CharField(max_length=16)
    app = models.CharField(max_length=16)
    uid = models.CharField(max_length=8)
    tstamp = models.DateTimeField()
    ooid = models.IntegerField()
    def getStr(self):
        msg = "%s\thostname:%s\tooid:%d\t" % (self._meta.db_table,self.hostname,self.ooid)
        return msg

    def getooidStr(self):
        return str(self.ooid)
    class Meta:
        managed = False
        db_table = 'order_cancel'


class OrderClose(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=16)
    pid = models.IntegerField()
    osuid = models.CharField(max_length=16)
    app = models.CharField(max_length=16)
    uid = models.CharField(max_length=8)
    tstamp = models.DateTimeField()
    ooid = models.IntegerField()
    def getStr(self):
        msg = "%s\thostname:%s\tooid:%d\t" % (self._meta.db_table,self.hostname,self.ooid)
        return msg

    def getooidStr(self):
        return str(self.ooid)
    class Meta:
        managed = False
        db_table = 'order_close'


class OrderCreate(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=16)
    pid = models.IntegerField()
    osuid = models.CharField(max_length=16)
    app = models.CharField(max_length=16)
    uid = models.CharField(max_length=8)
    tstamp = models.DateTimeField()
    ooid = models.IntegerField()
    poid = models.IntegerField()
    acct = models.CharField(max_length=4)
    client = models.CharField(max_length=16, blank=True, null=True)
    ocap = models.CharField(max_length=1)
    ores = models.CharField(max_length=4)
    ticker = models.CharField(max_length=24)
    undly = models.CharField(max_length=24, blank=True, null=True)
    pc = models.CharField(max_length=1, blank=True, null=True)
    expiry = models.DateField(blank=True, null=True)
    strike = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    side = models.TextField()  # This field type is a guess.
    qty = models.IntegerField()
    otype = models.TextField()  # This field type is a guess.
    lmtpx = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    tif = models.TextField()  # This field type is a guess.
    oc = models.CharField(max_length=1, blank=True, null=True)
    clioid = models.CharField(max_length=24)
    cacct = models.CharField(max_length=8)
    execinst = models.CharField(max_length=8)
    rtinst = models.CharField(max_length=8)
    clrinst = models.CharField(max_length=8)
    srcuser = models.CharField(max_length=8)
    srcdesk = models.CharField(max_length=8)
    dstuser = models.CharField(max_length=8)
    dstdesk = models.CharField(max_length=8)
    exch = models.CharField(max_length=4)
    currcy = models.TextField()  # This field type is a guess.
    umsg = models.CharField(max_length=32)
    def getStr(self):
        msg = "%s\thostname:%s\tooid:%d\tside:%s\tqty:%d\totype:%s\tlmtpx:%lf\ttif:%s\toc:%s\texch:%s\tcurrcy:%s" \
              % (self._meta.db_table,self.hostname,self.ooid,self.side,self.qty,self.otype,0.0 if self.lmtpx is None else self.lmtpx,self.tif,self.oc,self.exch,self.currcy)
        return msg

    def getooidStr(self):
        return str(self.ooid)
    class Meta:
        managed = False
        db_table = 'order_create'


class OrderOut(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=16)
    pid = models.IntegerField()
    osuid = models.CharField(max_length=16)
    app = models.CharField(max_length=16)
    uid = models.CharField(max_length=8)
    tstamp = models.DateTimeField()
    ooid = models.IntegerField()
    qout = models.IntegerField()
    def getStr(self):
        msg = "%s\thostname:%s\tooid:%d\tqout:%d" % (self._meta.db_table,self.hostname,self.ooid,self.qout)
        return msg

    def getooidStr(self):
        return str(self.ooid)
    class Meta:
        managed = False
        db_table = 'order_out'


class OrderReject(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=16)
    pid = models.IntegerField()
    osuid = models.CharField(max_length=16)
    app = models.CharField(max_length=16)
    uid = models.CharField(max_length=8)
    tstamp = models.DateTimeField()
    ooid = models.IntegerField()
    smsg = models.TextField()
    def getStr(self):
        msg = "%s\thostname:%s\tooid:%d\tsmsg:%s" % (self._meta.db_table,self.hostname,self.ooid,self.smsg)
        return msg

    def getooidStr(self):
        return str(self.ooid)
    class Meta:
        managed = False
        db_table = 'order_reject'


class OrderRejectCancel(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=16)
    pid = models.IntegerField()
    osuid = models.CharField(max_length=16)
    app = models.CharField(max_length=16)
    uid = models.CharField(max_length=8)
    tstamp = models.DateTimeField()
    ooid = models.IntegerField()
    smsg = models.TextField()
    def getStr(self):
        msg = "%s\thostname:%s\tooid:%d\tsmsg:%s" % (self._meta.db_table,self.hostname,self.ooid,self.smsg)
        return msg

    def getooidStr(self):
        return str(self.ooid)
    class Meta:
        managed = False
        db_table = 'order_reject_cancel'


class OrderRejectReplace(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=16)
    pid = models.IntegerField()
    osuid = models.CharField(max_length=16)
    app = models.CharField(max_length=16)
    uid = models.CharField(max_length=8)
    tstamp = models.DateTimeField()
    ooid = models.IntegerField()
    smsg = models.TextField()
    def getStr(self):
        msg = "%s\thostname:%s\tooid:%d\tsmsg:%s" % (self._meta.db_table,self.hostname,self.ooid,self.smsg)
        return msg

    def getooidStr(self):
        return str(self.ooid)
    class Meta:
        managed = False
        db_table = 'order_reject_replace'


class OrderReplace(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=16)
    pid = models.IntegerField()
    osuid = models.CharField(max_length=16)
    app = models.CharField(max_length=16)
    uid = models.CharField(max_length=8)
    tstamp = models.DateTimeField()
    ooid = models.IntegerField()
    pqty = models.IntegerField()
    potype = models.TextField()  # This field type is a guess.
    plmtpx = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    def getStr(self):
        msg = "%s\thostname:%s\tooid:%d\tpqty:%d\tpotype:%s\tplmtpx:%lf" \
              % (self._meta.db_table,self.hostname,self.ooid,self.pqty,self.potype,0.0 if self.plmtpx is None else self.plmtpx)
        return msg

    def getooidStr(self):
        return str(self.ooid)
    class Meta:
        managed = False
        db_table = 'order_replace'


class OrderTransactionLog(models.Model):
    seqnum = models.IntegerField(primary_key=True)
    ooid = models.IntegerField()
    errmsg = models.TextField(blank=True, null=True)
    tstamp = models.DateTimeField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    def getStr(self):
        msg = "%s\tooid:%d\terrmsg:%s\tquery:%s" \
              % (self._meta.db_table,self.ooid,self.errmsg,self.query)
        return msg

    def getooidStr(self):
        return str(self.ooid)
    class Meta:
        managed = False
        db_table = 'order_transaction_log'


class Orders(models.Model):
    ooid = models.IntegerField(primary_key=True)
    seqnum = models.IntegerField()
    poid = models.IntegerField()
    acct = models.CharField(max_length=4)
    client = models.CharField(max_length=16, blank=True, null=True)
    ocap = models.CharField(max_length=1)
    ores = models.CharField(max_length=4, blank=True, null=True)
    ticker = models.CharField(max_length=24)
    undly = models.CharField(max_length=24, blank=True, null=True)
    pc = models.CharField(max_length=1, blank=True, null=True)
    expiry = models.DateField(blank=True, null=True)
    strike = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    side = models.TextField()  # This field type is a guess.
    qty = models.IntegerField()
    otype = models.TextField()  # This field type is a guess.
    lmtpx = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    pqty = models.IntegerField()
    potype = models.TextField()  # This field type is a guess.
    plmtpx = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    tif = models.TextField()  # This field type is a guess.
    oc = models.CharField(max_length=1, blank=True, null=True)
    qfilled = models.IntegerField()
    qopen = models.IntegerField()
    avgpx = models.DecimalField(max_digits=12, decimal_places=6)
    tname = models.TextField()  # This field type is a guess.
    state = models.TextField()  # This field type is a guess.
    cstate = models.TextField()  # This field type is a guess.
    rstate = models.TextField()  # This field type is a guess.
    clioid = models.CharField(max_length=24)
    cacct = models.CharField(max_length=8)
    execinst = models.CharField(max_length=8)
    rtinst = models.CharField(max_length=8)
    clrinst = models.CharField(max_length=8)
    srcuser = models.CharField(max_length=8)
    srcdesk = models.CharField(max_length=8)
    dstuser = models.CharField(max_length=8)
    dstdesk = models.CharField(max_length=8)
    exch = models.CharField(max_length=4, blank=True, null=True)
    currcy = models.TextField()  # This field type is a guess.
    umsg = models.CharField(max_length=32)
    smsg = models.CharField(max_length=32)
    cstamp = models.DateTimeField()
    lstamp = models.DateTimeField()
    def getStr(self):
        msg = "%s\tooid:%d\tside:%s\tqty:%d\totype:%s\tlmtpx:%lf\ttif:%s\toc:%s\texch:%s\tcurrcy:%s\tqfilled:%d\tqopen:%d\tstate:%s\tcstate:%s\trstate:%s\texch:%s" \
              % (self._meta.db_table,self.ooid,self.side,self.qty,self.otype,0.0 if self.lmtpx is None else self.lmtpx,self.tif,self.oc,self.exch,self.currcy,self.qfilled,self.qopen,self.state,self.cstate,self.rstate,self.exch)
        return msg

    def getooidStr(self):
        return str(self.ooid)
    class Meta:
        managed = False
        db_table = 'orders'


class Users(models.Model):
    uid = models.CharField(primary_key=True, max_length=9)
    pwd = models.CharField(max_length=32)
    select_priv = models.NullBooleanField()
    insert_priv = models.NullBooleanField()
    subscr_priv = models.NullBooleanField()
    pwd_expired = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'users'