from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import WorkOrder
from .serializers import (
    CleaningWorkOrderSerialzer,
    MaidRequestSerializer,
    TechnicianRequestSerializer,
    AmenityRequestSerializer,
)


class CleaningWorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.filter(order_type="Cleaning")
    serializer_class = CleaningWorkOrderSerialzer

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_maid_supervisor():
            return Response(
                "Cleaning work orders can only be created by Maid Supervisors.",
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer.save(created_by=user, order_type="Cleaning", status="Created")


class MaidRequestViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.filter(order_type="Maid Request")
    serializer_class = MaidRequestSerializer

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_maid_supervisor():
            return Response(
                "Maid requests can only be created by Maid Supervisors.",
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer.save(created_by=user, order_type="Maid Request", status="Created")


class TechnicianRequestViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.filter(order_type="Technician Request")
    serializer_class = TechnicianRequestSerializer

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_technician_supervisor():
            return Response(
                "Technician request cannot be created by Technician Supervisors.",
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer.save(
            created_by=user, order_type="Technician Request", status="Created"
        )


class AmenityRequestViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = AmenityRequestSerializer

    def perform_create(self, serializer):
        user = self.request.user

        if not user.is_guest():
            return Response(
                "Amenity requests can only be created by guests.",
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer.save(created_by=user, order_type="Amenity Request", status="Created")
