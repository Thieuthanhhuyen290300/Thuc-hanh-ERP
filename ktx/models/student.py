from odoo import _, models, fields, api


class HrEmployee(models.Model):
    _inherit = "res.partner"

    msv = fields.Char("Mã sinh viên", required=True)
    date_in = fields.Date("Ngày nhập học")
    ten_lien_he=fields.Char("Tên Bố/Mẹ")
    ngay_cmd=fields.Date("Ngày cấp CMND")
    stk=fields.Char("Sô tài khoản ngân hàng")
    cmnd=fields.Integer("Số CMND")
    gt = fields.Selection([
        ('one', 'Nam'),
        ('two', 'Nữ'),
        ('three', 'Khác'),], string='Giới tính')
    sinh=fields.Date("Ngày sinh")
    dia_chi=fields.Char("Địa Chỉ")
    sdt_khan=fields.Char("Số điện thoại khẩn")
