from django.db import models
from django.template.defaultfilters import truncatewords
from django.utils.translation import ugettext_lazy as _

from .managers import ContactMessageManager, ArchiveMessageManager


class ContactMessage(models.Model):
    """
        Message stored from contact form
    """

    from_name = models.CharField(_('From'), max_length=255, null=True,
                                 blank=True)
    from_email = models.EmailField(_('From email'))
    subject = models.CharField(_('Subject'), max_length=255, null=True,
                            blank=True)
    country = models.CharField(_('Country'), max_length=255, null=True,
                            blank=True)
    message = models.TextField(_('Message'))

    date_received = models.DateTimeField(_('Received'), auto_now=True)
    date_readed = models.DateTimeField(_('Readed'), null=True, blank=True)

    objects = ContactMessageManager()

    class Meta:
        verbose_name = _('Contact message')
        verbose_name_plural = _('Contact messages')

    def __unicode__(self):
        return self.title

    @property
    def title(self):
        """
            return subject or part of the message
        """
        return self.subject or truncatewords(self.message, 5)


class ArchiveMessage(ContactMessage):
    """
        All messages that was already readed
    """

    objects = ArchiveMessageManager()

    class Meta:
        proxy = True
        verbose_name = _('Archive message')
        verbose_name_plural = _('Archive messages')
