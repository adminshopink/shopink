# -*- coding: utf-8 -*-
from odoo import models, fields, api, TransientModel # <-- Importa TransientModel aquí

class AccountMoveConfirmationWizard(TransientModel):
    _name = 'account.move.confirmation.wizard'
    _description = 'Asistente de Confirmacion de Factura '

    move_id = fields.Many2one('account.move', string='Factura', required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.partner', related='move_id.partner_id', string='Cliente')
    amount_total = fields.Float(related='move_id.amount_total', string='Monto Total')

    def action_force_post(self):
        self.ensure_one()
        # Se ejecuta action_post pasando el contexto que salta este mismo wizard
        return self.move_id.with_context(skip_confirmation_wizard=True).action_post()
