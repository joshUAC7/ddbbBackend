# Generated by Django 4.2.2 on 2023-06-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfauth', '0002_alter_customusermodel_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='userId',
            field=models.CharField(default='40b845cf22e144b', editable=False, max_length=16, primary_key=True, serialize=False),
        ),
    ]
