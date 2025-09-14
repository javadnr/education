from odoo import models, fields


class BooklandBook(models.Model):

    # Metadate
    _name = "bookland.book"
    _description = "Book"

    # Fields
    name = fields.Char(
        string="Book Title",
        help="Store the title of the book",
        required=True,
        index=True,
        size=512,


    )
    description = fields.Char()
