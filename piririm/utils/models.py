import ulid

from django.db import models

from powerlibs.django.contrib.models import TimestampedModelMixin


def ulid_str_generator():
    return ulid.new().str


class SystemBaseModel(TimestampedModelMixin):
    class Meta:
        abstract = True

    id = models.CharField(max_length=26, default=ulid_str_generator,
                          primary_key=True, editable=False)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'<{clsname}: {self}>'
