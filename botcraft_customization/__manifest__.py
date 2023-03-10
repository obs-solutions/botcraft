# -*- coding: utf-8 -*-
{
    'name': 'BotCraft Subscription PriceList',
    'version': '16.0.0.2',
    'summary': 'BotCraft Subscription PriceList',
    'sequence': 0,
    'description': """
    Used to set PriceList with subscription inside Sale order
    """,
    'author': "Reliution",
    'website': "https://www.reliution.com",
    'depends': [
        'base',
        'sale_temporal',
        'hr_maintenance'
    ],
    'data': [
        'views/equipment_view.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
