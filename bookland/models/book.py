from odoo import fields, models


class BooklandBook(models.Model):
    # Model Attributes
    _name = "bookland.book"
    _description = "Book"

    # Fields
    name = fields.Char(
        string="Book Title",
        help="Store the title of the book",
        translate=True,
        required=True,
        index=True,
        size=512,
    )
    description = fields.Html(
        # string="Description"
        required=False,
        translate=True,
        index=False,
    )
    publish_date = fields.Date(string="Publish")

    # time_to_market_date = {
    #     "type": "date",
    #     "name": "present_date",
    #     "note": "This is when the book is present to market"
    # }
    time_to_market_date = fields.Date(required=False)

    price = fields.Float(
        string="Book Price",
        required=False,
        digits=2,
        index=False,
        default=10.50,
        readonly=True,
        groups="base.user_group",
        help="""
<h1>Price of the Book</h1>
<p>How much the book should sell on store</p>
""",
    )
