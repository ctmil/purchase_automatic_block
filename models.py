from odoo import tools, models, fields, api, _
from odoo.exceptions import ValidationError
import base64
from datetime import date,datetime
import csv
import json
from odoo.tools.safe_eval import safe_eval

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        self.button_done()
        return res
