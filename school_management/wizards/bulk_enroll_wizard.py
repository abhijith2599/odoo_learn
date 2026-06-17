# -*- coding: utf-8 -*-
from odoo import models, fields, api

class BulkEnrollWizard(models.TransientModel):
    _name = 'school.bulk.enroll.wizard'
    _description = 'Bulk Enroll Wizard'

    class_id = fields.Many2one('school.class', string='Class', required=True)

    def action_enroll(self):
        # The active_ids in context contain the selected students
        active_ids = self.env.context.get('active_ids', [])
        students = self.env['school.student'].browse(active_ids)
        for student in students:
            # We will change their state to enrolled and assign the class
            student.write({
                'class_id': self.class_id.id,
                'state': 'enrolled'
            })
