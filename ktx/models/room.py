
from odoo import _, models, fields, api

class Room(models.Model):
    _inherit = 'product.template'
    khu=fields.Char('Khu')
    so_giuong=fields.Integer('Số giường',default=8)
    giuong_trong=fields.Integer("Giường trống")


