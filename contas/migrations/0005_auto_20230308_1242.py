# Generated by Django 3.2 on 2023-03-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_alter_transacao_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
    ]