from odoo import fields, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    inter_company_analytic_distribution = fields.Json()