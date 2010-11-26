#!/usr/bin/env python
# vim:set fileencoding=utf-8 sw=4 ts=8 et:vim
# Author:  Marko Mahnič
# Created: mar 2010 

import csv

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

from cms.models import CMSPlugin

TMP = getattr(settings, "CMSPLUGIN_CSVTABLE_WRAPPER_STYLES", (
   ('ta-plain', 'Normal'),
   ('ta-left', 'Align left'),
   ('ta-right', 'Align right'),
   ('ta-center', 'Centered'),
))
CMSPLUGIN_CSVTABLE_WRAPPER_STYLES = tuple( (item[0], _(item[1])) for item in TMP)

TMP = getattr(settings, "CMSPLUGIN_CSVTABLE_TABLE_STYLES", (
   ('ts-default', 'Default'),
))
CMSPLUGIN_CSVTABLE_TABLE_STYLES = tuple( (item[0], _(item[1])) for item in TMP)

CMSPLUGIN_CSVTABLE_TABLE_WIDTHS = (
    (0, _('Auto')), (20, '20%'), (30, '30%'), (40, '40%'), (50, '50%'),
    (60, '60%'), (70, '70%'), (80, '80%'), (90, '90%'), (100, '100%')
)

class CsvCell:
    def __init__(self, content, row, order):
        self.content = content
        self.row = row
        self.odrer = order

class CsvRow:
    def __init__(self, number, columns):
        self.odd = number % 2 != 0
        self.cells = [CsvCell(c, self, ic) for ic,c in enumerate(columns)]

# Derived from CMSPlugin => doesn't exist outside of a page
class CsvTablePlugin(CMSPlugin):
    caption = models.CharField(_('Caption'), max_length=200, blank=True)
    headrows = models.IntegerField(_('Header rows'), default=1)
    #columns = models.CharField(_('Column layout'), max_length=200, blank=True
    #    help_text=_(
    #        'Describe the column width and alignment in a comma separated list.\n' +
    #        'Value: 5>,3,10<  means: '
    #        'column 1 is 5 units wide and right aligned, ' +
    #        'column 2 is 3 units wide and centered, ' +
    #        'column 3 is 10 units wide and left aligned.'
    #        ))
    csv_data = models.TextField(_('CSV Data'))
    width = models.IntegerField(_('Table width'), choices=CMSPLUGIN_CSVTABLE_TABLE_WIDTHS, default=40)
    table_css = models.CharField(_('Table style'), choices=CMSPLUGIN_CSVTABLE_TABLE_STYLES, max_length=20, blank=True)
    wrapper_css = models.CharField(_('Table placement'), choices=CMSPLUGIN_CSVTABLE_WRAPPER_STYLES, max_length=20, blank=True)

    def __unicode__(self):
        return u'%s' % (self.caption)

    # TODO: cache rows?
    def getRows(self):
        rows = []
        # XXX: Assume data is in unicode!
        csvRows = csv.reader(self.csv_data.encode("utf8").split("\n"))
        for ir,row in enumerate(csvRows):
            rows.append(CsvRow(ir, [c.decode("utf8") for c in row]))

        return rows

