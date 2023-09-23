from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import PropertyUser, WorkOrder


class CleaningWorkOrderTests(APITestCase):
    def setUp(self) -> None:
        self.supervisor_user = PropertyUser.objects.create(
            username="supervisor", password="password", user_role="Maid Supervisor"
        )
        self.guest_user = PropertyUser.objects.create(
            username="guest", password="password", user_role="Guest"
        )

        self.work_order = WorkOrder.objects.create(
            created_by=self.supervisor_user,
            assigned_to=self.supervisor_user,
            room="101",
            started_at="2023-09-22T08:00:00Z",
            finished_at="2023-09-22T10:00:00Z",
            order_type="Cleaning",
            status="Created",
        )

    def test_get_work_orders(self):
        self.client.force_login(user=self.supervisor_user)
        url = reverse("cleaningworkorders-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_work_orders(self):
        self.client.force_login(user=self.supervisor_user)
        data = {
            "created_by": self.supervisor_user.id,
            "assigned_to": self.supervisor_user.id,
            "room": "102",
            "started_at": "2023-09-23T08:00:00Z",
            "finished_at": "2023-09-23T10:00:00Z",
            "order_type": "Cleaning",
            "status": "Created",
        }
        url = reverse("cleaningworkorders-list")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_work_order(self):
        self.client.force_login(user=self.supervisor_user)

        data = {"status": "In Progress"}
        url = reverse("cleaningworkorders-detail", args=[self.work_order.id])
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.work_order.refresh_from_db()
        self.assertEqual(self.work_order.status, "In Progress")

    def test_delete_work_order(self):
        self.client.force_login(user=self.supervisor_user)
        url = reverse("cleaningworkorders-detail", args=[self.work_order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(WorkOrder.objects.filter(pk=self.work_order.id).exists())

    def test_unauthenticated_get_cleaning_work_order(self):
        url = reverse("cleaningworkorders-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_guest_user_should_no_permission_to_get_cleaning_work_order_list(self):
        self.client.force_login(user=self.guest_user)
        url = reverse("cleaningworkorders-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
