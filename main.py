import os

from aiohttp import web

from app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    web.run_app(app, port=port)
