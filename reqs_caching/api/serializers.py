import json
import xmltodict
from rest_framework import serializers

from cacher.models import Request, Response


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['url', 'method', 'headers', 'body']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['headers']:
            data['headers'] = json.loads(data['headers'])
        if data['body']:
            if data['headers'].get('Content-Type', '').startswith(
                    'application/json'):
                data['body'] = json.loads(data['body'])
            elif data['headers'].get('Content-Type', '').startswith(
                    'application/xml'):
                data['body'] = xmltodict.parse(data['body'])
        return data


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ['url', 'status_code', 'headers', 'body']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['headers']:
            data['headers'] = json.loads(data['headers'])
        if data['body']:
            if data['headers'].get('Content-Type', '').startswith(
                    'application/json'):
                data['body'] = json.loads(data['body'])
            elif data['headers'].get('Content-Type', '').startswith(
                    'application/xml'):
                data['body'] = xmltodict.parse(data['body'])
        return data
