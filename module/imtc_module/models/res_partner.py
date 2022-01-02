# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    id_number = fields.Char(string="Identity No.")
    student_id = fields.Many2one('student.student', string="Student")
    # product_id = fields.Many2one('product.product', string="Training Program")

    @api.model
    def create(self, values):
        student_obj = self.env['student.student']
        crm_obj = self.env['crm.lead']
        context = self._context
        id_number = ""
        student_id = False
        if not values.get('id_number'):
            if context.get('active_model') == 'crm.lead':
                active_id = context.get('active_id')
                crm_id = crm_obj.browse(active_id)
                id_number = crm_id.id_number if crm_id else ""
        else:
            id_number = values['id_number']
        if id_number != "":
            student_values = {
                'name': values['name'],
                'id_number': id_number
            }
            student_id = student_obj.create(student_values)
        values['student_id'] = student_id.id if student_id else False
        res = super(ResPartner, self).create(values)
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