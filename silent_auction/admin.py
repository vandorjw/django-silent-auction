# -*- coding: utf-8 -*-
from django.contrib import admin
from parler.admin import (
    TranslatableAdmin,
    TranslatableStackedInline,
)
from silent_auction.models import (
    Bid,
    Event,
    EventAdmin,
    Item,
)


class ItemInline(TranslatableStackedInline):
    model = Item
    extra = 0



@admin.register(Bid)
class BidAdminConf(admin.ModelAdmin):
    list_display = [
        'pk',
    ]


@admin.register(Event)
class EventAdminConf(TranslatableAdmin):
    list_display = [
        'pk', 'name', 'owner', 'start_date_time', 'end_date_time',
    ]
    inlines = [
        ItemInline,
    ]


@admin.register(EventAdmin)
class EventAdminAdminConf(admin.ModelAdmin):
    list_display = [
        'pk', 'user', 'event',
    ]



@admin.register(Item)
class ItemAdminConf(TranslatableAdmin):
    list_display = [
        'pk', 'seller', 'retail_value', 'min_bid', 'event', 'name', 'slug',
    ]
