# -*- coding: utf-8 -*-
{
    'name': 'Shopink - Carga de Datos Localización VE',
    'summary': 'Mapeo automatizado de cuentas, grupos e impuestos para Shopink.',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Localizations',
    'author': 'Shopink',
    'license': 'LGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'data/account_account.csv',
        'data/account_tax_group.csv',
        'data/account_tax.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
