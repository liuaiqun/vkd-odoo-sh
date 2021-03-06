# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    odoo_edi_token = fields.Char(string='Token *', help='Define the token that is used for login to FlexEDI', related="company_id.odoo_edi_token", readonly=False)
    module_odoo_edi_invoice = fields.Boolean(string='Enable EDI Invoicing (Send EDI invoices)')
    module_odoo_edi_vendorbill = fields.Boolean(string='Enable EDI Vendor Bills (Recieve EDI invoices)')
    module_odoo_edi_saleorder = fields.Boolean(string='Enable EDI Sales orders and qoutations')
    module_odoo_edi_purchase = fields.Boolean(string='Enable EDI Purchase orders')
    edi_mode = fields.Selection(string="EDI Operation mode", help="Choose how we handle EDI connections. Option 'Production' for running against a production environment and sending real documents to real customers. Option 'Test' is to send documents to the testing environment where data is processed but not actually sent. Option 'Development/Debug' is used when we do not want to contact a server, which results in the file just being dumped locally on the server", related="company_id.edi_mode", readonly=False, selection=[('production', 'Production'), ('test', 'Test'), ('development', 'Development/Debugging')])


    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()

        res.update(
            odoo_edi_token=self.odoo_edi_token,
            edi_mode=self.edi_mode
        )
        return res
