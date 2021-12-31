# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    id_number = fields.Char(string="Identity No.")
    student_id = fields.Many2one('student.student', string="Student")
    # product_id = fields.Many2one('product.product', string="Training Program")

    @api.model
    def create(self, values):
        res = super(ResPartner, self).create(values)
        student_obj = self.env['student.student']
        student_values = {
            'name': values['name'],
        }
        return res

    # _sql_constraints = [
    #     (
    #         "id_number_uniq",
    #         "unique(id_number)",
    #         (
    #             "A partner with the same identity number has been created before!"
    #         ),
    #     )
    # ]