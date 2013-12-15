import collections


class Views(object):
    view_decorators = []

    def __init__(self, name=None, app_name=None):
        self.name = name
        self.app_name = app_name

    def wrap_view(self, view):
        """Wrap view with decorators
        """
        decorated_view = view
        for decorator in self.view_decorators:
            if isinstance(decorator, collections.Sequence):
                decorator_function = decorator[0]
                if len(decorator) > 1:
                    args = decorator[1]
                else:
                    args = ()
                if len(decorator) > 2:
                    kwargs = decorator[2]
                else:
                    kwargs = {}
            else:
                decorator_function = decorator
                args = ()
                kwargs = {}

            decorated_view = decorator_function(view, *args, **kwargs)
        return decorated_view

    def get_urls(self):
        """Django urls
        """
        return []

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.name
