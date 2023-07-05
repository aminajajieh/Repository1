from odoo import fields,models,api

class TypeWork(models.Model):
    _name = 'sanabel.work'

    name=fields.Char(string="Work")