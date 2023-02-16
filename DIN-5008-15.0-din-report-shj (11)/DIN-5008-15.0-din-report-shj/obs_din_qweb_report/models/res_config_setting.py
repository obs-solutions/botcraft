# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    # ==========================
    # Field Declaration
    # ==========================

    position_increment = fields.Integer(
        related="company_id.position_increment",
        string="Default Quotation Validity (Days)",
        readonly=False,
    )
    print_position = fields.Boolean(
        "Print Position",
        related="company_id.print_position",
        config_parameter="print_position",
        readonly=False,
    )
    position_line_number = fields.Boolean(string='Display Position Number',
                                          config_parameter="obs_din_qweb_report.position_line_number")

    def delivery_address(self):
        return self.env.user.has_group('sale.group_delivery_invoice_address')

    # ==========================
    # Method Declaration
    # ==========================

    @api.onchange('position_line_number')
    def get_position_line_number(self):
        if self.position_line_number:
            self.print_position = True
        else:
            self.print_position = False
