# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    contact_id = fields.Many2one('res.partner', string="Contact", tracking=True)
