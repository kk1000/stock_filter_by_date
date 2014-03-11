# -*- coding: utf-8 -*-

from openerp.osv import orm, fields
from datetime import datetime as DT
from dateutil.relativedelta import  relativedelta

def _filter_by_date(model, cr, uid, obj, name, args, context=None):
    """
    The fields name must begin with 'filter_by_', so the real fields is name[10:]
    """
    if not args:
        return []
    utc_datetime_from = args[0][2]
    utc_datetime_to = (DT.strptime(utc_datetime_from, '%Y-%m-%d %H:%M:%S') + \
                       relativedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
    ids = model.search(
        cr, uid, [(name[10:], '<', utc_datetime_to),
                  (name[10:], '>=', utc_datetime_from)])
    if not ids:
        return [('id', '=', 0)]
    return [('id', 'in', ids)]

class stock_move(orm.Model):
    _inherit = 'stock.move'
    _columns = {
        'filter_by_date': fields.function(
            lambda *a, **k: {}, fnct_search=_filter_by_date,
            type="datetime", string='Date'),
        'filter_by_create_date': fields.function(
            lambda *a, **k: {}, fnct_search=_filter_by_date,
            type="datetime", string='Creation Date'),
        'filter_by_date_expected': fields.function(
            lambda *a, **k: {}, fnct_search=_filter_by_date,
            type="datetime", string='Schedule Date'),
    }

class stock_picking(orm.Model):
    _inherit = 'stock.picking'
    _columns = {
        'filter_by_min_date': fields.function(
            lambda *a, **k: {}, fnct_search=_filter_by_date,
            type="datetime", string='Scheduled Date'),
        'filter_by_create_date': fields.function(
            lambda *a, **k: {}, fnct_search=_filter_by_date,
            type="datetime", string='Creation Date'),
    }

class stock_picking_in(orm.Model):
    _inherit = 'stock.picking.in'
    _columns = {
        'filter_by_min_date': fields.function(
            lambda *a, **k: {}, fnct_search=_filter_by_date,
            type="datetime", string='Scheduled Time'),
        'filter_by_create_date': fields.function(
            lambda *a, **k: {}, fnct_search=_filter_by_date,
            type="datetime", string='Creation Date'),
    }

class stock_picking_out(orm.Model):
    _inherit = 'stock.picking.out'
    _columns = {
        'filter_by_min_date': fields.function(
            lambda *a, **k: {}, fnct_search=_filter_by_date,
            type="datetime", string='Scheduled Time'),
        'filter_by_create_date': fields.function(
            lambda *a, **k: {}, fnct_search=_filter_by_date,
            type="datetime", string='Creation Date'),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
