# -*- coding: utf-8 -*-
from odoo import SUPERUSER_ID
from . import models

def post_init_hook(env):
    """
    Este método se ejecuta inmediatamente al instalar el módulo,
    ANTES de que otros procesos fiscales dependientes corran.
    Configura el país, activa VES como moneda base y prepara USD.
    """

    # 1. Forzar la instalación y activación del idioma Español de Venezuela
    lang_code = 'es_VE'
    
    # Buscamos si el idioma existe en el sistema
    lang_ids = env['res.lang'].with_context(active_test=False).search([('code', '=', lang_code)])

    if lang_ids:
        # Lo activamos si estaba inactivo
        if not lang_ids.active:
            lang_ids.toggle_active()
    else:
        # Si no existe en el registro base, lo creamos y activamos
        lang_ids = env['res.lang'].create({
            'code': lang_code,
            'name': 'Spanish (VE) / Español (VE)',
            'direction': 'ltr',
            'date_format': '%d/%m/%Y',
            'time_format': '%H:%M:%S',
            'grouping': '[3, 3, 0]',
            'decimal_point': ',',
            'thousands_sep': '.',
            'active': True,
        })

    # Odoo 19: Forzar la carga de los archivos de traducción (.po) del core para es_VE
    env['res.lang']._load_backend_translations(lang_code)

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
