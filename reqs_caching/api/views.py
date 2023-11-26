from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

import requests
import redis
import json

from cacher.models import Request, Response
from .serializers import RequestSerializer, ResponseSerializer


class MasterReqsView(APIView):
    def post(self, request):
        # Parse request data
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            method = serializer.validated_data['method']
            headers = serializer.validated_data['headers']
            body = serializer.validated_data['body']
        else:
            return Response({'error': 'Invalid request data'},
                            status=HTTP_400_BAD_REQUEST)

        # Check if request and response data is already cached in Redis
        r = redis.Redis(host='localhost', port=6379, db=0)
        request_key = f'request:{url}'
        response_key = f'response:{url}'
        request_cached = r.get(request_key)
        response_cached = r.get(response_key)

        # If request and response data is not cached,
        # make request to external API and cache it
        if request_cached is None or response_cached is None:
            response = requests.request(method,
                                        url,
                                        headers=headers,
                                        data=body)

            # Check if response is valid
            if response.status_code != 200:
                return Response(
                    {'error': 'Invalid response from external API'},
                    status=HTTP_400_BAD_REQUEST)

            # Save request and response data to database
            request_data = {
                'url': url,
                'method': method,
                'headers': json.dumps(headers),
                'body': body,
            }
            request_serializer = RequestSerializer(data=request_data)
            if request_serializer.is_valid():
                r.set(response_key, json.dumps(request_serializer.data))
                request_serializer.save()

            response_data = {
                'url': url,
                'method': response.status_code,
                'headers': json.dumps(response.headers),
                'body': response.content,
            }
            response_serializer = ResponseSerializer(data=response_data)
            if response_serializer.is_valid():
                response_serializer.save()
                r.set(response_key, json.dumps(response_serializer.data))
                return Response(response_serializer.data, status=HTTP_200_OK)

            return Response(
                {'error': 'Invalid response from external API'},
                status=HTTP_400_BAD_REQUEST)

        # Return cashed response data
        response_cached = json.loads(response_cached)
        return Response(response_cached)


class VisaReqsView(APIView):
    def put(self, request):
        # Parse request data
        body_reqst = request.data.get('body')
        req_obj = Request.objects.get(**body_reqst)
        serializer = RequestSerializer(req_obj, data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            method = serializer.validated_data['method']
            headers = serializer.validated_data['headers']
            body = serializer.validated_data['body']
        else:
            return Response({'error': 'Invalid request data'},
                            status=HTTP_400_BAD_REQUEST)

        # Check if request and response data is already cached in Redis
        r = redis.Redis(host='localhost', port=6379, db=0)
        request_key = f'request:{url}'
        response_key = f'response:{url}'
        request_cached = r.get(request_key)
        response_cached = r.get(response_key)

        # If request and response data is not cached,
        # make request to external API and cache it
        if request_cached is None or response_cached is None:
            response = requests.request(method,
                                        url,
                                        headers=headers,
                                        data=body)

            # Check if response is valid
            if response.status_code != 200:
                return Response(
                    {'error': 'Invalid response from external API'},
                    status=HTTP_400_BAD_REQUEST)

            # Save request and response data to database
            request_data = {
                'url': url,
                'method': method,
                'headers': json.dumps(headers),
                'body': body,
            }
            request_serializer = RequestSerializer(req_obj, data=request_data)
            if request_serializer.is_valid():
                request_serializer.save()
                r.set(request_key, json.dumps(request_serializer.data))

            response_data = {
                'url': url,
                'method': response.status_code,
                'headers': json.dumps(response.headers),
                'body': response.content,
            }
            response_serializer = ResponseSerializer(req_obj,
                                                     data=response_data)
            if response_serializer.is_valid():
                response_serializer.save()
                r.set(response_key, json.dumps(response_serializer.data))
                return Response(response_serializer.data, status=HTTP_200_OK)

            return Response(
                {'error': 'Invalid response from external API'},
                status=HTTP_400_BAD_REQUEST)

        # Return cashed response data
        response_cached = json.loads(response_cached)
        return Response(response_cached)
