import odoo
from odoo import models, fields, api

class Enseignant(models.Model):
    _name = "tutorat.enseignant"
    _description = "enseignant à l'ecole"
    idEns = fields.Char(string="id", required=True)    
    nomEns = fields.Char(string="Nom", required=True) 
    prenomEns = fields.Char(string="Prenom", required=True) 