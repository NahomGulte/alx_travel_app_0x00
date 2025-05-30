from rest_framework import serializers
from .models import Listing 
from .models import Booking 
from .models import Message
from .models import Chat

class BookingSerializer(serializers.ModelSerializer):
    message_id = serializers.CharField(max_length=255)
    summary = serializers.SerializerMethodField()
    class Meta:
        model = Booking
        fields = '__all__'
class ListingSerializer(serializers.ModelSerializer):
    message_body = serializers.CharField(max_length=255)
    summary = serializers.SerializerMethodField()
    class Meta:
        model = Listing
        fields = '__all__'        
    def validate_message(self, obj):
        if ( message_body =! obj.conversation_id):
            raise serializers.ValidationError("Title is too short.")
        return value
