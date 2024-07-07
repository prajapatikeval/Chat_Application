# Generated by Django 4.2.13 on 2024-06-26 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_messages_ai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='chat',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='api.chats'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='sender',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
