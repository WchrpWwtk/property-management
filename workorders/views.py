from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import WorkOrder, PropertyUser
from .permissions import IsMaidSupervisorOrReadOnly, IsGuestOrReadOnly
from .serializers import (
    CleaningWorkOrderSerialzer,
    MaidRequestSerializer,
    TechnicianRequestSerializer,
    AmenityRequestSerializer,
)


class CleaningWorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.filter(order_type="Cleaning")
    serializer_class = CleaningWorkOrderSerialzer
    permission_classes = [IsMaidSupervisorOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user, order_type="Cleaning", status="Created")


class MaidRequestViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.filter(order_type="Maid Request")
    serializer_class = MaidRequestSerializer
    permission_classes = [IsMaidSupervisorOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user, order_type="Maid Request", status="Created")


class TechnicianRequestViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.filter(order_type="Technician Request")
    serializer_class = TechnicianRequestSerializer
    permission_classes = [IsMaidSupervisorOrReadOnly, IsGuestOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(
            created_by=user, order_type="Technician Request", status="Created"
        )


class AmenityRequestViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = AmenityRequestSerializer
    permission_classes = [IsGuestOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user, order_type="Amenity Request", status="Created")
