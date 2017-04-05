import uuid
import xbmcaddon

_addon = xbmcaddon.Addon()

title_lang = int(_addon.getSetting('title_language'))
allow_ga = _addon.getSetting('allow_ga') == 'true'
user_agent = str(_addon.getSetting('user_agent'))

client_id = _addon.getSetting('client_id')
if not client_id:
    client_id = str(uuid.uuid4())
    _addon.setSetting('client_id', client_id)
