# Generated by Django 3.0.14 on 2022-11-30 15:44

import core.fields
import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('validity_from', core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now)),
                ('validity_to', core.fields.DateTimeField(blank=True, db_column='ValidityTo', null=True)),
                ('legacy_id', models.IntegerField(blank=True, db_column='LegacyID', null=True)),
                ('id', models.AutoField(db_column='grievanceID', primary_key=True, serialize=False)),
                ('uuid', models.CharField(db_column='grievanceUUID', default=uuid.uuid4, max_length=36, unique=True)),
                ('benficiary', models.CharField(blank=True, db_column='beneficiary', max_length=255, null=True)),
                ('creation_date', models.DateField(blank=True, db_column='creationDate', null=True)),
                ('status', models.CharField(blank=True, choices=[('Open', 'Open'), ('Close', 'Close'), ('In Progress', 'In Progress')], db_column='Status', default='Open', max_length=36, null=True)),
                ('description', models.CharField(blank=True, db_column='description', max_length=255, null=True)),
                ('type_of_grievance', models.CharField(blank=True, choices=[('Inquiry', 'Inquiry'), ('Problem', 'Problem'), ('General', 'General')], db_column='typeOfGrievance', default='General', max_length=36, null=True)),
                ('comments', models.CharField(blank=True, db_column='comments', max_length=36, null=True)),
                ('created_by', models.DateField(blank=True, db_column='createdBy', null=True)),
                ('close_date', models.DateField(blank=True, db_column='closeDate', null=True)),
            ],
            options={
                'db_table': 'tblGrievance',
                'managed': True,
            },
        ),
    ]
