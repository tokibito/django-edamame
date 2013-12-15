def to_method(view, **base_kwargs):
    """Convert view function to instance method
    """
    def _view(self, request, *args, **kwargs):
        _kwargs = base_kwargs.copy()
        _kwargs.update(kwargs)
        return view(request, *args, **_kwargs)
    return _view
