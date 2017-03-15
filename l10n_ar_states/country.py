# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __odoo__.py file in module root
# directory
##############################################################################
from odoo import fields, models


class CountryState(models.Model):
    _inherit = 'res.country.state'

    afip_code = fields.Char(
        'AFIP code',
        help='Codigo oficial del AFIP.'
    )
