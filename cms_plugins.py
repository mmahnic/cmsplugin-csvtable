from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_csvtable.models import CsvTablePlugin

class CMSCsvTablePlugin(CMSPluginBase):
    model = CsvTablePlugin
    name = _('CSV Table')
    render_template = 'plugins/cmsplugin_csvtable/default.html'

    def render(self, context, instance, placeholder):
        context.update({
            'table': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CMSCsvTablePlugin)
