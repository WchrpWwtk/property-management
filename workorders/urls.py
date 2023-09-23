from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(
    r"cleaning-work-orders",
    views.CleaningWorkOrderViewSet,
    basename="cleaningworkorders",
)
router.register(r"maid-requests", views.MaidRequestViewSet, basename="maidrequests")
router.register(
    r"technician-requests",
    views.TechnicianRequestViewSet,
    basename="technicianrequests",
)
router.register(
    r"amenity-requests", views.AmenityRequestViewSet, basename="amenityrequests"
)

urlpatterns = [path("", include(router.urls))]
