
from odoo import _, models, fields, api

class Room(models.Model):
    _name = "room"

    code=fields.Char("Mã phòng", required=True)
    name = fields.Char("Tên phòng", required=True)
    so_giuong = fields.Integer("Số giường")
    gia=fields.Integer("Đơn giá")
