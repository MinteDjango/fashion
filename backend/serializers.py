from fashiongebeya.models import Item
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Item
        fields = ["id", "caption", "price", "image", "image_url"]

    def get_image_url(self, obj):
        return obj.image.url