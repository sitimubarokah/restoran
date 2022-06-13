from odoo import api, fields, models 


class pesan (models.Model):
    _name = 'restoran.pesan'
    _description = 'new description'

    pelayan = fields.Many2one(comodel_name='restoran.pekerja', string='Pelayan')
    
    name = fields.Many2one(comodel_name='restoran.pelanggan', string='Pembeli')
    no_meja = fields.Integer (string='Nomor Meja')
    tanggal = fields.Datetime(string='Tanggal Pesan',default=fields.Datetime.now)
    dtlpesanan = fields.One2many(comodel_name='restoran.makanan', inverse_name='dtlpesanan_ids', string='Pesanan')
    
    
    total_harga = fields.Integer(compute='_compute_total_harga',string='Total Harga')

    @api.model
    def _compute_total_harga(self):
        for record in self:
            total=sum(self.env['restoran.makanan'].search([('dtlpesanan_ids','=',record.id)]).mapped('harga'))
            record.total_harga=total

