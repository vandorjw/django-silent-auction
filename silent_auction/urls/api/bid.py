# -*- coding: utf-8 -*-
from django.conf.urls import url
from silent_auction.views.api import bid


urlpatterns = [
    url(
        regex=r'^$',
        view=bid.list_bids,
        name='list_bids',
    ),
    url(
        regex=r'^create/$',
        view=bid.create_bid,
        name='create_bid',
    ),
    url(
        regex=r'^update/(?P<uuid>[-\w]+)/$',
        view=bid.update_bid,
        name='update_bid',
    ),
    url(
        regex=r'^(?P<uuid>[-\w]+)/$',
        view=bid.retrieve_bid,
        name='retrieve_bid',
    ),
]