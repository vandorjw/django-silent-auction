# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 17:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bidder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auction_bids', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bids',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=160)),
                ('slug', models.SlugField(max_length=160)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='EventAdmin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silent_auction.Event')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Event Admin',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=160)),
                ('slug', models.SlugField(max_length=160)),
                ('description', models.TextField()),
                ('retail_value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('min_bid', models.DecimalField(decimal_places=2, max_digits=7)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='silent_auction.Event')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auction_items', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=160, unique=True)),
                ('slug', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='silent_auction.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auction_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bid',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='silent_auction.Item'),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('event', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('name', 'location'), ('slug', 'location')]),
        ),
    ]