from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests as req
from requests.exceptions import Timeout


@api_view(http_method_names=['GET'])
def beautyboxes_list(request):
    ### хз, как проверить эту конструкцию на таймоут. теоретически должно работать...
    try:
        beautybox_list = req.get("https://stepik.org/media/attachments/course/73594/beautyboxes.json", timeout=10).json()
    except Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
    #######
    result = []
    if request.query_params:
        min_price = request.query_params.get('min_price')
        min_weight = request.query_params.get('min_weight')
        if min_price and not min_weight:
            for box in beautybox_list:
                if box["price"] >= int(min_price):
                    result.append(box)
            return Response(result)
        if min_weight and not min_price:
            for box in beautybox_list:
                if box["weight_grams"] >= int(min_weight):
                    result.append(box)
            return Response(result)
        if min_weight and min_price:
            for box in beautybox_list:
                if box["price"] >= int(min_price) and box["weight_grams"] >= int(min_weight):
                    result.append(box)
            return Response(result)
    if beautybox_list:
        return Response(beautybox_list)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['GET'])
def recipients_list(request):
    try:
        recipient_list = req.get("https://stepik.org/media/attachments/course/73594/recipients.json", timeout=10).json()
    except Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
    if recipient_list:
        return Response(recipient_list)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['GET'])
def beautybox_detail(request, id):
    try:
        beautyboxes_list = req.get("https://stepik.org/media/attachments/course/73594/beautyboxes.json", timeout=10).json()
    except Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
    response = None
    for indx, beautybox in enumerate(beautyboxes_list):
        if indx == id:
             response = beautybox
    if response:
        return Response(response)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['GET'])
def recipient_detail(request, id):
    try:
        recipients_list = req.get("https://stepik.org/media/attachments/course/73594/recipients.json", timeout=10).json()
    except Timeout:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
    response = None
    for indx, recipient in enumerate(recipients_list):
        if indx == id:
             response = recipient
    if response:
        return Response(response)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

