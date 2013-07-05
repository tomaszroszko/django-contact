from django.conf import settings


#move messages that was already readed to archive after
# how many hours by default is set for 2 hours
MESSAGE_ARCHIVE_HOURS = getattr(settings, 'MESSAGE_ARCHIVE_HOURS', 2)