from datetime import datetime
import aiohttp
from bs4 import BeautifulSoup


class HoroMail:
    URLBASE = "https://horo.mail.ru/prediction/{sign}/{timeline}/"

    SIGN_ALIASES = {
        'aries': 'aries',
        'taurus': 'taurus',
        'gemini': 'gemini',
        'cancer': 'cancer',
        'leo': 'leo',
        'virgo': 'virgo',
        'libra': 'libra',
        'scorpio': 'scorpio',
        'sagittarius': 'sagittarius',
        'capricorn': 'capricorn',
        'aquarius': 'aquarius',
        'pisces': 'pisces',
    }

    TIMELINES = [
        'today',
        'tomorrow',
        'yesterday',
        'week',
        'month',
        'year',
        str(datetime.now().year)
    ]

    async def make_request(self, sign, timeline):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.URLBASE.format(sign=sign, timeline=timeline)) as resp:
                return await resp.text()

    def check_timeline(self, timeline):
        return timeline in self.TIMELINES

    def check_sign(self, sign):
        return sign in self.SIGN_ALIASES.values()

    async def get_prediction(self, sign, timeline):
        if not self.check_sign(sign):
            return 'Not found'

        html = await self.make_request(sign=sign, timeline=timeline)

        soup = BeautifulSoup(html, 'html.parser')

        prediction_html = soup.find('div', {'class': 'article__item article__item_alignment_left article__item_html'})

        predictions = [str(prediction.text) for prediction in prediction_html.find_all('p')]

        return '\n'.join(predictions)
