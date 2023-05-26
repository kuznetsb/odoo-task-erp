from odoo import http


class PersonsWebsite(http.Controller):
    @http.route("/persons", website=True, auth="public")
    def get_five_last_persons(self, **kwargs):
        persons = http.request.env["website.persons"].search(
            [], limit=5, order="create_date desc"
        )
        return http.request.render("persons.persons_page", {"persons": persons})
