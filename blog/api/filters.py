from django_filters import rest_framework as filters

from blog.models import Post

class PostFilterSet(filters.FilterSet):
    published_from = filters.DateFilter(
        field_name="published_at", lookup_expr="gte", label="Published Date From"
    )
    published_to = filters.DateFilter(
        field_name="published_at", lookup_expr="lte", label="Published Date To"
    )
    author_email = filters.CharFilter(
        field_name="author__email",
        lookup_expr="icontains",
        label="Author Email Contains",
    )
    summary = filters.CharFilter(
        field_name="summary",
        lookup_expr="icontains",
        label="Summary Contains",
    )
    content = filters.CharFilter(
        field_name="content",
        lookup_expr="icontains",
        label="Content Contains",
    )

    class Meta:
        model = Post
        fields = ["author", "tags"]


# References
# https://github.com/carltongibson/django-filter/blob/main/django_filters/rest_framework/backends.py
# https://github.com/carltongibson/django-filter/blob/main/django_filters/rest_framework/filterset.py
# https://github.com/encode/django-rest-framework/blob/master/rest_framework/filters.py
# https://github.com/carltongibson/django-filter/blob/c816887f4e3b43def5008a0181e93c153fec0fbf/django_filters/filters.py#L281
# https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html