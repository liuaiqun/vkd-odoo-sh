# -*- coding: utf-8 -*-
{
    'name': "Framework for Odoo EDI integration using FlexEDI",

    'summary': """
        This module serves as a base framework for EDI integration with Odoo""",

    'description': """
        This module serves as a framework for integrating EDI communication with Odoo Enterprise.

        The purpose of this module is to serve as a base implementation and contains the basic views, data models, python classes and other base code required.
    """,

    'author': "VK Data ApS",
    'website': "https://vkdata.dk",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Specific Industry Applications',
    'version': '2.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_setup', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_company_form_view.xml',
        'views/res_config_view.xml',
        'views/product_uom_form_view.xml',
        'data/odoo_edi_product_uom.xml',
        'data/odoo_edi_endpoints.xml',
        'data/odoo_edi_uom_to_product_uom.xml',
    ],

    "external_dependencies": {
        "python": ['pysftp'],
    },

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
