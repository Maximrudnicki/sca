from rest_framework import serializers

from .models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target

        fields = ("id", "name", "country", "notes", "is_completed", "mission")


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True, read_only=True)

    class Meta:
        model = Mission

        fields = ("id", "name", "cat", "is_completed", "targets")
