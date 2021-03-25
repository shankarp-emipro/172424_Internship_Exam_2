{
    'name': 'Sales Commission Ept',
    'version': '1.0.1',
    'category': 'Sales/Commission',
    'summary': 'Sales commission',
    'description': """
This module contains all the sales commission related calculations.
    """,
    'depends': ['sale'],
    'data': [
        'security/sales_commission_ept_security.xml',
        'security/ir.model.access.csv',
        'views/sales_commission_ept_menus.xml'

    ],
    'installable': True,
    'auto_install': False
}
