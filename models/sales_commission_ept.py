from odoo import models, fields


class SalesCommissionEpt(models.Model):
    _name = "sales.commission.ept"
    _description = "To store sales commission related data"

    name = fields.Char(string="Commission Name", help="Commission name sequential")
