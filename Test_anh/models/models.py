from odoo import models, fields, api


class Contract(models.Model):
    _name = "contact1234"
   # _inherit = ['mail.thread', 'mail.activity.mixin']

    Ten = fields.Text('ten', required="True")
    Bao_gia = fields.Many2one("sale.order")
    Thong_tin = fields.Text('thong_tin', required="True")
    name = fields.Many2one("res.partner")
    state = fields.Selection([('confirm', 'Confirmed'),
                              ('reject', 'Rejected')], default='',
                             string="Status", tracking=True)
    prescription_line_ids = fields.One2many('contact1234', 'name',
                                            string="Prescription Lines")
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'
        #    rec.message_post(body='Message 1', partner_ids=[user1.partner_id.id, user2.partner_id.id])

    def action_reject(self):
        for rec in self:
            rec.state = 'reject'

    nickname = fields.Char('Nickname')
    description = fields.Text('Pet Description')
    age = fields.Integer('Pet Age', default=1)
    weight = fields.Float('Weight (kg)')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    pet_image = fields.Binary("Pet Image", attachment=True, help="Pet Image")

    product_ids = fields.Many2many(comodel_name='product.product',
                                   string="Related Products",
                                   relation='pet_product_rel',
                                   column1='col_pet_id',
                                   column2='col_product_id')


class Task2(models.Model):
    _inherit = "sale.order"

    def my_button(self):
        return {
            'name': "Your String",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'contact1234',

            'target': 'current',
        }
    Tam = fields.One2many('contact1234', 'name', string="Ten Nguoi Duyet")
    #Ten_PA = fields.Many2one(string="Ten", related="Tam.Ten")


