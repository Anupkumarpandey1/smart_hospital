from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Information'

    name = fields.Char(required=True)
    specialization = fields.Char()
    experience = fields.Integer()
    available = fields.Boolean(default=True)
