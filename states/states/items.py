# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StatesItem(scrapy.Item):
    overall_ranking = scrapy.Field()
    state_name = scrapy.Field()
    air_quality_ranking = scrapy.Field()
    water_quality_ranking = scrapy.Field()
    area_in_sq_mi = scrapy.Field()
    gdp_in_billion = scrapy.Field()
    college_educated_in_percentage = scrapy.Field()
    population = scrapy.Field()
    median_income_in_dollar = scrapy.Field()
    energy_ranking = scrapy.Field()
    transportation_ranking = scrapy.Field()
    pollution_ranking = scrapy.Field()
    renewable_energy_usage_in_percentage = scrapy.Field()
    roads_in_poor_condition_in_percentage = scrapy.Field()
    days_with_unhealthy_air_quality = scrapy.Field()
    drinking_water_violation_points = scrapy.Field()
    industrial_toxins_lbs_per_sq_mi = scrapy.Field()
