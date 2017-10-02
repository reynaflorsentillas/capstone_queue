from odoo import models, fields, api

class QueueOffice(models.Model):
	_name = 'queue.office.category'

	name = fields.Char()
	code = fields.Char()

class QueueOffice(models.Model):
	_name = 'queue.office'
	_description = 'Queue Officce'

	name = fields.Char()
	category_id = fields.Many2one('queue.office.category', string='Category')