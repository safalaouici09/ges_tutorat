# -*- coding: utf-8 -*-
from odoo import models, fields, api
class ProjetTutorat(models.Model):
    _name = "tutorat.projet"
    _description = "Projet de tutorat "

    idProjetTutorat = fields.Char(string="IdProjetTutorat", required=True)
    descProjetTutorat = fields.Char(string="description")
      
    #commande_id  = fields.one2one('GestTutorat.commandeTutorat',
        #ondelete='cascade', string="commande de projet ", required=True)