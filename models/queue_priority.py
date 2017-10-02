from odoo import models, fields, api

class QueuePriority(models.Model):
	_name = 'queue.priority'
	_description = 'Queue Priority'

	name = fields.Char()
	code = fields.Char()
	priority_sequence = fields.Integer(string='Priority Sequence')