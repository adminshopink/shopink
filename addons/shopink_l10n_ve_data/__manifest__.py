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
        'data/account.account.csv',
        'data/account.tax.group.csv',
        'data/account.tax.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
