# -*- coding: utf-8 -*-

{
    'name': 'Online Jobs Skills Inherit Filds',
    'category': 'Website/Website',
    'author': 'CrossPy Co, Osvaldo Cruz',
    'sequence': 315,
    'version': '1.0',
    'summary': 'Manage your online hiring process adding skills fields in recruitment form ',
    'description': "This module allows to asak the appliance skill in the recruitment for form",
    'depends': ['website_hr_recruitment'],
    'data': [
        'views/website_hr_recruitment_templates.xml',
        'data/config_data.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': ['website_hr_recruitment'],
    'assets': {
    },
    'license': 'Other proprietary',
}
