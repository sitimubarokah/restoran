import string
from odoo import api, fields, models 


class Makanan (models.Model):
    _name = 'restoran.makanan'
    _description = 'New description'

    name = fields.Char (string = 'Nama Menu')
    deskripsi = fields.Char (string = 'Deskripsi')
    harga = fields.Integer (string = 'Harga')
    dtlpesanan_ids = fields.Many2one(comodel_name='restoran.pesan', string='Pesanan')
    
