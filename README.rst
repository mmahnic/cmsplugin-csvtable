
Django CMS plugin for creating simple tables using CSV
======================================================

Installation
------------

Add the plugin to the installed applications::

    INSTALLED_APPS = (
        # ...
        'cmsplugin_csvtable',
        # ...

        # migrations
        'south',
    )


Configuration
-------------

* CMSPLUGIN_CSVTABLE_WRAPPER_STYLES

    A tuple with the styles for the table wrapper. Used mostly for alignment.
    The default is::

        CMSPLUGIN_CSVTABLE_WRAPPER_STYLES = (
           ('ta-plain', _('Normal')),
           ('ta-left', _('Align left')),
           ('ta-right', _('Align right')),
           ('ta-center', _('Centered')),
           )

* CMSPLUGIN_CSVTABLE_TABLE_STYLES

    A tuple with the styles for the table. This defines the look of the table.
    The default is::

        CMSPLUGIN_CSVTABLE_TABLE_STYLES = (
           ('ts-default', _('Default')),
           ('ts-empty', _('Empty')),
           ('ts-plain', _('Plain')),
           )

* CMSPLUGIN_CSVTABLE_TABLE_WIDTHS

    A tuple with predefined widths for the table. Value 0 means Auto-Size,
    other values widths in percent of the containing element. The default is::

        CMSPLUGIN_CSVTABLE_TABLE_WIDTHS = (
            (0, _('Auto')), (20, '20%'), (30, '30%'), (40, '40%'), (50, '50%'),
            (60, '60%'), (70, '70%'), (80, '80%'), (90, '90%'), (100, '100%')
            )

CSS styles
----------

The default styles are defined in media/cmsplugin_csvtable/csvtable.scss.

