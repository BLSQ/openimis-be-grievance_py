# Generated by Django 3.2.16 on 2023-03-20 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0008_add_enrollment_officer_gql_query_location_right'),
        ('ticket', '0011_remove_ticket_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='current_village',
            field=models.ForeignKey(blank=True, db_column='CurrentVillage', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='location.location'),
        ),
    ]
