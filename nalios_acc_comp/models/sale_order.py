from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_purchase_order_line_data(self, so_line, date_order, company):
        res = super(SaleOrder, self)._prepare_sale_order_line_data(so_line, date_order, company)
        res.update({"inter_company_analytic_distribution": so_line.analytic_distribution,})
        return res
