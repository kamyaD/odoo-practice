# -*- coding: utf-8 -*-


from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.estate.property"
    _description="Estate  property details"
    
    name = fields.Char(required=True)
    property_type_id=fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    user_id = fields.Many2one("res.users", string="User")
    tags_id = fields.Many2many("estate.property.tag")
    offer_id= fields.One2many("estate.property.offer", "price", string="price")
    description = fields.Char()
    postcode = fields.Char()
    date_available= fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection = [('north', 'North'), ('east', 'East'), ('west', 'West')]
    )
    active = fields.Boolean('Active', default=True)
    state = fields.Selection(string='State', copy= False, default= 'new',  selection= [('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')])

class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description ="Estate property description"

    name=fields.Char(required=True)

class PropertyTag(models.Model):
    _name="estate.property.tag"
    _description=""

    name=fields.Char(required=True)

class PropertyOffer(models.Model):
    _name="estate.property.offer"
    _description=""

    price=fields.Float()
    status=fields.Selection(string="Status", copy=False, selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id=fields.Many2one("res.partner", string="Partner", required=True)
    property_id=fields.Many2one("res.property", string="Property", required=True)



