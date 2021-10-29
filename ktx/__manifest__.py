# -*- coding: utf-8 -*-
{
    'name': 'Quản lý ký túc xá',
    'version': '1.0',
    'author': '',
    'maintainer': '',
    'website': '',

    'description': """ """,
    'depends': ['base',"mail" ,"portal", "product","sale","hr"],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        "views/student_view.xml",
        "views/dormitory.xml",
        "views/room.xml"

    ],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
