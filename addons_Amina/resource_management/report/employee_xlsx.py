from odoo import models


class EmployeeXlsx(models.AbstractModel):
    _name = 'report.resource_management.report_employee_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        print("lines",lines)
        format1=workbook.add_format({'font_size':14,'align':'vcenter','bold':True})
        format2=workbook.add_format({'font_size':10,'align':'vcenter', })
        sheet=workbook.add_worksheet('Patient Card')

        sheet.write(0,0,'Name',format1)
        sheet.write(0,1,lines.name,format2)

        sheet.write(1,0,'Last Name',format1)
        sheet.write(1, 1, lines.last_name, format2)

        sheet.write(2, 0, 'Age', format1)
        sheet.write(2, 1, lines.age, format2)

        sheet.write(3, 0, 'Currency', format1)
        sheet.write(3, 1, lines.currency_id.name, format2)

        sheet.write(4, 0, 'Salary', format1)
        sheet.write(4, 1, lines.salary, format2)

        sheet.write(0, 3, 'Type of Work', format1)
        sheet.write(0, 4, lines.type_work, format2)

        sheet.write(1, 3, 'Address', format1)
        sheet.write(1, 4, lines.address, format2)

        sheet.write(2, 3, 'Region', format1)
        sheet.write(2, 4, lines.region.name, format2)

        sheet.write(3, 3, 'Nationality', format1)
        sheet.write(3, 4, lines.nationality, format2)

        sheet.write(4, 3, 'Manager', format1)
        sheet.write(4, 4, lines.manager.name, format2)

        # Données du tableau
        distributions = lines.mapped('distribution')

        # Write table headers
        headers = ['New Benefeciary', 'Old Benefeciary', 'Products', 'Amount', 'Time', 'Status']
        for col, header in enumerate(headers):
            sheet.write(7, col, header, format1)

        # Write table data
        for row, dist in enumerate(distributions, start=8):
            sheet.write(row, 0, dist.name)
            sheet.write(row, 1, dist.benef_id.name)
            sheet.write(row, 2, dist.product_ids.name)
            sheet.write(row, 3, dist.amount)
            sheet.write(row, 4, dist.dateTime)
            sheet.write(row, 5, dist.state)