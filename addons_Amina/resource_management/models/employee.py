from odoo import fields, models, api


class Employee(models.Model):
    _name = 'sanabel.employee'

    name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    age = fields.Integer(string="Age", required=True)

    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.ref('base.LBP').id)
    salary = fields.Monetary(string='Salary', currency_field='currency_id')

    type_work = fields.Selection([('investigator', 'Investigator'),
                                  ('field_visit', 'Field Visit'), ('it', 'IT'), ('logistic', 'Logistic'), ('destributor', 'Destributor')
                                  ], string="Type of Work")

    # type_work = fields.Many2many(comodel_name='sanabel.work', string="Type of Work")

    address = fields.Char(string="Address")
    region = fields.Many2one(comodel_name='sanabel.region', string="Region", required=True)
    nationality = fields.Selection([('syrian', 'Syrian'),
                                    ('lebanese', 'Lebanese'),
                                    ], string="Nationality")

    manager = fields.Many2one(comodel_name='sanabel.employee', string="Manager",
                              domain="[('type_work', '=', type_work)]")

    distribution = fields.One2many(comodel_name='sanabel.distribution', inverse_name='employee_id', string="Distribution")

    # filtered_distribution = fields.One2many(comodel_name='sanabel.distribution', inverse_name='dist_id',
    #                                         compute='_compute_filtered_distribution', string="Distributions")
    #
    # @api.depends('name')
    # def _compute_filtered_distribution(self):
    #     for record in self:
    #         record.filtered_distribution = self.env['sanabel.distribution'].search(
    #             [('distributor', '=', record.name)])