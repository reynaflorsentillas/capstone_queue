from odoo import models, fields, api

class QueueTransaction(models.Model):
	_name = 'queue.transaction'

	name = fields.Char()
	is_senior = fields.Boolean(string='Senior Citizen?')
	senior_id = fields.Char(strig='Senior ID')
	office_id = fields.Many2one('queue.office', string='Office')
	op_number = fields.Char(string='Order of Payment')