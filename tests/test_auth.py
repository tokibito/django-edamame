from unittest import TestCase


class AuthViewsTest(TestCase):
    def getOne(self):
        """return test target
        """
        from django.conf import settings
        settings.configure()
        from edamame import auth
        return auth.AuthenticateViews()

    def test_urls_pattern(self):
        views = self.getOne()
        urls = views.urls
        resolver_login = urls[0][0]
        self.assertEqual(resolver_login.regex.pattern, r'^login/$')
        resolver_logout = urls[0][1]
        self.assertEqual(resolver_logout.regex.pattern, r'^logout/$')
