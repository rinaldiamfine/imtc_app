# -*- coding: utf-8 -*-

from odoo import models, fields

class StudentClass(models.Model):
    _name = 'student.class'
    _description = "Student Class"

    name = fields.Char(string="Name")
    product_id = fields.Many2one('product.product', string="Training Program")
    assigned_student_ids = fields.One2many('assigned.student', 'student_class_id', string="Students")
    session_ids = fields.One2many('student.session', 'class_id', string="Session")
    active = fields.Boolean(string="Is Active", default=True)
    
class AssignedStudent(models.Model):
    _name = 'assigned.student'
    _description = "Assigned Student"
    
    student_class_id = fields.Many2one('student.class', string="Class")
    student_id = fields.Many2one('student.student', string="Student")