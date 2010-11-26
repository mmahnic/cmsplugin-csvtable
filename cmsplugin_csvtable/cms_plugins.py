#!/usr/bin/env python
# vim:set fileencoding=utf-8 sw=4 ts=8 et:vim
# Author:  Marko Mahnič
# Created: mar 2010 

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_csvtable.models import CsvTablePlugin
from django.utils.translation import ugettext as _
from django.conf import settings

class CMSCsvTablePlugin(CMSPluginBase):
    model = CsvTablePlugin
    name = _('CSV Table')
    render_template = 'plugins/cmsplugin_csvtable/default.html'
    # change_form_template = 'admin/plugins/cmsplugin_csvtable/plugin_change_form.html'

    text_enabled = True

    def render(self, context, instance, placeholder):
        rows = instance.getRows()
        headrows = max(0, instance.headrows)
        has_width = instance.width >= 10
        context.update({
            'table': instance,
            'thead_rows': rows[:headrows],
            'tbody_rows': rows[headrows:],
            'has_width': has_width,
            'placeholder': placeholder
        })
        return context

    def icon_src(self, instance):
        return settings.MEDIA_URL + u"cmsplugin_csvtable/image/table.png"


plugin_pool.register_plugin(CMSCsvTablePlugin)
