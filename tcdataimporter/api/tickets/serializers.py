from rest_framework import serializers
from tickets.models import Ticket, TICKET_STATUS
from djangoserver.settings import DATETIME_FORMAT
from djangoserver.settings import TIME_ZONE

class TicketSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    created = serializers.DateTimeField(format = DATETIME_FORMAT, default_timezone=TIME_ZONE)
    status = serializers.ChoiceField(choices=TICKET_STATUS, default='WAITING')

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.created = validated_data.get('created', instance.created)
        instance.status = validated_data.get('status', instance.status)

        instance.save()
        return instance