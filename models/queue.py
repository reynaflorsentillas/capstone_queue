from odoo import models, fields, api

class Queue(models.Model):
	_name = 'queuq.queue'
	_description = 'Queue'

	name = fields.Char()
