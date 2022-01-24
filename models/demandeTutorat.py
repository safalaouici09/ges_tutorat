# -*- coding: utf-8 -*-
from . import etudiant
from odoo import models, fields, api
class DemandeTutorat(models.Model):
    _name = "tutorat.demande"
    _description = "demande de tutorat"
    
    nDemande = fields.Char(string="nDemande", required=True)
    desDemande = fields.Char(string="description demande ", required=True)
    #valide=fields.models.BooleanField()
    #idEtudiant = fields.Many2one('tutorat.etudiant',
        #ondelete='cascade', string="Etudiant", required=True) 