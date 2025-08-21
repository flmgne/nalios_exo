from odoo import fields, models

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    inter_company_analytic_distribution = fields.Json()