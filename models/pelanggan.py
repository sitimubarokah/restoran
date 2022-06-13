from odoo import api, fields, models 


class pelanggan (models.Model):
    _name = 'restoran.pelanggan'
    _description = 'new description'

    name = fields.Char(string='Nama')
    id_pelanggan = fields.Char(string='Id Pelanggan')
    alamat = fields.Char(string='Alamat')
    no_tlp = fields.Char(string='Nomor Telepon')
    
