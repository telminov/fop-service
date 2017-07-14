# coding: utf-8
from rest_framework import serializers


class GeneratePdf(serializers.Serializer):
    filename = serializers.CharField()
    fo_data = serializers.CharField()
    images = serializers.ListField(
        child=serializers.ImageField(max_length=None, allow_empty_file=False)
    )
