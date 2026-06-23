# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Student Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='male')
    class_id = fields.Many2one('school.class', string='Class', required=True, ondelete='restrict')
    roll_number = fields.Char(string='Roll Number')
    date_of_birth = fields.Date(string='Date of Birth')
    email = fields.Char(string='Email')
    photo = fields.Image(string='Photo', max_width=1920, max_height=1920)
    blood_group = fields.Selection([
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ], string='Blood Group')
    guardian_phone = fields.Char(string='Guardian Phone')
    guardian_email = fields.Char(string='Guardian Email')
    fee_balance = fields.Float(string='Fee Balance')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('applied', 'Applied'),
        ('enrolled', 'Enrolled'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft', tracking=True)

    def action_apply(self):
        for record in self:
            record.state = 'applied'
            record.activity_schedule(
                'mail.mail_activity_data_todo',
                summary='Review Admission Application',
                user_id=self.env.user.id
            )

    def action_enroll(self):
        for record in self:
            record.state = 'enrolled'
            template = self.env.ref('school_management.email_template_enrollment_confirmation', raise_if_not_found=False)
            if template:
                template.send_mail(record.id, force_send=True)

    def action_reject(self):
        for record in self:
            record.state = 'rejected'

    @api.model
    def _cron_absent_notification(self):
        _logger.info("Executing Daily Absent Notification Cron")

    @api.model
    def _cron_fee_reminder(self):
        _logger.info("Executing Monthly Fee Reminder Cron")
