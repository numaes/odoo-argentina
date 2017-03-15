# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __odoo__.py file in module root
# directory
##############################################################################
from odoo import fields, models


class SaleConfiguration(models.TransientModel):
    _inherit = 'sale.config.settings'

    group_multiple_id_numbers = fields.Boolean(
        "Allow Multiple Id Numbers on Partners",
        help="If you allow multiple Id Numbers, then a new tab for 'Id "
        "NUmbers' will be added on partner form view",
        implied_group='l10n_ar_partner.group_multiple_id_numbers',
    )
