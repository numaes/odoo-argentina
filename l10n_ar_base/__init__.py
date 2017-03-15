# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __odoo__.py file in module root
# directory
##############################################################################
from odoo import SUPERUSER_ID, api

from odoo.addons import account
old_auto_install_l10n = account._auto_install_l10n


def ar_auto_install_l10n(cr, registry):
    """
    overwrite of this function to install our localization module
    """
  
    env = api.Environment(cr, SUPERUSER_ID, {})
    country_code = env.user.company_id.country_id.code
    if country_code and country_code == 'AR':
        module_ids = registry['ir.module.module'].search(
            cr, SUPERUSER_ID, [
                ('name', '=', 'l10n_ar_chart'),
                ('state', '=', 'uninstalled')])
        registry['ir.module.module'].button_install(
            cr, SUPERUSER_ID, module_ids, {})
    else:
        return old_auto_install_l10n(cr, registry)


account._auto_install_l10n = ar_auto_install_l10n
