# -*- coding: utf-8 -*-

from odoo import models, fields


class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    # ==========================
    # Field Declaration
    # ==========================

    display_folding_marks = fields.Boolean(related='company_id.display_folding_marks', readonly=False,
                                           string='Display Folding Marks')
    logo_configuration = fields.Selection([('left', 'Left'), ('right', 'Right'), ('center', 'Center')],
                                          related='company_id.logo_configuration', readonly=False)
