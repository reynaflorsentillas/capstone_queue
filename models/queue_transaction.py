from odoo import models, fields, api

class QueueTransaction(models.Model):
	_name = 'queue.transaction'

	name = fields.Char()
	priority = fields.Many2one('queue.priority', string='Priority')
	office_id = fields.Many2one('queue.office', string='Office')
	op_number = fields.Char(string='Order of Payment')
	queue_number = fields.Integer(string='Queue Number')
	current_station = fields.Char()