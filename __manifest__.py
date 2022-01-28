# -*- coding: utf-8 -*-
{
    'name': "GesTutorat",

    'summary': """Gestion des Tutorats""",

    'description': """
        Gestion  des tutorats des etudiants  :
            - Gerer les demandes de tutorat des étudiants 
            - Gerer les sessions de tutorats 
            - Creer les différents rapports du tutorats 
    """,

    'author': "LAOUICI_AITSAID",
    'website': "http://www.esi.dz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',
    'application':True,
    # any module necessary for this one to work correctly
    'depends': ['base'],
    #'application':True,

    # always loaded
    'data': [
        #'security/security.xml',
        #'security/ir.model.access.csv',
        #'templates.xml',
        'views/etudiant_view.xml',
	    #'reports.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        
    ],
}
