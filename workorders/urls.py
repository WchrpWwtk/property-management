from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"cleaning-work-orders", views.CleaningWorkOrderViewSet)
router.register(r"maid-requests", views.MaidRequestViewSet)
router.register(r"technician-request", views.TechnicianRequestViewSet)
router.register(r"amenity-requests", views.AmenityRequestViewSet)

urlpatterns = [path("", include(router.urls))]
