# -*- coding: utf-8 -*-
from openerp import fields, models, api
import re


class res_partner(models.Model):
    _inherit = 'res.partner'

    responsability_id = fields.Many2one(
        'afip.responsability', 
        'Resposability'
    )
    # para ejemplo
    # default=lambda self: self._context.get('location_id', False)
    # para ejemplo
    document_type_id = fields.Many2one(
        'afip.document_type', 'Document type',
        default=lambda self: self._context.get('document_type_id.name', 'RUT')
        )
    document_number = fields.Char(
        'Document number', size=64,)
    iibb = fields.Char('Gross Income', size=64)
    start_date = fields.Date('Start-up Date')

    @api.onchange('document_number', 'document_type_id')
    def onchange_document(self):
        print 'Entra al onchange del VAT'
        mod_obj = self.env['ir.model.data']
        if self.document_number and ('afip.document_type', self.document_type_id.id) == mod_obj.get_object_reference('l10n_ar_invoice', 'dt_CUIT'):
            print 'entra por CUIT'
            print 'self.document_type_id.id: ' + str(self.document_type_id.id)
            document_number = re.sub('[^1234567890]', '', str(self.document_number))
            self.vat = 'AR%s' % document_number
            self.document_number = document_number
        ## agregado por Daniel Blanco
        elif self.document_number and ('afip.document_type', self.document_type_id.id) == mod_obj.get_object_reference('l10n_ar_invoice', 'dt_RUT'):
            print 'entra por RUT'
            print 'self.document_type_id.id: ' + str(self.document_type_id.id)
            print 'self.document_type_id.name: ' + str(self.document_type_id.name)
            document_number = re.sub('[^1234567890K]', '', str(self.document_number))
            self.vat = 'CL%s' % document_number
            self.document_number = document_number
        else:
            print 'no entra por ninguno'
            print 'self.document_type_id.id: ' + str(self.document_type_id.id)