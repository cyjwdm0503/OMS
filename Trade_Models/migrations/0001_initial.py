# -*- coding: utf-8 -*-
# Generated by Django 1.9.dev20150901040355 on 2015-09-16 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderAcceptReplace',
            fields=[
                ('seqnum', models.IntegerField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(blank=True, max_length=16, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('osuid', models.CharField(blank=True, max_length=16, null=True)),
                ('app', models.CharField(blank=True, max_length=16, null=True)),
                ('uid', models.CharField(blank=True, max_length=8, null=True)),
                ('tstamp', models.DateTimeField(blank=True, null=True)),
                ('ooid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_accept_replace',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderAck',
            fields=[
                ('seqnum', models.IntegerField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(blank=True, max_length=16, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('osuid', models.CharField(blank=True, max_length=16, null=True)),
                ('app', models.CharField(blank=True, max_length=16, null=True)),
                ('uid', models.CharField(blank=True, max_length=8, null=True)),
                ('tstamp', models.DateTimeField(blank=True, null=True)),
                ('ooid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_ack',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderCancel',
            fields=[
                ('seqnum', models.IntegerField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(blank=True, max_length=16, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('osuid', models.CharField(blank=True, max_length=16, null=True)),
                ('app', models.CharField(blank=True, max_length=16, null=True)),
                ('uid', models.CharField(blank=True, max_length=16, null=True)),
                ('tstamp', models.DateTimeField(blank=True, null=True)),
                ('ooid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_cancel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderCreate',
            fields=[
                ('seqnum', models.IntegerField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(blank=True, max_length=16, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('osuid', models.CharField(blank=True, max_length=16, null=True)),
                ('app', models.CharField(blank=True, max_length=16, null=True)),
                ('uid', models.CharField(blank=True, max_length=16, null=True)),
                ('tstamp', models.DateTimeField(blank=True, null=True)),
                ('ooid', models.IntegerField(blank=True, null=True)),
                ('poid', models.IntegerField(blank=True, null=True)),
                ('acct', models.CharField(blank=True, max_length=4, null=True)),
                ('client', models.CharField(blank=True, max_length=16, null=True)),
                ('ocap', models.CharField(blank=True, max_length=1, null=True)),
                ('ores', models.CharField(blank=True, max_length=4, null=True)),
                ('ticker', models.CharField(blank=True, max_length=24, null=True)),
                ('undly', models.CharField(blank=True, max_length=24, null=True)),
                ('pc', models.CharField(blank=True, max_length=1, null=True)),
                ('expiry', models.DateField(blank=True, null=True)),
                ('strike', models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True)),
                ('side', models.CharField(blank=True, max_length=8, null=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('otype', models.CharField(blank=True, max_length=8, null=True)),
                ('lmtpy', models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True)),
                ('tif', models.CharField(blank=True, max_length=8, null=True)),
                ('oc', models.CharField(blank=True, max_length=1, null=True)),
                ('clioid', models.CharField(blank=True, max_length=24, null=True)),
                ('cacct', models.CharField(blank=True, max_length=8, null=True)),
                ('execinst', models.CharField(blank=True, max_length=8, null=True)),
                ('rtinst', models.CharField(blank=True, max_length=8, null=True)),
                ('clrinst', models.CharField(blank=True, max_length=8, null=True)),
                ('srcuser', models.CharField(blank=True, max_length=8, null=True)),
                ('srcdesk', models.CharField(blank=True, max_length=8, null=True)),
                ('dstuser', models.CharField(blank=True, max_length=8, null=True)),
                ('dstdesk', models.CharField(blank=True, max_length=8, null=True)),
                ('exch', models.CharField(blank=True, max_length=8, null=True)),
                ('currcy', models.CharField(blank=True, max_length=8, null=True)),
                ('umsg', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'order_create',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderOut',
            fields=[
                ('seqnum', models.IntegerField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(blank=True, max_length=16, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('osuid', models.CharField(blank=True, max_length=16, null=True)),
                ('app', models.CharField(blank=True, max_length=16, null=True)),
                ('uid', models.CharField(blank=True, max_length=16, null=True)),
                ('tstamp', models.DateTimeField(blank=True, null=True)),
                ('ooid', models.IntegerField(blank=True, null=True)),
                ('qout', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_out',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderReject',
            fields=[
                ('sequm', models.IntegerField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(blank=True, max_length=16, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('osuid', models.CharField(blank=True, max_length=16, null=True)),
                ('app', models.CharField(blank=True, max_length=16, null=True)),
                ('uid', models.CharField(blank=True, max_length=16, null=True)),
                ('tstamp', models.DateTimeField(blank=True, null=True)),
                ('ooid', models.IntegerField(blank=True, null=True)),
                ('smsg', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_reject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderRejectCancel',
            fields=[
                ('seqnum', models.IntegerField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(blank=True, max_length=16, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('osuid', models.CharField(blank=True, max_length=16, null=True)),
                ('app', models.CharField(blank=True, max_length=16, null=True)),
                ('uid', models.CharField(blank=True, max_length=8, null=True)),
                ('tstamp', models.DateTimeField(blank=True, null=True)),
                ('ooid', models.IntegerField(blank=True, null=True)),
                ('smsg', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_reject_cancel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderRejectReplace',
            fields=[
                ('seqnum', models.IntegerField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(blank=True, max_length=16, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('osuid', models.CharField(blank=True, max_length=16, null=True)),
                ('app', models.CharField(blank=True, max_length=16, null=True)),
                ('uid', models.CharField(blank=True, max_length=8, null=True)),
                ('tstamp', models.DateTimeField(blank=True, null=True)),
                ('ooid', models.IntegerField(blank=True, null=True)),
                ('smsg', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_reject_replace',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderReplace',
            fields=[
                ('seqnum', models.IntegerField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(blank=True, max_length=16, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('osuid', models.CharField(blank=True, max_length=16, null=True)),
                ('app', models.CharField(blank=True, max_length=16, null=True)),
                ('uid', models.CharField(blank=True, max_length=8, null=True)),
                ('tstamp', models.DateTimeField(blank=True, null=True)),
                ('ooid', models.IntegerField(blank=True, null=True)),
                ('pqty', models.IntegerField(blank=True, null=True)),
                ('potype', models.CharField(blank=True, max_length=8, null=True)),
                ('plmtpx', models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True)),
            ],
            options={
                'db_table': 'order_replace',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('ooid', models.IntegerField(primary_key=True, serialize=False)),
                ('seqnum', models.IntegerField(blank=True, null=True)),
                ('poid', models.IntegerField(blank=True, null=True)),
                ('acct', models.CharField(blank=True, max_length=4, null=True)),
                ('client', models.CharField(blank=True, max_length=16, null=True)),
                ('ocap', models.CharField(blank=True, max_length=1, null=True)),
                ('ores', models.CharField(blank=True, max_length=4, null=True)),
                ('ticker', models.CharField(blank=True, max_length=24, null=True)),
                ('undly', models.CharField(blank=True, max_length=24, null=True)),
                ('pc', models.CharField(blank=True, max_length=1, null=True)),
                ('expiry', models.DateField(blank=True, null=True)),
                ('strike', models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True)),
                ('side', models.CharField(blank=True, max_length=8, null=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('otype', models.CharField(blank=True, max_length=8, null=True)),
                ('lmtpy', models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True)),
                ('pqty', models.IntegerField(blank=True, null=True)),
                ('potype', models.CharField(blank=True, max_length=8, null=True)),
                ('plmtpx', models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True)),
                ('tif', models.CharField(blank=True, max_length=8, null=True)),
                ('oc', models.CharField(blank=True, max_length=1, null=True)),
                ('qfilled', models.IntegerField(blank=True, null=True)),
                ('qopen', models.IntegerField(blank=True, null=True)),
                ('avgpx', models.DecimalField(blank=True, decimal_places=6, max_digits=12, null=True)),
                ('tname', models.CharField(blank=True, max_length=16, null=True)),
                ('state', models.CharField(blank=True, max_length=8, null=True)),
                ('cstate', models.CharField(blank=True, max_length=8, null=True)),
                ('rstate', models.CharField(blank=True, max_length=8, null=True)),
                ('clioid', models.CharField(blank=True, max_length=24, null=True)),
                ('cacct', models.CharField(blank=True, max_length=8, null=True)),
                ('execinst', models.CharField(blank=True, max_length=8, null=True)),
                ('rtinst', models.CharField(blank=True, max_length=8, null=True)),
                ('clrinst', models.CharField(blank=True, max_length=8, null=True)),
                ('srcuser', models.CharField(blank=True, max_length=8, null=True)),
                ('srcdesk', models.CharField(blank=True, max_length=8, null=True)),
                ('dstuser', models.CharField(blank=True, max_length=8, null=True)),
                ('dstdesk', models.CharField(blank=True, max_length=8, null=True)),
                ('exch', models.CharField(blank=True, max_length=8, null=True)),
                ('currcy', models.CharField(blank=True, max_length=8, null=True)),
                ('umsg', models.CharField(blank=True, max_length=32, null=True)),
                ('smsg', models.CharField(blank=True, max_length=32, null=True)),
                ('cstamp', models.DateTimeField(blank=True, null=True)),
                ('lstamp', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderTransactionLog',
            fields=[
                ('seqnum', models.IntegerField(primary_key=True, serialize=False)),
                ('ooid', models.IntegerField(blank=True, null=True)),
                ('errmsg', models.TextField(blank=True, null=True)),
                ('tstamp', models.DateTimeField(blank=True, null=True)),
                ('query', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_transaction_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uid', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('pwd', models.CharField(blank=True, max_length=32, null=True)),
                ('select_priv', models.NullBooleanField()),
                ('insert_priv', models.NullBooleanField()),
                ('subscr_priv', models.NullBooleanField()),
                ('pwd_expired', models.NullBooleanField()),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
