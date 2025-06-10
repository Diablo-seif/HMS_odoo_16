from odoo import api, fields, models
class Patient (models.Model):
    _name = 'patient.patient'
    _description = 'patient.patient'
    _rec_name= "name"

    name = fields.Char(string="patient name", required=True)
    l_name = fields.Char(string="Last name", required=True)
    age = fields.Integer(string="Age", required=False)
    birth_date = fields.Date(string="Birth date", required=False)
    history = fields.Text(string="History", required=False, default="No History")
    cr_ratio = fields.Float(string="CR Ratio")
    blood_type = fields.Selection(string="Blood type", selection=[ ('a+', 'A+') , ('ab+', 'AB+'),('a-', 'A-') , ('ab-', 'AB-'),('b+', 'B+') ,   ('o+', 'O+'),('b-', 'B-') ,   ('o-', 'O-'),   ]   )
    pcr = fields.Boolean(string="PCR")
    img = fields.Binary(string="Image")
    add = fields.Char(string="Address", required=False)
    doctor_id = fields.Many2many(comodel_name="doctors.doctors",string="Doctor")
    department_id = fields.Many2one(comodel_name="department.department", string="Department", required=False)
    state  = fields.Selection(string="State", selection=[('u', 'Undetermined') , ('g', 'Good'), ('f', 'Fair') ,   ('s', 'Serious') ])

    @api.onchange('age')
    def _on_change_pcr(self):
        if self.age is not None:
            if 0 < self.age <= 30:
                self.pcr = True
                return {
                    "warning": {
                        'title': 'PCR',
                        'message': 'PCR is set to True because age is 30 or under.',
                    }
                }
            elif self.age > 30:
                self.pcr = False
                return {
                    "warning": {
                        'title': 'PCR',
                        'message': 'PCR is set to False because age is over 30.',
                    }
                }
        self.pcr = False
        return {}

    log_history_id = fields.One2many(comodel_name="patient.history.line", inverse_name="patient_id", string="Grade")



class PatientHistoryLogin(models.Model):
    _name = 'patient.history.line'
    _description = 'patient.history.line'

    patient_id = fields.Many2one(comodel_name="patient.patient",string="patient Name",)
    date  = fields.Datetime(string="Date", required=False, )
    des  = fields.Text(string="Description", required=False, )

