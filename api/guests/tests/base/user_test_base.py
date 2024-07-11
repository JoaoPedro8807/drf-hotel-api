from django.test import TestCase
from ..mixins.user_mixins import UserAtuhModelMixin, UserAPIMixin
from django.urls import reverse
from rest_framework import test


class UserAuthModelBaseTest(TestCase, UserAtuhModelMixin):
    def setUp(self) -> None:
        self.user_model = self.make_user_model()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()



class UserAPIBaseTest(test.APITestCase, UserAPIMixin):
    def setUp(self) -> None:
        self.urls = {
            'login': reverse('guests:login'),
            'create': reverse('guests:user_create')
        }
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()