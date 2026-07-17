# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    l10n_ve_customer_rif = fields.Char(
        string='RIF del Cliente',
        compute='_compute_l10n_ve_customer_fiscal_data',
        store=True,
        readonly=False
    )
    
    l10n_ve_taxpayer_type = fields.Selection([
        ('ordinary', 'Contribuyente Ordinario'),
        ('special', 'Contribuyente Especial'),
        ('exempt', 'No Sujeto / Exento'),
    ], string='Tipo de Contribuyente', compute='_compute_l10n_ve_customer_fiscal_data', store=True, readonly=False)

    @api.depends('partner_id')
    def _compute_l10n_ve_customer_fiscal_data(self):
        for order in self:
            if order.partner_id:
                order.l10n_ve_customer_rif = order.partner_id.l10n_ve_rif
                order.l10n_ve_taxpayer_type = order.partner_id.l10n_ve_taxpayer_type
            else:
                order.l10n_ve_customer_rif = False
                order.l10n_ve_taxpayer_type = False
