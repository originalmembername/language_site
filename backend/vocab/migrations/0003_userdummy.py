# Generated by Django 2.1.2 on 2019-06-01 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0002_auto_20190209_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDummy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('vocabList', models.ManyToManyField(to='vocab.Vocabs')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]