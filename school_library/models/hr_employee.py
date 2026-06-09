# -*- coding: utf-8 -*-
from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    employee_type = fields.Selection(selection_add=[
        ('teacher', 'Teacher'),
        ('librarian', 'Librarian'),
    ], ondelete={'teacher': 'set default', 'librarian': 'set default'})
    
    specialization_ids = fields.Many2many(
        'school.specialization', 
        'hr_employee_specialization_rel', 
        'employee_id', 
        'specialization_id', 
        string='Specializations'
    )
