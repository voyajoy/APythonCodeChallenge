from django.http import JsonResponse
from django.test import mock, RequestFactory, TestCase

from . import views


class DoubleBookTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    @mock.patch('booking.views.detect_conflicts', return_value=list())
    def test_double_book(self, mock_detect):
        c1, c2 = list(), list()
        request = self.factory.post('/book/double/', data={'c1': c1, 'c2': c2})
        resp = views.double_book(request)

        self.assertIsInstance(resp, JsonResponse)
        mock_detect.assert_called_once_with(c1, c2)

    @mock.patch('booking.views.detect_conflicts', return_value=list())
    def test_no_data(self, mock_detect):
        request = self.factory.post('/book/double/', data={})
        resp = views.double_book(request)

        self.assertIsInstance(resp, JsonResponse)
        mock_detect.assert_called_once_with(list(), list())


class DetectConflictsTestCase(TestCase):

    def test_empty(self):
        c1, c2 = list(), list()
        conflicts = views.detect_conflicts(c1, c2)
        self.assertIsInstance(conflicts, list)
        self.assertListEqual(conflicts, list())

    def test_single_overlap(self):
        e1 = {"name": "Foo", "checkIn": "2016-07-12", "checkOut": "2016-07-19"}
        e2 = {"name": "Bar", "checkIn": "2016-07-18", "checkOut": "2016-07-20"}

        conflicts = views.detect_conflicts([e1], [e2])
        self.assertIsInstance(conflicts, list)
        self.assertListEqual(conflicts[0], [e1, e2])
        self.assertEqual(1, len(conflicts))

    def test_double_overlap(self):
        e1 = {"name": "Foo", "checkIn": "2016-07-12", "checkOut": "2016-07-19"}
        e2 = {"name": "Bar", "checkIn": "2016-07-18", "checkOut": "2016-07-20"}
        e3 = {"name": "Egg", "checkIn": "2016-07-11", "checkOut": "2016-07-17"}

        conflicts = views.detect_conflicts([e1], [e2, e3])
        self.assertIsInstance(conflicts, list)
        self.assertListEqual(conflicts[0], [e1, e2])
        self.assertListEqual(conflicts[1], [e1, e3])
        self.assertEqual(2, len(conflicts))

    def test_two_disjoint_overlaps(self):
        e1 = {"name": "Foo", "checkIn": "2016-07-12", "checkOut": "2016-07-19"}
        e2 = {"name": "Bar", "checkIn": "2016-07-18", "checkOut": "2016-07-20"}
        f1 = {"name": "Egg", "checkIn": "2016-08-00", "checkOut": "2016-08-17"}
        f2 = {"name": "Meh", "checkIn": "2016-08-11", "checkOut": "2016-08-17"}

        conflicts = views.detect_conflicts([e1, f1], [e2, f2])
        self.assertIsInstance(conflicts, list)
        self.assertListEqual(conflicts[0], [e1, e2])
        self.assertListEqual(conflicts[1], [f1, f2])
        self.assertEqual(2, len(conflicts))

    def test_no_overlap(self):
        e1 = {"name": "Foo", "checkIn": "2016-07-12", "checkOut": "2016-07-19"}
        e2 = {"name": "Bar", "checkIn": "2016-07-20", "checkOut": "2016-07-23"}

        conflicts = views.detect_conflicts([e1], [e2])
        self.assertEqual(0, len(conflicts))

    def test_same_checkout_and_checkin_day(self):
        e1 = {"name": "Foo", "checkIn": "2016-07-12", "checkOut": "2016-07-19"}
        e2 = {"name": "Bar", "checkIn": "2016-07-19", "checkOut": "2016-07-23"}

        conflicts = views.detect_conflicts([e1], [e2])
        self.assertEqual(0, len(conflicts))
