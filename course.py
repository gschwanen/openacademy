from osv import orm, fields


class Course(orm.BaseModel):
    _name = "openacademy.course"

    _columns = {
        'name': fields.char(string="Title", size=256, required=True,),
        'description': fields.text(string="Description"),
    }
