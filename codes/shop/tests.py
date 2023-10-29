import os

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from _base.settings import BASE_DIR
from shop.models import Order, Vendor


class ObjectFactory:

    @staticmethod
    def create_vendor(data):
        return Vendor.objects.create(**data)

    @staticmethod
    def create_order(data):
        return Order.objects.create(**data)


class DelayReportViewTest(TestCase):

    def setUp(self) -> None:
        print(os.path.join(BASE_DIR, 'db.sqlite3'))
        super().setUp()
        self.url = "api/v1/shop/delay/"

    def test_successful_report_creation(self):
        order = ObjectFactory.create_order(
            {"vendor": ObjectFactory.create_vendor({"name": "test-vendor"}),
             "name": "test-order", "delivery_duration": 10})

        data = {
            'order_id': order.id,
            'name': order.name,
        }

        response = self.client.post(self.url, data=data)
        s = 1
