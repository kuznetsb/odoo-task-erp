import datetime
from dateutil.relativedelta import relativedelta

from odoo import fields, models, api


class Person(models.Model):
    _name = "website.persons"
    _description = "Persons table for website app"

    first_name = fields.Char(string="First name", size=255)
    last_name = fields.Char(string="Last name", size=255)
    full_name = fields.Char(string="Full name", compute="_get_full_name", default="")
    birthday = fields.Date(string="Birthday date")
    age = fields.Integer(string="Age", compute="_compute_age", default=0)
    sex = fields.Selection(
        selection=[("m", "male"), ("f", "female"), ("non", "non-binary")], string="Sex"
    )
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        default=lambda self: self.env.company,
        ondelete="set null",
    )

    @api.depends("first_name", "last_name")
    def _get_full_name(self):
        for rec in self:
            if rec.first_name and rec.last_name:
                rec.full_name = rec.first_name + " " + rec.last_name

    @api.depends("birthday")
    def _compute_age(self):
        today = datetime.date.today()
        for rec in self:
            if rec.birthday:
                rec.age = int(relativedelta(today, rec.birthday).years)
