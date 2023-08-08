from odoo import fields,models

class ClassRoomXlsx(models.AbstractModel):
    _name = 'report.classroom.classroom_report_details_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, students):
        format1=workbook.add_format({'bold':True,'bg_color':'gray'})
        bold = workbook.add_format({'bold': True})
        format2=workbook.add_format({'align':'right'})
        row=0
        col=0

        for obj in students:
            sheet = workbook.add_worksheet('Book'[:31])
            student_name = obj.name
            student_dob=obj.date_of_birth
            if student_dob:
                str_dob=student_dob.strftime('%d/%m/%Y')
            student_street=obj.street
            student_street2 = obj.street2
            student_city = obj.city
            student_state = obj.state_id.name
            student_zip = obj.zip
            student_country = obj.country_id.name
            student_age = obj.age
            student_full_total=obj.total_marks


            # One sheet by partner

            sheet.set_column('A:B',20)
            sheet.set_column('C:D', 15)
            sheet.set_column('E:E', 20)
            sheet.set_column('F:F', 16)
            sheet.write(row, col,'Name' , bold)
            if student_name:
                sheet.write(row,col + 1, student_name)
            sheet.write(row, col + 4, 'Date of Birth',bold)
            if student_dob:
                sheet.write(row, col + 5, str_dob,format2)
            sheet.write(row + 1, col, 'Address', bold)
            if student_state:
                sheet.write(row + 1, col + 1, student_street)
            if student_street2:
                sheet.write(row + 2, col + 1, student_street2)
            if student_city:
                sheet.write(row + 3, col + 1, student_city)
            if student_state:
                sheet.write(row + 3, col + 2, student_state)
            if student_zip:
                sheet.write(row + 3, col + 3, student_zip,format2)
            if student_country:
                sheet.write(row + 4, col + 1, student_country)
            sheet.write(row + 1, col + 4, 'Age', bold)
            if student_age:
                sheet.write(row + 1, col + 5, student_age,format2)
            sheet.write(row + 6, col, 'MarkList',bold)
            sheet.write(row + 7, col, 'Exam Name', format1)
            sheet.write(row + 7, col +1, 'Subject 1',format1)
            sheet.write(row + 7, col + 2, 'Subject 2',format1)
            sheet.write(row + 7, col + 3, 'Subject 3',format1)
            sheet.write(row + 7, col + 4, 'Subject 4',format1)
            sheet.write(row + 7, col + 5, 'Total',format1)
            sheet.write(row + 7, col + 6, 'Average',format1)


        for std in students.mark_list_ids:
            row+=1
            sheet.write(row + 7, col, std.exam_name)
            sheet.write(row + 7, col + 1, std.subject1)
            sheet.write(row + 7, col + 2, std.subject2)
            sheet.write(row + 7, col + 3, std.subject3)
            sheet.write(row + 7, col + 4, std.subject4)
            sheet.write(row + 7, col + 5, std.total,format2)
            sheet.write(row + 7, col + 6, std.average,format2)
            row=row
        if student_full_total:
            sheet.write(row + 8, col + 5, "Total Marks : ",bold)
            sheet.write(row + 8, col + 6,student_full_total,bold)

