# Generated by Django 4.0.2 on 2022-03-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.CharField(max_length=100)),
                ('econtact', models.CharField(max_length=100)),
                ('eage', models.IntegerField()),
            ],
            options={
                'db_table': 'employee1',
            },
        ),
    ]