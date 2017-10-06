from odoo import models, fields, api

class QueuePriority(models.Model):
	_name = 'queue.priority'
	_description = 'Queue Priority'

	name = fields.Char()
	code = fields.Char()
	priority_sequence = fields.Integer(string='Priority Sequence')
	last_served = fields.Integer(string='Last Number Served')
	last_in_queue = fields.Integer(string='Last Number in Queue')



class QueuePriorityMonitoring(models.Model):
	_name = 'queue.prioritymonitoring'
	_description = 'Queue Priority Monitoring'

	name = fields.Char()
	priority = fields.Many2one('queue.priority', string='Priority')
	office_id = fields.Many2one('queue.office', string='Office')
	last_served = fields.Integer(string='Last Number Served')
	last_in_queue = fields.Integer(string='Last Number in Queue')