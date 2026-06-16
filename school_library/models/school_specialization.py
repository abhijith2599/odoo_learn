# -*- coding: utf-8 -*-
from odoo import models, fields

class SchoolSpecialization(models.Model):
    _name = 'school.specialization'
    _description = 'School Specialization'

    name = fields.Char(string='Specialization Name', required=True)
