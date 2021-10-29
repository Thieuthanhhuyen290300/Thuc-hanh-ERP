
from odoo import _, models, fields, api

class Dormitory(models.Model):
    _name = "dormitory"


    name_all=fields.Many2many("hr.employee", string="Sinh viên cùng phòng")
    name=fields.Many2one("hr.employee" ,string="Sinh viên đại điện", required=True)
    sdt=fields.Char("Điện thoại đại diện",related="name.mobile_phone")
    msv=fields.Char("Mã sinh viên đại điện" , required=True , related="name.msv")
    address=fields.Char("Địa chỉ sinh viên đại diện" , related="name.work_email")
    name_phong=fields.Many2one("room","Tên phòng" , required=True)
    code_phong=fields.Char("Mã phòng" , required=True)
    khu = fields.Selection([
        ('a', 'Khu A'),
        ('b', 'Khu B'),
        ('c', 'Khu C'),] , required=True , default="a", string="Khu")
    so_giuong=fields.Integer("Số giường")
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
    ten_thiet_bi=fields.Char("Tên thiết bị")
    hang = fields.Char("Hãng sản xuất")
    trang_thai = fields.Selection([
        ('a', 'Mới'),
        ('b', 'Đã qua sử dụng'),
        ('c', 'Hỏng'),], string="Tinh trạng")
    ngay_vao=fields.Date("Ngày vào")

    @api.onchange('name_phong')
    def get_value(self):
        self.code_phong = self.name_phong.code

    @api.onchange('name_phong')
    def get_so_giuong(self):
        self.so_giuong = self.name_phong.so_giuong