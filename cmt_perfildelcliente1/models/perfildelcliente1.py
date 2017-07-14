from odoo import api, fields, models


class perfildelcliente1(models.Model):
	_inherit = 'res.partner'
	x_cmt_perfildelcliente1 = fields.Char(string="Perfil del cliente 1", compute='_get_perfildelcliente1')

	@api.one
	@api.depends('x_cmt_cargo',
		 'x_cmt_medioseentero',
		 'x_cmt_tienepaginaweb')
	def _get_perfildelcliente1(self):
	    for record in self:
    		record['x_cmt_perfildelcliente'] = self.x_cmt_cargo + self.x_cmt_medioseentero