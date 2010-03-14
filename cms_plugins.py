#!/usr/bin/env python
# vim:set fileencoding=utf-8 sw=4 ts=8 et:vim
# Author:  Marko Mahnič
# Created: mar 2010 

from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_csvtable.models import CsvTablePlugin

class CMSCsvTablePlugin(CMSPluginBase):
    model = CsvTablePlugin
    name = _('CSV Table')
    render_template = 'plugins/cmsplugin_csvtable/default.html'
    change_form_template = 'admin/plugins/cmsplugin_csvtable/plugin_change_form.html'

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

plugin_pool.register_plugin(CMSCsvTablePlugin)
