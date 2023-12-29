# -*- coding: utf-8 -*-
# CrossPy Co. Osvaldo Cruz, Author.

from odoo.addons.website_hr_recruitment.controllers import main as websitehrrecruitment
from odoo.http import request


class WebsiteHrRecruitment(websitehrrecruitment.WebsiteHrRecruitment):

    def jobs_apply(self, job, **kwargs):
        error = {}
        default = {}
        states = []
        env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        states = env['res.country.state'].search([('country_id', '=', 31)])

        if 'website_hr_recruitment_error' in request.session:
            error = request.session.pop('website_hr_recruitment_error')
            default = request.session.pop('website_hr_recruitment_default')

        return request.render("website_hr_recruitment.apply", {
            'job': job,
            'error': error,
            'states': states,
            'default': default,
        })

