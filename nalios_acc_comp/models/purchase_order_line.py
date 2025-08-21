from odoo import fields, models

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    inter_company_analytic_distribution = fields.Json()