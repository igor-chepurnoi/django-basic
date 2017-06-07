from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from project.apps.cms.enums import Status


class Article(models.Model):
    title = models.CharField(
        _('title'), max_length=255)

    content = models.TextField(_('content'))

    slug = models.SlugField(
        _('slug'), max_length=255,
        help_text=_("Used to build the entry's URL."))

    meta_title = models.CharField(
        _('meta title'), max_length=255)

    meta_description = models.TextField(
        _('meta description'), max_length=255, null=True, blank=True)

    meta_keywords = models.TextField(
        _('meta keywords'), max_length=255, null=True, blank=True)

    status = models.IntegerField(
        _('status'), db_index=True,
        choices=((x.value, x.name.title()) for x in Status), default=Status.ACTIVE)

    creation_date = models.DateTimeField(
        _('creation date'), default=timezone.now, editable=False)
