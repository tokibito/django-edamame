from unittest import TestCase


class ToMethodTest(TestCase):
    def setUp(self):
        def spam_view(request):
            return 'spam result'

        self.view = spam_view

    def getOne(self):
        from edamame import utils
        return utils.to_method

    def test_success_call(self):
        to_method = self.getOne()
        method = to_method(self.view)
        self.assertEqual(method(None, None), 'spam result')
