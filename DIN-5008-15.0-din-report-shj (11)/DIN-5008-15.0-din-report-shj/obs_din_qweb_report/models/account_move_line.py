# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    position_number = fields.Integer(
        readonly=True, compute='_compute_position_number')

    def _compute_position_number(self):
        for line in self.mapped('move_id'):
            order_line_number = 1
            for move_line in line.invoice_line_ids:
                if move_line.display_type in ['line_section', 'line_note']:
                    move_line.position_number = order_line_number
                    continue
                move_line.position_number = order_line_number
                order_line_number += 1
