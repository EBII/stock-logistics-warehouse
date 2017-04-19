# -*- encoding: utf-8 -*-
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Extended Inventory Preparation Filters",
    "version": "10.0.1.0.0",
    "depends": [
        "stock",
    ],
    "author": "OdooMRP team,"
              "AvanzOSC,"
              "Serv. Tecnol. Avanzados - Pedro M. Baeza,"
              "Odoo Community Association (OCA)",
    "contributors": [
        "Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>",
        "Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>",
    ],
    "category": "Inventory, Logistic, Storage",
    "website": "http://www.odoomrp.com",
    "summary": "More filters for inventory adjustments",
    "data": [
        "views/stock_inventory_view.xml",
        "security/ir.model.access.csv",
    ],
    'installable': True,
}
