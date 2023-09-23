from rest_framework import serializers
from .models import WorkOrder


class CleaningWorkOrderSerialzer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ["room", "status"]

    def validate(self, data):
        user = self.context["request"].user

        if not user.is_maid_uservisor():
            raise serializers.ValidationError(
                "Cleaning work orders can only be created by Maid Supervisors."
            )

        return data


class MaidRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ["room", "description"]

    def validate(self, data):
        user = self.context["request"].user

        if not user.is_maid_supervisor():
            raise serializers.ValidationError(
                "Maid requests can only be created by Maid Supervisors."
            )

        return data


class TechnicianRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ["room", "defect_type"]

    def validate(self, data):
        user = self.context["request"].user

        if user.is_technician_supervisor():
            raise serializers.ValidationError(
                "Technician requests cannot be created by Technician Supervisors."
            )

        return data


class AmenityRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ["room", "amenity_type", "quantity"]

    def validate(self, data):
        user = self.context["request"].user

        if not user.is_guest():
            raise serializers.ValidationError(
                "Amenity requests can only be created by guests."
            )

        return data
