from aiohttp import web

from .foursquare import get_foursquare_category, InvalidQueryException


async def foursquare_category(request):
    client = request.app['client']
    try:
        response = await get_foursquare_category(client, request.query)
    except InvalidQueryException as ex:
        return web.json_response({'error': str(ex)}, status=400)
    return web.json_response(response)
