# -*- coding: utf-8 -*-

{
    'name': 'Stock picking / move filter by date',
    'version': '1.0',
    'category': 'Stock',
    'sequence': 14,
    'description': """
Stock move filter by **date** , **schudule date** , **createion date** ,
Stock picking filter by **schudule date**, **createion date**

库存调拨：按 **日期** , **计划日期**, **创建日期** 筛选,
收发货单：按 **计划日期**, **创建日期** 筛选
    """,
    'author': 'Shine-IT<contact@openerp.cn>',
    'website': 'http://www.openerp.cn',
    'depends': ['stock'],
    'data': ['stock_view.xml'],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
