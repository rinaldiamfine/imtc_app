# -*- coding: utf-8 -*-
{
    'name': "IMTC",

    'summary': 'Training Management System',

    'description': """
        
    """,

    'author': "Rinaldi",
    'website': "https://rinaldiamfine.herokuapp.com",
    'category': 'Administration',
    'version': '13.1.0.1',
    'installable': True,
    'license': 'LGPL-3',

    'depends': [
        'base',
        'crm',
        'sale_crm',
        'sale',
        'purchase',
        'account',
        'l10n_id',
        'website'
    ],
    'data': [
        'views/student_view.xml',
        'views/menuitem_view.xml',
        "security/ir.model.access.csv"
    ],
}
