# Generated by Django 2.2.5 on 2019-10-15 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='please',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=120)),
                ('reg_no', models.IntegerField(default=0)),
                ('message', models.TextField(default='best')),
            ],
        ),
    ]
