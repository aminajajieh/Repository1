from odoo import fields, models


class product(models.Model):
    _name = 'sanabel.product'

    name = fields.Char(string="Product")
    #product_id=fields.Many2one(comodel_name='sanabel.distribution')