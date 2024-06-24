from rest_framework import serializers
from .models import Image, Review, Hotel, Package


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    package_name = serializers.ReadOnlyField(source='package.name')

    class Meta:
        model = Image
        fields = ['id', 'package', 'package_name', 'image']


class ReviewSerializer(serializers.ModelSerializer):
    reviewer_username = serializers.ReadOnlyField(source='reviewer.username')

    class Meta:
        model = Review
        fields = ['id', 'package', 'reviewer', 'reviewer_username', 'review_text', 'rating']
        read_only_fields = ['reviewer']


class PackageSerializer(serializers.ModelSerializer):
    images_set = ImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    hotels = HotelSerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = '__all__'
