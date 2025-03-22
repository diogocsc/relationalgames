# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                           #
#    __manifest__.py file at the root folder of this module.                   #
###############################################################################

{
    'name': 'Custom Cart Style',
    'version': '16.0.1.0.0',
    'category': 'Website',
    'summary': 'Custom styling for cart summary',
    
    # Module dependency management
    'depends': [
        'website_sale', 
    ],
    
    # Data files to be loaded
    'data': [
        'views/templates.xml',
    ],
    
    # Frontend asset management
    'assets': {
        'web.assets_frontend': [
            'website_cart_style_custom/static/src/scss/cart.scss',  # Custom cart styling
        ],
    },
    
    # Module configuration
    'installable': True,       
    'application': True,       
    'auto_install': False,    
    'license': 'LGPL-3',    
    
    # Additional metadata (recommended)
    'author': 'Test Ecom',
    'website': 'https://www.yourcompany.com',
    'description': """
        Custom Cart Styling Module
        =========================
        This module provides custom styling modifications for the e-commerce cart summary page.
        
        Features:
        ---------
        * Custom cart layout modifications
        * Enhanced visual styling through SCSS
        * Seamless integration with website_sale module
    """,
    'maintainer': 'Test Ecom',
}