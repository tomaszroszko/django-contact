from django.contrib import admin
from django.template.defaultfilters import truncatewords
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _now

from .models import ArchiveMessage, ContactMessage


class BaseMessageAdmin(admin.ModelAdmin):
    """
        Basic admin for contact and archive
    """

    list_display = ('from_name', 'from_email', 'subject', 'message_admin',
                    'country', 'date_received', 'date_readed', 'answer_link')
    list_display_links = ('from_name', 'from_email', 'subject')
    readonly_fields = ('from_name', 'from_email', 'subject', 'message',
                       'country', 'date_received', 'date_readed')
    search_fields = ('from_name', 'from_email', 'message')
    fieldsets = (
        (_('From'), {
            'fields': (('from_name', 'from_email'),)
        }),
        (_('Message'), {
            'fields': ('subject', 'message',)
        }),
        (_('Dates'), {
            'fields': (('date_received', 'date_readed'),)
        })
    )

    def get_actions(self, request):
        return {}

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def message_admin(self, obj):
        """
            return trucated message
        """
        return truncatewords(obj.mesasge, 5)
    message_admin.short_description = _('Message')

    def answer_link(self, obj):
        """
            return answer link using mailto
        """
        return u'<a class="grp-button" href="mailto:%s?subject=RE: %s">%s</a>' % (
            obj.from_email, obj.title, _now('answer')
        )
    answer_link.allow_tags = True
    answer_link.short_description = _('Answer')


class ContactMessageAdmin(BaseMessageAdmin):

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """
            when user read the message in bo... set a read date
        """
        obj = self.get_object(request, object_id)
        obj.date_readed = now()
        obj.save()
        return super(ContactMessageAdmin, self).change_view(
            request, object_id, form_url, extra_context)


class ArchiveMessageAdmin(BaseMessageAdmin):
    pass


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(ArchiveMessage, ArchiveMessageAdmin)
