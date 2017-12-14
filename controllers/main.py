# -*- coding: utf-8 -*-
import base64

from odoo import SUPERUSER_ID
from odoo import http, _
from odoo.tools.translate import _
from odoo.http import request

from odoo.addons.website.models.website import slug

import logging
_logger = logging.getLogger(__name__)



class capstonequeue(http.Controller):
    @http.route('/queue', type='http', auth="public", website=True)
    def queue(self, **kw):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
        priorities = http.request.env['queue.priority'].sudo()
        priorities = priorities.search([])


        office = request.params['office']

        values = {
            'priorities': priorities,
            'office': office
        }

        return request.render("capstone_queue.queue", values)




    @http.route('/confirmation', type='http', auth="public", website=True)
    def confirmation(self, **kw):

        #Get Last In Queue Number
        prioritymonitoring = http.request.env['queue.prioritymonitoring'].sudo()

        priority_id = request.params['priority']
        office_id = request.params['office']
        payment_order = request.params['payment_order']
        name = request.params['name']

        last_in_queue = 0

        prioritymonitoring = prioritymonitoring.search([['priority.id','=',priority_id],['office_id.id','=',office_id]])

        priority_desc = ''

        for priom in prioritymonitoring:
            last_in_queue = (priom.last_in_queue)


        priority = http.request.env['queue.priority'].sudo()
        priority = priority.search([['id','=',priority_id]])

        for prio in priority:
            priority_desc = prio.name


        office_id = request.params['office']

        offices = http.request.env['queue.office'].sudo()
        offices = offices.search([['id','=',office_id]])
        office_desc = ''

        for office in offices:
            office_desc = office.name


        currently_serving = '-'

        active_transactions = http.request.env['queue.transaction'].sudo()

        active_transactions = active_transactions.search([['office_id.id','=',office_id],['priority.id','=',priority_id],['current_station','!=','none']])

        for trans in active_transactions:
            currently_serving = trans.queue_number


        values = {
            'last_in_queue':last_in_queue,
            'currently_serving': currently_serving,
            'priority_desc': priority_desc,
            'office': office_desc,
            'office_id': office_id,
            'priority_id': priority_id,
            'name': name,
            'payment_order': payment_order
        }



        return request.render("capstone_queue.confirmation", values)





    @http.route('/offices', type='http', auth="public", website=True)
    def offices(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page

        offices = http.request.env['queue.office'].sudo()
        offices = offices.search([])

        values = {
            'offices': offices
        }

        return request.render("capstone_queue.offices", values)





    @http.route('/dequeue', type='http', auth="public", website=True)
    def dequeue(self, **kw):

        priority = http.request.env['queue.priority'].sudo()

        priority = priority.search([])


        offices = http.request.env['queue.office'].sudo()

        offices = offices.search([])

        values = {
            'priorities': priority,
            'offices': offices
        }

        return request.render("capstone_queue.dequeue", values)



    @http.route('/monitoring', type='http', auth="public", website=True)
    def monitoring(self, **kw):

        active_transactions = http.request.env['queue.transaction'].sudo()

        active_transactions = active_transactions.search([['current_station','!=','none']])


        values = {
            'active_transactions': active_transactions
        }

        return request.render("capstone_queue.monitoring", values)




    @http.route('/servicing', type='http', auth="public", website=True)
    def servicing(self, **kw):

        if not request.uid:
            request.uid = 1

        #Get Last In Queue Number
        prioritymonitoring = http.request.env['queue.prioritymonitoring'].sudo()

        priority_id = request.params['priority']
        office_id = request.params['office']
        current_station = request.params['station']

        last_served = 0
        done_serving = request.params['last_served']

        if done_serving != 0:
            que_transaction = http.request.env['queue.transaction'].sudo()
            que_transaction = que_transaction.search([['queue_number','=',done_serving],['priority.id','=',priority_id],['office_id.id','=',office_id]])
            que_transaction.write({
                'current_station': 'none'
            })

        prioritymonitoring = prioritymonitoring.search([['priority.id','=',priority_id],['office_id.id','=',office_id]])

        priority_desc = ''

        search_result = 0

        for priom in prioritymonitoring:
            last_served = (priom.last_served + 1)

            que_transaction = http.request.env['queue.transaction'].sudo()
            que_transaction = que_transaction.search([['queue_number','=',last_served],['priority.id','=',priority_id],['office_id.id','=',office_id]])

            for qtrans in que_transaction:
                search_result = search_result + 1


            if search_result > 0:
                que_transaction1 = http.request.env['queue.transaction'].sudo()
                que_transaction1 = que_transaction1.search([['current_station','=',current_station],['priority.id','=',priority_id],['office_id.id','=',office_id]])

                que_transaction1.write({
                    'current_station': 'none'
                })

                que_transaction.write({
                    'current_station': request.params['station']
                })


        priority = http.request.env['queue.priority'].sudo()
        priority = priority.search([['id','=',priority_id]])

        for prio in priority:
            priority_desc = prio.name

        if search_result > 0:
            prioritymonitoring.write({
                'last_served': last_served
            })


        offices = http.request.env['queue.office'].sudo()
        offices = offices.search([['id','=',office_id]])
        office_desc = ''

        for office in offices:
            office_desc = office.name



        values = {
            'priority': request.params['priority'],
            'office': request.params['office'],
            'station': request.params['station'],
            'priority_desc': priority_desc,
            'office_desc': office_desc,
            'last_served': last_served,
            'remark': ''
        }

        if search_result == 0:
            values = {
                'priority': request.params['priority'],
                'office': request.params['office'],
                'station': request.params['station'],
                'priority_desc': '',
                'office_desc': '',
                'last_served': '',
                'remark': 'Queue Cleared'
            }

        return request.render("capstone_queue.servicing", values)




    @http.route('/add_transaction', type='http', auth="public", website=True)
    def add_transaction(self, **kw):
        #Super ID which is ADMIN 1
        if not request.uid:
            request.uid = 1

        #Get Last In Queue Number
        prioritymonitoring = http.request.env['queue.prioritymonitoring'].sudo()

        priority_id = request.params['priority']
        office_id = request.params['office']

        last_in_queue = 0

        prioritymonitoring = prioritymonitoring.search([['priority.id','=',priority_id],['office_id.id','=',office_id]])

        priority_desc = ''

        for priom in prioritymonitoring:
            last_in_queue = (priom.last_in_queue + 1)


        priority = http.request.env['queue.priority'].sudo()
        priority = priority.search([['id','=',priority_id]])

        for prio in priority:
            priority_desc = prio.name


        #How to Call a Model in a Controller
        transactions = http.request.env['queue.transaction'].sudo()

        result = transactions.create({
            'name' : request.params['name'],
            'priority': request.params['priority'],
            'office_id': request.params['office'],
            'op_number': request.params['payment_order'],
            'queue_number': last_in_queue,
            'current_station': 'none'
        })

        prioritymonitoring.write({
            'last_in_queue': last_in_queue
        })

        office_id = request.params['office']

        offices = http.request.env['queue.office'].sudo()
        offices = offices.search([['id','=',office_id]])
        office_desc = ''
        office_location = ''

        for office in offices:
            office_desc = office.name
            office_location = office.location


        values = {
            'result': result,
            'last_in_queue':last_in_queue,
            'priority_desc': priority_desc,
            'office': office_desc,
            'office_location': office_location
        }



        return request.render("capstone_queue.print_number", values)