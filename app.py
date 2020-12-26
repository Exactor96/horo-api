from aiohttp import web

import views

app = web.Application()
app.add_routes(
    [
        web.get('/ping', views.ping),
        web.get('/mail-horoscope', views.get_horo),
    ]
)
