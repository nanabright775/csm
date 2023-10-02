from rest_framework import serializers
from media.models import (
    TagModel,GalleryModel, ImageModel,
    Anouncement,Programs, News, Event
)

class TagModelSerializer(serializers.ModelSerializer):
    """seializer for tags"""

    class Meta:
        model = TagModel
        fields = ['id', 'tagname', 'description']
        read_only_fields = ['id']
        
        
class  GalleryModelSerializer(serializers.ModelSerializer):
    """serializers for gallery"""
    tag = TagModelSerializer
    
    class Meta:
        model = GalleryModel
        fields = ['tags', 'title', 'description', 'date_created', 'id']  
        read_only_fields = ['id']
        
class ImageSerializer(serializers.ModelSerializer):
    """serializer for uploading images to imagemodels"""
    class Meta:
        model = ImageModel
        fields =['id', 'image', ]
        read_only_fields=['id']
        extra_kwargs = {'image': {'required': 'True'}}

class ImageModelSerializer(serializers.ModelSerializer):
    """serielizers for image fields"""
    gallery = GalleryModelSerializer
    image = ImageSerializer
    class Meta:
        model = ImageModel
        fields = ['title', 'date_created', 'gallery', 'image', 'id']
        read_only_fields = ['id']

class EventSerializer(serializers.ModelSerializer):
    """serializers for event"""
    class Meta:
        model = Event
        fields = ['title', 'date_started', 'date_ended', 'description', 'image', 'id']
        read_only_fields = ['id']

class NewsSerializer(serializers.ModelSerializer):
    """serializers for News"""
    class Meta:
        model = News
        fields = ['title', 'description', 'image', 'date', 'id']
        read_only_fields = ['id']
        
        
class ProgramsSerializers(serializers.ModelSerializer):
    """serializers for programms"""
    class Meta:
        model = Programs
        fields = ['title', 'description', 'date', 'id']
        read_only_fields = ['id']
        
class AnnouncementSerielizer(serializers.ModelSerializer):
    """serializers for announcement"""
    class Meta:
        model = Anouncement
        fields = ['title', 'description', 'date', 'id']
        read_only_fields=['id']
