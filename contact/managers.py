from datetime import timedelta
from django.db import models
from django.db.models import Q
from django.utils.timezone import now

from .settings import MESSAGE_ARCHIVE_HOURS


class MaxReadedDatetimeMixIn(object):
    """
        Mixin helper class for Contact and Archive manager
    """

    @property
    def max_readed_datetime(self):
        """
            return border datetime ... news older then this date should go
            to archive
        """
        return now() - timedelta(hours=MESSAGE_ARCHIVE_HOURS)


class ContactMessageManager(models.Manager, MaxReadedDatetimeMixIn):
    """
        Show only messages that are not readed yet... and even if they
        readed time of they read is no more then MESSAGE_ARCHIVE_HOURS hours
    """

    def get_query_set(self):
        return super(ContactMessageManager, self).get_query_set().filter(
            Q(date_readed__isnull=True) |
            Q(date_readed__gt=self.max_readed_datetime)
        )


class ArchiveMessageManager(models.Manager, MaxReadedDatetimeMixIn):
    """
        Show only message that are readed and older then read date -
        MESSAGE_ARCHIVE_HOURS
    """

    def get_query_set(self):
        return super(ArchiveMessageManager, self).get_query_set().filter(
            Q(date_readed__isnull=False) &
            Q(date_readed__lte=self.max_readed_datetime)
        )