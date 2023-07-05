from odoo import fields, models


class distributer(models.Model):
    _name = 'sanabel.distributer'

    name = fields.Char(string="Distributor")


class region(models.Model):
    _name = 'sanabel.region'

    name = fields.Char(string="Region")
