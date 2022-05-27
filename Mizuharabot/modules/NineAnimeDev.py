from Mizuharabot import telethn
from Mizuharabot.events import register

from animedev import client as AnimeDevClient, exceptions

@register(pattern='/search')
async def animedev_function(event):
    await event.reply(str(event.message))
    anime_name = event.message.split()
    if len(anime_name) <= 1:
        await message.reply_text('Please enter the anime name.\n\n<b>Example:</b>\n/search Doraemon.')
        return
    try:
        anime = AnimeDevClient.search(' '.join(anime_name[1:]))
    except exceptions.NotFound:
        await message.reply_text('Anime not found.')
        return
    except Exception as e:
        await message.reply_text(f'[ERROR]: {e}\n\nPlease report this at @Shinobu_Support.')
        return
    msg_text = f'''
Anime Title: {anime['AnimeTitle']}
    '''
    buttons = [[Button.url('Download Link', anime['AnimeLink'])], [Button.url('Search Query', anime['Search_Query'])]]
    await telethn.send_file(event.chat_id, anime['AnimeImg'], caption=msg_text)
