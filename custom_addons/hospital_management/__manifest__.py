{
    'name': 'Hospital Management System',
    'version': '1.0',
    'summary': 'Manage Hospital Operations',
    'author': 'Anup Kumar Pandey',
    'category': 'Healthcare',
    'depends': ['base', 'mail', 'sale', 'account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/appointment_views.xml',
        'reports/patient_report.xml'
    ],
    'installable': True,
    'application': True,
}
