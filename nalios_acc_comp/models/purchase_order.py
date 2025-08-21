from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def _prepare_sale_order_line_data(self, line, company):
        res = super(PurchaseOrder, self)._prepare_sale_order_line_data(line, company)
        res.update({"inter_company_analytic_distribution": line.analytic_distribution,})
        return res
