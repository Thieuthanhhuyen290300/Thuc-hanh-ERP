from odoo import _, models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    msv = fields.Char("Mã sinh viên", required=True)
    date_in = fields.Date("Ngày nhập học")
    sdt=fields.Char("Di động")
    x_email=fields.Char("Email")
    ten_lien_he=fields.Char("Tên Bố/Mẹ")
    ngay_cmd=fields.Date("Ngày cấp")
    name=fields.Char( "Tên sinh viên",placeholder = "Tên sinh viên", required = "True")
    stk=fields.Char("Sô tài khoản ngân hàng")
    gvcn=fields.Char("Giáo viên chủ nhiệm")
