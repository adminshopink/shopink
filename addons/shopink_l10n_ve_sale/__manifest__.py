# -*- coding: utf-8 -*-
{
    'name': 'Shopink - Ventas Localización VE',
    'summary': 'Campos fiscales y reporte de cotización predeterminado para Venezuela.',
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'author': 'Shopink',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'shopink_l10n_ve_partner',
    ],
    'data': [
        'report/sale_report_templates.xml',  # <-- Registramos el archivo del reporte
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
