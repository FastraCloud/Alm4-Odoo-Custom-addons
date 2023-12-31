# -*- coding: utf-8 -*-
{
    'name': "ALM Multi-Location Store",

    'summary': """
        A multi location store """,

    'description': """
        Available for companies with multiple stock warehouse
    """,

    'author': "BigFix Technology",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','purchase','analytic'],

    # always loaded
    'data': [
	'security/rules.xml',
	'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
	'data/internal_request_sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'auto_install': False,
}
