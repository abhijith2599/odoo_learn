# -*- coding: utf-8 -*-
from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Book Title', required=True)
    author = fields.Char(string='Author')
    isbn = fields.Char(string='ISBN')
    description = fields.Text(string='Description')
