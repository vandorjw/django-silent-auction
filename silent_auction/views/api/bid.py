# -*- coding: utf-8 -*-
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from silent_auction.serializers import BidSerializer
from silent_auction.models import Bid


@api_view(['GET', ])
def retrieve_bid(request, bid_uuid):
    """
    """
    if request.method == 'GET':
        try:
            queryset = Bid.objects.get(pk=bid_uuid)
        except Bid.DoesNotExist:
            response_data = {
                "error": {
                    "state": "not found",
                    "details": "Bid object with ID {} could not be found.".format(bid_uuid)
                }
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = BidSerializer(queryset)
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST', ])
def create_bid(request):
    """
    """
    if request.user.is_authenticated():

        bidder = request.user
        item = "unkown"

        serializer = BidSerializer(queryset, many=True)

        response_data = {"detail": "not implemented"}
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        response_data = {"detail": "not authenticated"}
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT', ])
def update_bid(request, bid_uuid):
    """
    """
    if request.method == 'PUT':
        response_data = {"details": "not implemented"}
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def delete_bid(request, bid_uuid):
    """
    """
    if request.method == 'GET':
        response_data = {"details": "not implemented"}
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def list_bids(request):
    """
    """
    if request.method == 'GET':
        queryset = Bid.objects.all()
        serializer = BidSerializer(queryset, many=True)
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)
