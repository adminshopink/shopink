# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        """ Sobrescribe la validación nativa para inyectar el número de control """
        for move in self:
            # Solo aplica para facturas de clientes (out_invoice) y notas de crédito (out_refund)
            if move.move_type in ('out_invoice', 'out_refund') and not move.payment_reference:
                # Extrae el siguiente número consecutivo de la secuencia oficial
                control_num = self.env['ir.sequence'].next_by_code('l10n_ve.control.number')
                move.payment_reference = control_num
                
        return super(AccountMove, self).action_post()
