from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        extra_kwargs = {
            'date_created': {'read_only': True}
        }

    def validate(self, attrs):
        if not attrs['text']:
            raise serializers.ValidationError('You must enter message text')
        return super().validate(attrs)