# -*- coding: utf-8 -*-
{
    'name': 'Shopink - Control de Pago Comercial en Ventas',
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'summary': 'Reportes y estados de pago comerciales en Órdenes de Venta independientes del flujo fiscal.',
    'author': 'Shopink',
    'depends': ['sale', 'account', 'shopink_l10n_ve_invoice_control'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
