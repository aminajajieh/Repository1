from odoo import fields,models,api
from odoo.exceptions import ValidationError


class Distribution(models.Model):
    _inherit = 'sanabel.distribution'

    distributor=fields.Many2one(comodel_name='sanabel.distributer', string="Distributor")
    employee_id=fields.Many2one(comodel_name='sanabel.employee',string="Employee",domain="[('type_work', '=','destributor')]")

    @api.model
    def create(self, vals):
        distribution_records = self.env['sanabel.distribution'].search([
            ('name', '=', vals['name']),
            ('benef_id', '=', vals['benef_id']),
            ('dateTime', '=', vals['dateTime']),
        ])
        if distribution_records:
            raise ValidationError("You already have a distribution on this date!")
        return super(Distribution, self).create(vals)

