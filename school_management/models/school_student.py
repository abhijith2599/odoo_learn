# -*- coding: utf-8 -*-
from odoo import models, fields

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Student Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='male')
    class_id = fields.Many2one('school.class', string='Class', required=True, ondelete='restrict')
    roll_number = fields.Char(string='Roll Number')
    date_of_birth = fields.Date(string='Date of Birth')
