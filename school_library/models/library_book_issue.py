# -*- coding: utf-8 -*-
from odoo import models, fields

class LibraryBookIssue(models.Model):
    _name = 'library.book.issue'
    _description = 'Library Book Issue'

    book_id = fields.Many2one('library.book', string='Book', required=True, ondelete='restrict')
    student_id = fields.Many2one('school.student', string='Student', required=True, ondelete='restrict')
    issue_date = fields.Date(string='Issue Date', default=fields.Date.today, required=True)
    return_date = fields.Date(string='Return Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('issued', 'Issued'),
        ('returned', 'Returned')
    ], string='Status', default='draft')
    notes = fields.Text(string='Notes')
