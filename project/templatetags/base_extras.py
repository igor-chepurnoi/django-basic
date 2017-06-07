from django import template

register = template.Library()


@register.simple_tag
def active_page(request, view_name, **kwargs):
    from django.core.urlresolvers import resolve, Resolver404
    path = resolve(request.path_info)
    if not request:
        return ""
    try:
        if path.url_name == view_name and path.kwargs == kwargs:
            return "active"
        else:
            return ""
    except Resolver404:
        return ""
