# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    position_number = fields.Integer(readonly=True, compute="_compute_position")

    @api.depends('order_id')
    def _compute_position(self):
        for order in self.mapped('order_id'):
            order_line_number = 1
            for line in order.order_line:
                if line.display_type in ['line_section', 'line_note']:
                    line.position_number = order_line_number
                    continue
                line.position_number = order_line_number
                order_line_number += 1
