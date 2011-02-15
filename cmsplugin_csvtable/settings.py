
from django.conf import settings as django_settings
from django.utils.translation import ugettext_lazy as _

CMSPLUGIN_CSVTABLE_WRAPPER_STYLES = getattr(django_settings, "CMSPLUGIN_CSVTABLE_WRAPPER_STYLES", (
        ('ta-plain', _('Normal')),
        ('ta-left', _('Align left')),
        ('ta-right', _('Align right')),
        ('ta-center', _('Centered')),
))

CMSPLUGIN_CSVTABLE_TABLE_STYLES = getattr(django_settings, "CMSPLUGIN_CSVTABLE_TABLE_STYLES", (
        ('ts-default', _('Default')),
        ('ts-empty', _('Empty')),
        ('ts-plain', _('Plain')),
))

CMSPLUGIN_CSVTABLE_TABLE_WIDTHS = (
        (0, _('Auto')), (20, '20%'), (30, '30%'), (40, '40%'), (50, '50%'),
        (60, '60%'), (70, '70%'), (80, '80%'), (90, '90%'), (100, '100%')
)

