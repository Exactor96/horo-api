from aiohttp import web
from parsers import HoroMail


async def get_horo(request: web.Request) -> web.Response:
    sign = request.query.get('sign')
    timeline = request.query.get('timeline')

    if not sign:
        return web.json_response({'success': False, 'message': 'sign not found'})

    if not timeline:
        return web.json_response({'success': False, 'message': 'timeline not found'})
    horo_mail = HoroMail()

    if not horo_mail.check_timeline(timeline):
        return web.json_response({'success': False, 'message': 'timeline is invalid'})

    data = await horo_mail.get_prediction(sign, timeline)

    return web.json_response({'success': True, 'data': data, 'sign': sign})


async def ping(request: web.Request) -> web.Response:
    return web.json_response({'success': True, 'message': 'pong'})
