# -*- coding: utf-8 -*-

{
    'name': 'Journal Sequence',
    'version': '19.0.0.0',
    'category': 'Accounting',
    'summary': 'Assign distinct and independent numbering sequences to each journal.',
    'description': """
    Provides independent, configurable numbering sequences for journal entries across different Odoo journals""",
    'sequence': '1',
    'author': 'Apagen Solutions Pvt Ltd',
    'company': 'Apagen Solutions Pvt Ltd',
    'maintainer': 'Apagen Solutions Pvt Ltd',
    'website': 'https://www.apagen.com/',
    'depends': ['account'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/account_journal.xml',
        'views/account_move.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
