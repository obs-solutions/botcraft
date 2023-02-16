# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    # ==========================
    # Field Declaration
    # ==========================

    print_position = fields.Boolean(string="Print Position", default=True)
    position_increment = fields.Integer(default=1, string="Position Increment By")
    partner_shipping_id = fields.Many2one('res.partner')
    partner_invoice_id = fields.Many2one('res.partner')
    display_folding_marks = fields.Boolean(string='Display Folding Marks')
    logo_configuration = fields.Selection([('left', 'Left'), ('right', 'Right'), ('center', 'Center')], default="left")

    _sql_constraints = [('check_position_increment', 'CHECK(position_increment > 0)',
                         'Position Increment is required and must be greater than 0.')]
