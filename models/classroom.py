from odoo import api,fields,models,_
from  datetime import  date

class ClassroomStudents(models.Model):
    _name = 'classroom.students'
    _description = 'Classroom Students'

    name=fields.Char(string="Name")
    date_of_birth=fields.Date(string="Date of Birth")
    age=fields.Integer(string="Age")
    street=fields.Char(string="Street")
    street2=fields.Char(string="Street 2")
    city=fields.Char(string="City")
    state_id=fields.Many2one('res.country.state',string="State")
    zip=fields.Char(string="Zip")
    country_id=fields.Many2one('res.country',string="Country")
    mark_list_ids=fields.One2many('mark.list','classroom_id',string="Mark List")
    total_marks = fields.Float(string="Total Marks", compute=('_compute_fulltotal_marks'))

    @api.depends('mark_list_ids')
    def _compute_fulltotal_marks(self):
        for rec in self:
            rec.total_marks = sum(rec.mark_list_ids.mapped('total'))

    @api.onchange('date_of_birth')
    def _onchange_dob(self):
        today=date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age= today.year - rec.date_of_birth.year
            else:
                rec.age=0

    def action_pdf_report(self):
        return self.env.ref('classroom.report_classroom_students_pdf').report_action(self)

    def action_xlsx_report(self):
        return self.env.ref('classroom.report_classroom_students_xlsx').report_action(self)




class MarkList(models.Model):
    _name = "mark.list"
    _description = "Mark List"

    exam_name=fields.Char(string="Exam Name")
    subject1=fields.Float(string="Subject 1")
    subject2 = fields.Float(string="Subject 2")
    subject3 = fields.Float(string="Subject 3")
    subject4 = fields.Float(string="Subject 4")
    total=fields.Float(string="Total" ,compute=('_compute_total_mark'))
    average=fields.Float(string="Average", compute=('_compute_average_mark'))
    classroom_id=fields.Many2one('classroom.students',string="ClassRooms")


    @api.depends('subject1','subject2','subject3','subject4')
    def _compute_total_mark(self):
        for rec in self:
            rec.total=rec.subject1+rec.subject2+rec.subject3+rec.subject4

    @api.depends('total')
    def _compute_average_mark(self):
        for rec in self:
            rec.average=(rec.subject1+rec.subject2+rec.subject3+rec.subject4)/4

