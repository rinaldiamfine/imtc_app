# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    id_number = fields.Char(string="Identity No.")
    product_id = fields.Many2one('product.product', string="Training Program")