{
    #  Information

    'name': 'OBS DIN QWeb Report Customization',
    'version': '15.1.3',
    'summary': 'OBS DIN QWeb Report Customization',
    'description': """
        OBS DIN QWeb Report Customization """,
    'category': 'Customization',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': [
        'web',
        'sale_management',
        'sale',
        'stock',
        'purchase',
        'account',
        'base_setup',
        'base',
        'l10n_de'
    ],
    'data': [
        'views/res_config_setting_view.xml',
        'views/base_document_layout.xml',
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'views/purchase_order_view.xml',
        'views/stock_picking_view.xml',
        'reports/folding_mark_layout.xml',
        'reports/report_sale.xml',
        'reports/report_purchase.xml',
        'reports/report_delivery_slip.xml',
        'reports/report_invoice.xml',
        'reports/obs_solutions_din_5008_a_template.xml',
        'reports/obs_solutions_din_5008_b_template.xml',

    ],
    'assets': {
        'web.report_assets_pdf': [
            'obs_din_qweb_report/static/src/scss/obs_din_report.scss',
        ],
    },

    # Other
    'auto_install': False,
    'application': True,
    'installable': True,
}
