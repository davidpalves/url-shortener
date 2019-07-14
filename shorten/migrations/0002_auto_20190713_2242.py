# Generated by Django 2.2.3 on 2019-07-13 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shorten', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encurtador',
            name='cod',
        ),
        migrations.RemoveField(
            model_name='encurtador',
            name='url',
        ),
        migrations.AddField(
            model_name='encurtador',
            name='count_redirects',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='encurtador',
            name='url_hash',
            field=models.CharField(default='', max_length=80, unique=True),
        ),
        migrations.AddField(
            model_name='encurtador',
            name='url_redirect',
            field=models.URLField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='encurtador',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='urls', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
