# -*- coding: utf-8 -*-
# CrossPy Co. Osvaldo Cruz, Author.

from odoo import models, fields, _
from odoo.exceptions import UserError


class Applicant(models.Model):

    _inherit = 'hr.applicant'

    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', default=lambda self: self.env.company.country_id)
    country_code = fields.Char(related='country_id.code', string="Country Code")

    def website_form_input_filter(self, request, values):
        super().website_form_input_filter(request, values)

        applicant_skill_ids = []
    
        if 'skill_ids' in request.params:
            skill_ids = [(0, 0, {'skill_type_id': 1, 'skill_id': int(x), 'skill_level_id': 1}) for x in request.params.get('skill_ids', '').split(',')]
            applicant_skill_ids.extend(skill_ids)
    
        if 'system_skill' in request.params:
            system_skill_ids = [(0, 0, {'skill_type_id': 2, 'skill_id': int(x), 'skill_level_id': 7}) for x in request.params.get('system_skill', '').split(',')]
            applicant_skill_ids.extend(system_skill_ids)
    
        values.update({'applicant_skill_ids': applicant_skill_ids})

        return values
