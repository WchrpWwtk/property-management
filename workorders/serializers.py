from rest_framework import serializers
from .models import WorkOrder, PropertyUser


class CleaningWorkOrderSerialzer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = [
            "room",
            "started_at",
            "finished_at",
            "status",
            "created_by",
            "assigned_to",
        ]

    def validate(self, data):
        user = self.context["request"].user

        if user.user_role != "Maid Supervisor":
            raise serializers.ValidationError(
                "Cleaning work orders can only be created by Maid Supervisors."
            )

        return data


class MaidRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = [
            "room",
            "started_at",
            "finished_at",
            "description",
            "created_by",
            "assigned_to",
        ]

    def validate(self, data):
        user = self.context["request"].user

        if user.user_role != "Maid Supervisor":
            raise serializers.ValidationError(
                "Maid requests can only be created by Maid Supervisors."
            )

        return data


class TechnicianRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = [
            "room",
            "started_at",
            "finished_at",
            "defect_type",
            "created_by",
            "assigned_to",
        ]

    def validate(self, data):
        user = self.context["request"].user

        if user.user_role == "Technician Supervisor":
            raise serializers.ValidationError(
                "Technician requests cannot be created by Technician Supervisors."
            )

        return data


class AmenityRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = [
            "room",
            "started_at",
            "finished_at",
            "amenity_type",
            "quantity",
            "created_by",
            "assigned_to",
        ]

    def validate(self, data):
        user = self.context["request"].user

        if user.user_role != "Guest":
            raise serializers.ValidationError(
                "Amenity requests can only be created by guests."
            )

        return data
