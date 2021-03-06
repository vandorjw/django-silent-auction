# -*- coding: utf-8 -*-
import uuid
from django.urls import reverse
from django.utils import timezone
from rest_framework import serializers
from parler_rest.serializers import (
    TranslatableModelSerializer,
    TranslatedFieldsField,
)
from versatileimagefield.serializers import VersatileImageFieldSerializer
from silent_auction.models import (
    Bid,
    Event,
    EventAdministrator,
    Item,
    ItemImage,
)


class BidSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(
        read_only=True,
        default=serializers.CreateOnlyDefault(timezone.now),
    )
    modified = serializers.DateTimeField(
        read_only=True,
        default=serializers.CreateOnlyDefault(timezone.now),
    )
    pk = serializers.UUIDField(
        read_only=True,
        default=serializers.CreateOnlyDefault(uuid.uuid4),
    )

    class Meta:
        model = Bid
        fields = (
            'pk',
            'bidder',
            'item',
            'value',
            'created',
            'modified',
        )


class EventAdministratorSerializer(serializers.ModelSerializer):
    pk = serializers.UUIDField(
        read_only=True,
        default=serializers.CreateOnlyDefault(uuid.uuid4),
    )

    class Meta:
        model = EventAdministrator
        fields = (
            'pk',
            'event',
            'user',
        )


class EventSerializer(TranslatableModelSerializer):
    pk = serializers.UUIDField(
        read_only=True,
        default=serializers.CreateOnlyDefault(uuid.uuid4),
    )
    translations = TranslatedFieldsField(
        shared_model=Event,
    )
    items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:retrieve_item',
        lookup_field='pk',
        lookup_url_kwarg='item_uuid',
    )

    class Meta:
        model = Event
        fields = (
            'pk',
            'start_date_time',
            'end_date_time',
            'owner',
            'translations',
            'items',

        )


class ItemImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='item_image',
    )

    class Meta:
        model = ItemImage
        fields = (
            'image',
        )


class ItemSerializer(TranslatableModelSerializer):
    pk = serializers.UUIDField(
        read_only=True,
        default=serializers.CreateOnlyDefault(uuid.uuid4),
    )
    bids = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:retrieve_bid',
        lookup_field='pk',
        lookup_url_kwarg='bid_uuid',
    )
    event = serializers.SerializerMethodField()
    images = ItemImageSerializer(many=True, read_only=True)
    translations = TranslatedFieldsField(shared_model=Item)

    class Meta:
        model = Item
        fields = (
            'pk',
            'seller',
            'retail_value',
            'starting_value',
            'min_increase',
            'event',
            'bids',
            'translations',
            'images',
        )

    def get_event(self, obj):
        try:
            request = self.context['request']
            url = request.build_absolute_uri(reverse('api:retrieve_event', kwargs={'event_uuid': str(obj.event.pk)}))
        except:
            url = reverse('api:retrieve_event', kwargs={'event_uuid': str(obj.event.pk)})

        return {
            "pk": str(obj.event.pk),
            "name": obj.event.name,
            "url": url,
        }
