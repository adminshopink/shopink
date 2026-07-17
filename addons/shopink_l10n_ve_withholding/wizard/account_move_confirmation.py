from odoo import models, fields, _
from odoo.exceptions import UserError

class AccountMoveConfirmationWizard(models.TransientModel):
    _name = 'account.move.confirmation.wizard'
    _description = 'Confirmación Crítica de Facturación Digital'

    move_id = fields.Many2one('account.move', string='Factura', required=True)
    partner_id = fields.Many2one('res.partner', related='move_id.partner_id', string='Cliente')
    amount_total = fields.Monetary(related='move_id.amount_total', currency_field='currency_id', string='Total')
    currency_id = fields.Many2one('res.currency', related='move_id.currency_id')

    def action_force_post(self):
        self.ensure_one()
        # Procedemos a publicar la factura de manera nativa una vez confirmado
        return self.move_id.with_context(skip_confirmation_wizard=True).action_post()
