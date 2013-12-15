from unittest import TestCase
from django.conf.urls import url, patterns, include


class ViewsIncludeTest(TestCase):
    """Django urls include target
    """
    def getOne(self):
        from edamame import base
        return base.Views()

    def test_include(self):
        views = self.getOne()
        result = include(views.urls)
        self.assertEqual(result, ([], None, None))


class ViewDecoratorsApplyTest(TestCase):
    """apply Views.view_decorators
    """
    def getOne(self):
        from edamame import base

        def egg_decorator(view):
            """return fixed value
            """
            def _wrap(request, *args, **kwargs):
                return 'egg result'
            return _wrap

        class TargetViews(base.Views):
            """spam view decorated with egg_decorator
            """
            view_decorators = (egg_decorator,)

            def spam(self, request):
                return 'spam result'

            def get_urls(self):
                return patterns('', url(r'^$', self.wrap_view(self.spam)))

        return TargetViews()

    def test_call(self):
        """test result of decorated view
        """
        views = self.getOne()
        urls = include(views.urls)
        resolver = urls[0][0]
        # result is egg_decorator result
        result = resolver.callback(None)
        self.assertEqual(result, 'egg result')
