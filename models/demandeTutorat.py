# -*- coding: utf-8 -*-
from datetime import date
from datetime import datetime

from . import etudiant
from odoo import models, fields, api

class DemandeTutorat(models.Model):
    _name = "tutorat.demande"
    _description = "demande de tutorat"
    titre = fields.Char("Titre de demande", required=True)
    demande_no = fields.Integer(string="N° demande", default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field')
    )
   
    #nDemande = fields.Char(string="N° demande", required=True)
    desDemande = fields.Char(string="Description demande", required=True)
    date= fields.Datetime(string="Date de Creation",default=lambda self: datetime.now())
    #valide=fields.models.BooleanField()
   # idEtudiant = fields.Many2one('tutorat.etudiant',
    #    ondelete='cascade', string="Etudiant", required=True) 
    



   