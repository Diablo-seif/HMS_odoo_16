from odoo import api, fields, models
class Department (models.Model):
    _name = 'department.department'
    _description = 'department.department'
    _rec_name= "name"

    name = fields.Char(string="name", required=True, )
    capacity = fields.Integer(string="Capacity",default=2 )
    is_opened = fields.Boolean(string="Is opened",default=True)
    patient_ids = fields.One2many(comodel_name="patient.patient", inverse_name="department_id", string="Patient", required=False)


