# Generated by Django 2.2.1 on 2019-05-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20190511_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Influence',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('points', models.IntegerField()),
            ],
            options={
                'db_table': 'Influence',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserDatabase',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('followers', models.IntegerField()),
                ('influence_points', models.IntegerField()),
                ('flag', models.BooleanField()),
            ],
            options={
                'db_table': 'user_database',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Hashtags',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
