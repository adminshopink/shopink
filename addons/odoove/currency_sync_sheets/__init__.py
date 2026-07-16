# -*- coding: utf-8 -*-
from odoo import SUPERUSER_ID
from . import models

def post_init_hook(env):
    """
    Este método se ejecuta inmediatamente al instalar el módulo,
    ANTES de que otros procesos fiscales dependientes corran.
    Configura el país, activa VES como moneda base y prepara USD.
    """
    # En Odoo 19, 'env' ya viene directo en los argumentos del hook.

    # 1. Forzar la instalación y activación del idioma Español de Venezuela
    lang_code = 'es_VE'
    lang_ids = env['res.lang'].with_context(active_test=False).search([('code', '=', lang_code)])

    if lang_ids:
        lang_ids.toggle_active()
        env['base.language.install'].create({'lang_codes': [lang_code]}).lang_install()

    # 2. Buscar país (Venezuela) y Monedas (VES y USD)
    main_company = env['res.company'].browse(1)
    venezuela = env['res.country'].search([('code', '=', 'VE')], limit=1)
    ves_currency = env['res.currency'].search([('name', '=', 'VES')], limit=1)
    usd_currency = env['res.currency'].search([('name', '=', 'USD')], limit=1)

    # 3. Activar la moneda USD en el sistema (necesaria para el histórico de tasas)
    if usd_currency and not usd_currency.active:
        usd_currency.write({'active': True})

    # 4. Asegurar que VES esté activa y setearla como la moneda base de la compañía
    if ves_currency:
        if not ves_currency.active:
            ves_currency.write({'active': True})

        # Cambiamos el país y la moneda principal de la empresa antes de la localización contable
        company_vals = {'currency_id': ves_currency.id}
        if venezuela:
            company_vals.update({'country_id': venezuela.id})

        main_company.write(company_vals)

    # 5. Configurar el idioma del usuario Administrador a es_VE
    admin_user = env['res.users'].browse(SUPERUSER_ID)
    admin_user.write({'lang': lang_code})
