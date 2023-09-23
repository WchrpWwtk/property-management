from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(
    r"cleaning-work-orders",
    views.CleaningWorkOrderViewSet,
    basename="cleaning-work-orders",
)
router.register(r"maid-requests", views.MaidRequestViewSet, basename="maid-requests")
router.register(
    r"technician-requests",
    views.TechnicianRequestViewSet,
    basename="technician-requests",
)
router.register(
    r"amenity-requests", views.AmenityRequestViewSet, basename="amenity-requests"
)

urlpatterns = [path("", include(router.urls))]
