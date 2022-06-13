from odoo import api, fields, models


class pekerja(models.Model):
    _name = 'restoran.pekerja'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    jabatan = fields.Char(string='Jabatan')
    status = fields.Boolean(string='Menikah')
    

    
