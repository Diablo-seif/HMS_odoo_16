from odoo import api, fields, models
class Doctor (models.Model):
    _name = 'doctors.doctors'
    _description = 'doctors.doctors'
    _rec_name= "name"

    name = fields.Char(string="First name", required=True,default="dr." )
    l_name = fields.Char(string="Last name", required=True,default=" " )
    img = fields.Binary(string="Image")
    patient_ids = fields.Many2many(comodel_name="patient.patient",string="Patient" )




