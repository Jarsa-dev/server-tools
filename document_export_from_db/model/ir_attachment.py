# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Julius Network Solutions SARL <contact@julius.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models


class ir_attachment(models.Model):
    _inherit = 'ir.attachment'

    def write_again(self, context=None):
        if context is None:
            context = {}
        location = self.env['ir.config_parameter'].get_param(
            'ir_attachment.location')
        if not location:
            return True
        for ia in self.browse(self.ids):
            if ia.db_datas:
                super(ir_attachment, self).write(ia.id, {
                    'datas': ia.datas,
                    'db_datas': False,
                }, context=context)
        return True
