# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(string='Class Name', required=True)
    teacher_id = fields.Many2one('res.users', string='Teacher')
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    student_ids = fields.One2many('school.student', 'class_id', string='Students')
    student_count = fields.Integer(string='Student Count', compute='_compute_student_count')

    @api.depends('student_ids')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.student_ids)

    def action_view_students(self):
        self.ensure_one()
        return {
            'name': 'Students',
            'type': 'ir.actions.act_window',
            'res_model': 'school.student',
            'view_mode': 'list,kanban,form',
            'domain': [('class_id', '=', self.id)],
            'context': {'default_class_id': self.id},
            'target': 'current',
        }
