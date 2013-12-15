from unittest import TestCase


class ModelViewsTest(TestCase):
    def getOne(self):
        from edamame import generic
        return generic.ModelViews()

    def test(self):
        views = self.getOne()
