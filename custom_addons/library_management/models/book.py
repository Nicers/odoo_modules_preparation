from odoo import models, fields

class BookLibrary(models.Model):
    _name = 'book.library'
    _description = 'Book library'

    title = fields.Char(string='Title', required=True)