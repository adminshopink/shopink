# -*- coding: utf-8 -*-
from odoo import models, fields, api

class L10nVeIslrConcept(models.Model):
    _name = 'l10n_ve.islr.concept'
    _description = 'Conceptos de Retención de ISLR Venezuela'

    name = fields.Char(string='Concepto/Actividad', required=True)
    code = fields.Char(string='Código de Actividad', help='Código oficial del SENIAT')
    withholding_percentage = fields.Float(string='% Retención', digits=(5, 2))
    subtracting_ut = fields.Float(string='Sustraendo en UT', default=0.0)
    person_type = fields.Selection([
        ('pn_r', 'Persona Natural Residente'),
        ('pn_nr', 'Persona Natural No Residente'),
        ('pj_d', 'Persona Jurídica Domiciliada'),
        ('pj_nd', 'Persona Jurídica No Domiciliada')
    ], string='Tipo de Persona', required=True)


class AccountMove(models.Model):
    _inherit = 'account.move'

    # IVA Recibido (Clientes)
    l10n_ve_iva_holding_number = fields.Char(string='Núm. Comprobante IVA Cliente', copy=False)
    l10n_ve_iva_holding_date = fields.Date(string='Fecha Comprobante IVA Cliente', copy=False)
    l10n_ve_iva_amount_retained = fields.Monetary(string='Monto IVA Retenido', currency_field='company_currency_id', copy=False)

    # ISLR Emitido/Recibido (Resumen)
    l10n_ve_islr_withholding_number = fields.Char(string='Núm. Comprobante ISLR', copy=False, readonly=True)
    l10n_ve_islr_amount_retained = fields.Monetary(
        string='Monto ISLR Retenido',
        currency_field='company_currency_id',
        compute='_compute_l10n_ve_islr_amounts',
        store=True
    )

    @api.depends('invoice_line_ids.l10n_ve_islr_concept_id', 'amount_untaxed')
    def _compute_l10n_ve_islr_amounts(self):
        for move in self:
            total_retained = 0.0
            if move.move_type == 'in_invoice':
                for line in move.invoice_line_ids:
                    concept = line.l10n_ve_islr_concept_id
                    if concept:
                        line_retained = line.price_subtotal * (concept.withholding_percentage / 100.0)
                        total_retained += line_retained
            move.l10n_ve_islr_amount_retained = total_retained


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    l10n_ve_islr_concept_id = fields.Many2one('l10n_ve.islr.concept', string='Concepto ISLR')
