from odoo import models, fields


class SalesCommissionLine(models.Model):
    _name = "sales.commission.line"
    _description = "To store sales commission line related data"

    commission_date = fields.Date(string="Date Commission", help="Date of the commission")
