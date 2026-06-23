# -*- coding: utf-8 -*-
{
    'name': "school_management",
    'version':  '18.0.1.0.0',
    'summary':  'Complete school ERP — Students, Fees, Exams, Library',
    'author':   'PearlSoft Technologies LLP',
    'description': """
                Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'data/config_data.xml',
        'data/cron.xml',
        'data/mail_template.xml',
        'reports/student_id_card_report.xml',
        'views/school_class_views.xml',
        'views/school_student_views.xml',
        'wizards/bulk_enroll_wizard_views.xml',
        'views/school_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'application':False
}
