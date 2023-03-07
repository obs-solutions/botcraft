# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class Pricelist(models.Model):
    _inherit = "product.pricelist"

    def _compute_price_rule(
            self, products, qty, uom=None, date=False, start_date=None, end_date=None, duration=None,
            unit=None, **kwargs
    ):
        """ Override to handle the temporal product price
         Based on Timebase Rule available for product set the sale order product price
        """
        self.ensure_one()

        if not products:
            return {}

        if not date:
            # Used to fetch pricelist rules and currency rates
            date = fields.Datetime.now()

        results = {}
        # Used to fetch Time based rules for with duration
        time_based_rule = self.product_pricing_ids.filtered(
            lambda i: i.product_template_id.product_variant_id in products)
        if time_based_rule and duration:
            if self._enable_temporal_price(start_date, end_date, duration, unit):
                temporal_products = products.filtered('is_temporal')
                Pricing = self.env['product.pricing']
                for product in temporal_products:
                    if (start_date and end_date) or (duration is not None and unit):
                        pricing = product._get_best_pricing_rule(
                            start_date=start_date, end_date=end_date, duration=duration, unit=unit,
                            pricelist=self, currency=self.currency_id
                        )
                        if not duration:
                            duration_vals = Pricing._compute_duration_vals(start_date, end_date)
                            duration = pricing and duration_vals[pricing.recurrence_id.unit or 'day'] or 0
                    else:
                        pricing = Pricing._get_first_suitable_pricing(product, self)
                        duration = pricing.recurrence_id.duration

                    if pricing:
                        price = pricing._compute_price(duration, unit or pricing.recurrence_id.unit)
                    else:
                        price = product.list_price
                    results[product.id] = pricing.currency_id._convert(
                        price, self.currency_id, self.env.company, date
                    ), False

        price_computed_products = self.env[products._name].browse(results.keys())
        return {
            **results,
            **super()._compute_price_rule(
                products - price_computed_products, qty, uom=uom, date=date, **kwargs),
        }
