# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    position_number = fields.Char(readonly=True, compute="_compute_position")

    @api.depends('picking_id')
    def _compute_position(self):
        for order in self.mapped('picking_id'):
            number = 1
            for line in order.move_ids_without_package:
                line.position_number = number
                number += 1
