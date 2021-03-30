from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampMixin(models.Model):
    created_date = models.DateTimeField(
        verbose_name=_("created date"), auto_now_add=True, editable=False
    )
    modified_date = models.DateTimeField(
        verbose_name=_("modified date"), auto_now=True, editable=False, db_index=True
    )

    class Meta:
        abstract = True


class BaseModel(TimeStampMixin):
    class Meta:
        abstract = True
