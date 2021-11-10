
from odoo import _, models, fields, api

class Dormitory(models.Model):
    _name = "dormitory"

    name_all=fields.Many2many("res.partner", string="Sinh viên cùng phòng")
    name=fields.Many2one("res.partner" ,string="Sinh viên đại điện", required=True)
    sdt=fields.Char("Điện thoại đại diện")
    msv=fields.Char("Mã sinh viên đại điện" )
    address=fields.Char("Địa chỉ sinh viên đại diện" )
    name_phong=fields.Many2one("product.template","Tên phòng" , required=True)
    code_phong=fields.Char("Mã phòng" , required=True)
    khu = fields.Char("Khu")
    so_giuong=fields.Integer("Số giường" , default=8)
    so_dien=fields.Integer("Số ban đầu")
    gia_dien=fields.Integer("Giá/KW")
    so_nuoc=fields.Integer("Số nước")
    gia_nuoc=fields.Integer("Giá/khối")
    ngay_gui=fields.Date("Ngày gửi")
    so_the=fields.Char("Sô thẻ xe")
    bien_so=fields.Char("Biển số")
    chu_xe=fields.Char("Tên đăng ký xe")
    loai_xe=fields.Char("Loại xe")
    phi_gui=fields.Integer("Phí gửi xe/tháng")
    dieu_hoa=fields.Boolean("Điều hòa")
    nong_lanh=fields.Boolean("Nóng lạnh")
    ngay_vao=fields.Date("Ngày vào")

    @api.onchange('name')
    def set_value(self):
        self.sdt = self.name.phone
        self.msv=self.name.msv
        self.address=self.name.street

    @api.onchange('name_phong')
    def set_value_room(self):
        self.code_phong = self.name_phong.default_code
        self.khu = self.name_phong.khu
