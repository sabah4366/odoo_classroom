# -*- coding: utf-8 -*-
{
    'name': "classroom",
    'summary': """ classroom management task """,
    'description': """ classroom management task""",
    'sequence':-200,
    'author': "Class",
    'website': "http://www.yourcompany.com",
    'category': '',
    'version': '0.1',
    'depends': ['base','report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/menu.xml',
        'views/classroom_view.xml',
        'report/classroom_report_template.xml',
        'report/classroom_report.xml',
    ],
    'demo': [],
    'application':True,
    'auto_install': False,
    'licence':'LGPL-3'
}
