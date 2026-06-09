# -*- coding: utf-8 -*-
{
    'name': "school_library",
    'version': '18.0.1.0.0',
    'summary': "School Library management and HR extensions",
    'description': """
        Manage library books, issue requests, and extend HR Employee for academic profiles.
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'depends': ['base', 'school_management', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_book_issue_views.xml',
        'views/hr_employee_views.xml',
        'views/library_menus.xml',
    ],
    'installable': True,
    'application': True,
}
