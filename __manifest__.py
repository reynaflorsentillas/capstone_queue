# -*- coding: utf-8 -*-
{
    'name': "Capstone Queue",

    'summary': """
        Queueing System""",

    'description': """
        Queueing System
    """,

    'author': "Capstone Solutions Inc.",
    'website': "http://www.capstone.ph",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/queue_office_data.xml',
        'data/queue_priority_data.xml',
        'views/queue_office_view.xml',
        'views/website_templates.xml',
        'views/queue_priority_view.xml',
        'views/queue_priority_monitoring.xml',
        'views/queue_transaction_view.xml',
        'views/queue_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}