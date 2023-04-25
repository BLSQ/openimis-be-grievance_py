# Generated by Django 3.2.16 on 2023-03-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0013_auto_20230328_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_priority',
            field=models.CharField(choices=[('C', 'Critical'), ('H', 'High'), ('N', 'Normal'), ('L', 'Low')], db_column='TicketPriority', default='N', help_text='how critical is the problem C = Critical and L = Low ', max_length=15),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.TextField(choices=[('W', 'Waiting'), ('T', 'Todo'), ('I', 'Inprogress'), ('R', 'Review'), ('C', 'CLOSE')], db_column='TicketStatus', default='W', max_length=15),
        ),
    ]
