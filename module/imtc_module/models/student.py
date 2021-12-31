# -*- coding: utf-8 -*-

from odoo import models, fields

class Student(models.Model):
    _name = 'student.student'
    _description = "Student"

    id_number = fields.Integer(String="KTP")
    name = fields.Char(string='Name')
    photo = fields.Binary(string='Photo')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    is_membership = fields.Boolean(string="Is Membership", default=False)
    active = fields.Boolean(string="Is Active", default=True)
    
    student_class_ids = fields.One2many('assigned.student', 'student_id', string="Class")