{
    "name": "Persons",
    "version": "1.0",
    "depends": ["website"],
    "description": """
    Module for persons processing
    """,
    # data files always loaded at installation
    "data": ["security/ir.model.access.csv", "views/persons_views.xml"],
    # data files containing optionally loaded demonstration data
    "demo": [],
    "application": True,
}
