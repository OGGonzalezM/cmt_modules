# -*- coding: utf-8 -*-
{
    'name': "CMT Models",

    'summary': """
        Modulo para los modelos de CMT""",

    'description': """
        Modulo para los modelos de CMT, Este es el primer modulo de pruebas
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/inherit_region.xml',
        'views/inherit_perfil_confirmado.xml',
    ], 
    'installable':True,
    'auto_install':False,
}