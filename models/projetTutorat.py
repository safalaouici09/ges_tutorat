# -*- coding: utf-8 -*-
from odoo import models, fields, api
class ProjetTutorat(models.Model):
    _name = "tutorat.projet"
    _description = "Projet de tutorat "

    idProjet = fields.Char(string="Id Projet ", required=True)
    descProjet = fields.Char(string="Description",required=True)
    enseignant =fields.Char(string="Enseignant", required=True)
    #idDemande = fields.many2one('tutorat.demande',
    # ondelete='cascade', string="demande de tutorat", required=True)
   