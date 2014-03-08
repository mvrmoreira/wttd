# coding: utf-8
from django.utils.timezone import now
from django.utils.translation import ungettext, ugettext as _
from django.contrib import admin
from eventex.subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'cpf', 'phone', 'created_at')
    list_filter = ['created_at']

    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()

    subscribed_today.short_description = _(u'Inscrito hoje?')
    subscribed_today.boolean = True
    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        # TODO: corrigir palavra inscricao
        msg = ungettext(
            u'%d inscricao foi marcada como paga.',
            u'%d inscricao foram marcadas como pagas.',
            count
        )
        self.message_user(request, msg % count)

    mark_as_paid.short_description = _('Marcar como pago')


# Register your models here.
admin.site.register(Subscription, SubscriptionAdmin)
