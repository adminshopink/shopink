# -*- coding: utf-8 -*-
{
    'name': 'Shopink - Localización Venezolana (Retenciones IVA e ISLR)',
    'version': '19.0.1.0.0',
    'summary': 'Gestión de retenciones de IVA recibidas e ISLR mediante diarios contables.',
    'category': 'Accounting/Localizations',
    'author': 'Shopink',
    'depends': ['account', 'web_studio', 'shopink_l10n_ve_partner'],
    'data': [
        # Seguridad (si aplica ir.model.access.csv para el wizard)
        'wizard/account_move_confirmation_views.xml', # <-- Primero el Wizard
        'views/l10n_ve_islr_concept_views.xml',
        'views/account_move_views.xml',               # <-- Después la herencia de la factura
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
