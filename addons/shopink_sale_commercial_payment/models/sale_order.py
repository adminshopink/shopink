# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commercial_payment_state = fields.Selection([
        ('unpaid', 'No Pagado'),
        ('partial', 'Pago Parcial'),
        ('paid', 'Totalmente Pagado')
    ], string='Estado de Pago (Comercial)', compute='_compute_commercial_payment_state', store=True, default='unpaid')

    @api.depends('invoice_ids', 'invoice_ids.state', 'invoice_ids.amount_residual')
    def _compute_commercial_payment_state(self):
        for order in self:
            if not order.invoice_ids:
                order.commercial_payment_state = 'unpaid'
                continue

            invoices = order.invoice_ids
            if all(inv.payment_state in ('paid', 'in_payment') for inv in invoices):
                order.commercial_payment_state = 'paid'
            elif any(inv.payment_state in ('paid', 'in_payment', 'partial') for inv in invoices):
                order.commercial_payment_state = 'partial'
            else:
                order.commercial_payment_state = 'unpaid'
