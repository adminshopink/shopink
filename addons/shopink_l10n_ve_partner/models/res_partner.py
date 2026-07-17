# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    l10n_ve_rif = fields.Char(
        string='RIF / Cédula',
        help="Formato: V-123456789, J-12345678-9, E-123456789"
    )
    
    l10n_ve_person_type = fields.Selection([
        ('V', 'Natural Venezolano (V)'),
        ('E', 'Natural Extranjero (E)'),
        ('J', 'Jurídico Nacional (J)'),
        ('G', 'Gobierno (G)'),
        ('P', 'Pasaporte (P)'),
    ], string='Tipo de Persona', default='V')

    l10n_ve_taxpayer_type = fields.Selection([
        ('ordinary', 'Contribuyente Ordinario'),
        ('special', 'Contribuyente Especial'),
        ('exempt', 'No Sujeto / Exento'),
    ], string='Tipo de Contribuyente', default='ordinary')
