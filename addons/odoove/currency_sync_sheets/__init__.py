# -*- coding: utf-8 -*-
from . import models
from odoo import api, SUPERUSER_ID

def post_init_hook(env):
    """
    Este método se ejecuta automáticamente justo después de instalar el módulo.
    Instala el idioma Español de Venezuela y lo setea por defecto en la compañía.
    """
    lang_code = 'es_VE'
    lang_ids = env['res.lang'].with_context(active_test=False).search([('code', '=', lang_code)])
    
    if lang_ids:
        lang_ids.toggle_active()
        env['base.language.install'].create({'lang_codes': [lang_code]}).lang_install()

    main_company = env['res.company'].browse(1)
    venezuela = env['res.country'].search([('code', '=', 'VE')], limit=1)
    
    if venezuela:
        main_company.write({
            'country_id': venezuela.id,
        })
        
    admin_user = env['res.users'].browse(SUPERUSER_ID)
    admin_user.write({'lang': lang_code})
