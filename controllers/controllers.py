# -*- coding: utf-8 -*-
from odoo import http

# class CapstoneQueue(http.Controller):
#     @http.route('/capstone_queue/capstone_queue/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/capstone_queue/capstone_queue/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('capstone_queue.listing', {
#             'root': '/capstone_queue/capstone_queue',
#             'objects': http.request.env['capstone_queue.capstone_queue'].search([]),
#         })

#     @http.route('/capstone_queue/capstone_queue/objects/<model("capstone_queue.capstone_queue"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('capstone_queue.object', {
#             'object': obj
#         })