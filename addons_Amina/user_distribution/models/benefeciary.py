from odoo import fields, models


class benefecary(models.Model):
    _name = 'sanabel.beneficiary'

    name = fields.Char(string="Name")
    nb_of_child = fields.Integer(string="Nb of Children")
    phone = fields.Char(string="Phone")
    nationality = fields.Selection([('syrian', 'Syrian'),
                                    ('lebanese', 'Lebanese'),
                                    ], string="Nationality")
    region = fields.Many2one(comodel_name='sanabel.region', string="Region", required=True)
