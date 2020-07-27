from scrapy import Spider, Request
from states.items import StatesItem
import re

class StatesSpider(Spider):
    name = "states_spider"
    allowed_urls = ["https://www.usnews.com/"]
    start_urls = ["https://www.usnews.com/news/best-states/rankings/natural-environment/air-water-quality"]

    def parse(self, response):
        rows_1 = response.xpath('//table[@class="TableTabular__TableContainer-impg-0 hjgtDg"]/tbody/tr[@class="TableTabular__TableRow-impg-1 gEWIto zebra"]')
        rows_2 = response.xpath('//table[@class="TableTabular__TableContainer-impg-0 hjgtDg"]/tbody/tr[@class="TableTabular__TableRow-impg-1 gEWIto"]')

        for row in rows_1:
            overall_ranking = row.xpath('.//span[@class="Span-sc-19wk4id-0 ezTccn"]/text()')[0].extract()
            state_name = row.xpath('.//span[@class="Span-sc-19wk4id-0 CBOWI"]/text()').extract_first()
            air_quality_ranking = row.xpath('.//span[@class="Span-sc-19wk4id-0 ezTccn"]/text()')[1].extract()
            water_quality_ranking = row.xpath('.//span[@class="Span-sc-19wk4id-0 ezTccn"]/text()')[2].extract()

            state_url = 'https://www.usnews.com' + row.xpath('.//div[@class="Box-w0dun1-0 iBOmAc Show-oz18v2-0 fMqFIG"]/a/@href').extract_first()

            meta = {'overall_ranking': overall_ranking, 'state_name': state_name, 'air_quality_ranking': air_quality_ranking, 'water_quality_ranking': water_quality_ranking}

            yield Request(url=state_url, callback=self.parse_state_page, meta=meta)

        for row in rows_2:
            overall_ranking = row.xpath('.//span[@class="Span-sc-19wk4id-0 ezTccn"]/text()')[0].extract()
            state_name = row.xpath('.//span[@class="Span-sc-19wk4id-0 CBOWI"]/text()').extract_first()
            air_quality_ranking = row.xpath('.//span[@class="Span-sc-19wk4id-0 ezTccn"]/text()')[1].extract()
            water_quality_ranking = row.xpath('.//span[@class="Span-sc-19wk4id-0 ezTccn"]/text()')[2].extract()

            state_url = 'https://www.usnews.com' + row.xpath('.//div[@class="Box-w0dun1-0 iBOmAc Show-oz18v2-0 fMqFIG"]/a/@href').extract_first()

            meta = {'overall_ranking': overall_ranking, 'state_name': state_name, 'air_quality_ranking': air_quality_ranking, 'water_quality_ranking': water_quality_ranking}

            yield Request(url=state_url, callback=self.parse_state_page, meta=meta)

    def parse_state_page(self, response):
        area_in_sq_mi = response.xpath('//div[@class="Grid-lx2f3i-0 gsCvcz"]//dl[@class="QuickStats-sc-6jc7cd-0 iiHxpW"]/dd/text()')[0].extract().replace(',', '')
        area_in_sq_mi = int(re.findall('(\d+) SQ. MI.', area_in_sq_mi)[0])

        gdp_in_billion = response.xpath('//div[@class="Grid-lx2f3i-0 gsCvcz"]//dl[@class="QuickStats-sc-6jc7cd-0 iiHxpW"]/dd/text()')[1].extract().replace(',', '')
        gdp_in_billion = float(re.findall('\W(\d+\.\d+) Billion', gdp_in_billion)[0])

        college_educated_in_percentage = response.xpath('//div[@class="Grid-lx2f3i-0 gsCvcz"]//dl[@class="QuickStats-sc-6jc7cd-0 iiHxpW"]/dd/text()')[2].extract()
        college_educated_in_percentage = int(re.findall('(\d+)%', college_educated_in_percentage)[0])

        population = response.xpath('//div[@class="Grid-lx2f3i-0 gsCvcz"]//dl[@class="QuickStats-sc-6jc7cd-0 iiHxpW"]/dd/text()')[3].extract().replace(',', '')
        population = int(re.findall('\d+', population)[0])

        median_income_in_dollar = response.xpath('//div[@class="Grid-lx2f3i-0 gsCvcz"]//dl[@class="QuickStats-sc-6jc7cd-0 iiHxpW"]/dd/text()')[5].extract().replace(',', '')
        median_income_in_dollar = int(re.findall('\W(\d+)', median_income_in_dollar)[0])

        energy_ranking = response.xpath('//div[@class="mb5"]//div[@class="Cell-sc-1abjmm4-0 ScorecardSection__BodyCell-sc-1beiwt5-0 dMreLJ"]//table//tbody//tr/td/text()')[16].extract()
        energy_ranking = int(re.findall('#(\d+)', energy_ranking)[0])

        transportation_ranking = response.xpath('//div[@class="mb5"]//div[@class="Cell-sc-1abjmm4-0 ScorecardSection__BodyCell-sc-1beiwt5-0 dMreLJ"]//table//tbody//tr/td/text()')[18].extract()
        transportation_ranking = int(re.findall('#(\d+)', transportation_ranking)[0])

        pollution_ranking = response.xpath('//div[@class="mb5"]//div[@class="Cell-sc-1abjmm4-0 ScorecardSection__BodyCell-sc-1beiwt5-0 dMreLJ"]//table//tbody//tr/td/text()')[-1].extract()
        pollution_ranking = int(re.findall('#(\d+)', pollution_ranking)[0])

        renewable_energy_usage_in_percentage = response.xpath('//div[@class="InfographicCard__GraphicCell-sc-1gn15vg-3 kjnMxq"]//span[@class="Span-sc-19wk4id-0 dykGAJ"]/text()')[0].extract()
        renewable_energy_usage_in_percentage = float(re.findall('(\d?\.?\d)%', renewable_energy_usage_in_percentage)[0])

        roads_in_poor_condition_in_percentage = response.xpath('//div[@class="InfographicCard__FlexDiv-sc-1gn15vg-2 ewYhhV"]//span[@class="Span-sc-19wk4id-0 fhbprU"]/text()')[1].extract()
        roads_in_poor_condition_in_percentage = float(re.findall('(\d?\.?\d)%', roads_in_poor_condition_in_percentage)[0])

        days_with_unhealthy_air_quality = response.xpath('//div[@class="InfographicCard__GraphicCell-sc-1gn15vg-3 jPxMSh"]//span[@class="Span-sc-19wk4id-0 iGxGjZ"]/text()')[1].extract()

        drinking_water_violation_points = response.xpath('//div[@class="InfographicCard__GraphicCell-sc-1gn15vg-3 kjnMxq"]//span[@class="Span-sc-19wk4id-0 itKMhR"]/text()')[1].extract()

        industrial_toxins_lbs_per_sq_mi = response.xpath('//div[@class="InfographicCard__GraphicCell-sc-1gn15vg-3 kjnMxq"]//span[@class="Span-sc-19wk4id-0 kpBKHU"]/text()')[-1].extract().replace(',', '')

        item = StatesItem()
        item['area_in_sq_mi'] = area_in_sq_mi
        item['gdp_in_billion'] = gdp_in_billion
        item['college_educated_in_percentage'] = college_educated_in_percentage
        item['population'] = population
        item['median_income_in_dollar'] = median_income_in_dollar
        item['energy_ranking'] = energy_ranking
        item['transportation_ranking'] = transportation_ranking
        item['pollution_ranking'] = pollution_ranking
        item['renewable_energy_usage_in_percentage'] = renewable_energy_usage_in_percentage
        item['roads_in_poor_condition_in_percentage'] = roads_in_poor_condition_in_percentage
        item['days_with_unhealthy_air_quality'] = days_with_unhealthy_air_quality
        item['drinking_water_violation_points'] = drinking_water_violation_points
        item['industrial_toxins_lbs_per_sq_mi'] = industrial_toxins_lbs_per_sq_mi
        item['overall_ranking'] = response.meta['overall_ranking']
        item['state_name'] = response.meta['state_name']
        item['air_quality_ranking'] = response.meta['air_quality_ranking']
        item['water_quality_ranking'] = response.meta['water_quality_ranking']

        yield item
