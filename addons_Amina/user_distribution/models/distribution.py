from odoo import fields, models, api
from odoo.exceptions import ValidationError


class distribution(models.Model):
    _name = 'sanabel.distribution'
    type = fields.Selection([
        ('kind', 'Kind'),
        ('cash', 'Cash')], string="Type", default="cash")
    benf_type = fields.Selection([('benf_new', 'New'), ('benf_old', 'Old')], string="Beneficiary Type",
                                 default='benf_new')
    state = fields.Selection(string="Change Stations", selection=[('waiting', 'Waiting'), ('delivered', 'Delivered'),
                                                                  ('canceled', 'Canceled'), ('rejected', 'Rejected'), ],
                             default='waiting')

    benef_id = fields.Many2one(comodel_name='sanabel.beneficiary', string="Old Benefeciary")
    name = fields.Char(string="New Benefeciary")
    # product = fields.Many2one(comodel_name='sanabel.product', string='Products')
    product_ids = fields.Many2many(comodel_name='sanabel.product', string='Products')
    qte = fields.Float(string="Qte", default=1)
    amount = fields.Float(string="Amount", default=None)
    dateTime = fields.Datetime(string='Time')
    distributor = fields.Many2one(comodel_name='sanabel.distributer', string="Distributor")
    phone = fields.Char(string="Phone", compute='_compute_phone', store=True)

    def button_waiting(self):
        if self.state:
            self.state = "waiting"

    def button_delivered(self):
        if self.state:
            self.state = "delivered"

    def button_canceled(self):
        if self.state:
            self.state = "canceled"

    def button_rejected(self):
        if self.state:
            self.state = "rejected"

    @api.depends('benf_type', 'benef_id.phone')
    def _compute_phone(self):
        for record in self:
            if record.benf_type == 'benf_new':
                record.phone = self.phone
            else:
                record.phone = record.benef_id.phone

    @api.onchange('product_ids')
    def _onchange_qte(self):
        self.qte = len(self.product_ids) * 2

    # @api.depends('benf_type')
    # def _compute_benf_type(self):
    #     for i in self:
    #         if i.benf_type == 'benf_new':
    #             i.phone = self.phone
    #         else:
    #             i.phone = i.benef_id.phone

    # @api.onchange('benf_type')
    # def _onchange_phone(self):
    #     if self.benf_type == 'benf_new':
    #         self.phone = ""
    #     else:
    #         self.phone = self.benef_id.phone

    # @api.onchange('benef_id')
    # def _onchange_phone(self):
    #     if self.benef_id:
    #         self.phone = self.benef_id.phone

    @api.ondelete(at_uninstall=False)
    def _ondelete_function(self):
        for record in self:
            if record.state == "delivered":
                raise ValidationError("can't delete it.")

    @api.model
    def create(self, vals):
        distribution_records = self.env['sanabel.distribution'].search([])
        for record in distribution_records:
            if (record.benef_id == vals['benef_id'] or record.name == vals['name']) and record.state == "waiting":
                raise ValidationError("You already have a waiting list!")

        return super().create(vals)

    # @api.model
    # def write(self, vals):
    #     if self.state in ['rejected', 'delivered']:
    #         raise ValidationError("You can not Edit it because it is not pending")
    #         return False
    #
    #     return super().write(vals)

    ################################## lch chta8let bala @api.model !!!!!!!!!!!!!!!!!!!!
    def write(self, values):
        if self.state in ['delivered', 'rejected']:
            raise ValidationError("You can not Edit on this because it is not pending")

        return super().write(values)
