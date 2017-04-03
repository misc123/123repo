# -*- coding: utf-8 -*-
#------------------------------------------------------------
# YT Movies
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.YTmovies'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

ID1 = ""
ID2 = ""
ID3 = ""
ID4 = ""
ID5 = ""
ID6 = ""
ID7 = ""
ID8 = ""
ID9 = ""
ID10 = ""

# Entry point
def run():
    plugintools.log("YTmovies.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("YTmovies.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="华语热播影视剧大本营",
        url="plugin://plugin.video.youtube/channel/UCKn4SloJmZYNYNq6RgzgrHw/playlists"+ID1+"/",
        thumbnail="https://yt3.ggpht.com/-3I2MApIMLHM/AAAAAAAAAAI/AAAAAAAAAAA/4vVxqjO5FZ4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="华语电视剧 官方频道",
        url="plugin://plugin.video.youtube/channel/UCX8mkGxfZP5uhzNNvFBo7Kw/playlists"+ID2+"/",
        thumbnail="https://yt3.ggpht.com/-5yCkq6BLXNo/AAAAAAAAAAI/AAAAAAAAAAA/A_XZ3FzWmp8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="大劇獨播",
        url="plugin://plugin.video.youtube/channel/UCNORTw_uosRNGgdEjwdHvuw/playlists"+ID3+"/",
        thumbnail="https://yt3.ggpht.com/-ONpJ-FuL14Y/AAAAAAAAAAI/AAAAAAAAAAA/ja4pf5PLQPc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="大劇獨播Plus",
        url="plugin://plugin.video.youtube/channel/UCC5TlXzHiGi5L5KPbybIJrw/playlists"+ID4+"/",
        thumbnail="https://yt3.ggpht.com/-dilMxQaE7sc/AAAAAAAAAAI/AAAAAAAAAAA/dPAtljTdAKY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="电影公社",
        url="plugin://plugin.video.youtube/channel/UCDrhLlg2TFXEYRdSmyS6hBQ/playlists"+ID5+"/",
        thumbnail="https://yt3.ggpht.com/-TOHWieuD_mI/AAAAAAAAAAI/AAAAAAAAAAA/1b5m0SQh9gA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="粵語電影1",
        url="plugin://plugin.video.youtube/channel/UCuKO160G7i-F4DNLHluzxAQ/playlists"+ID6+"/",
        thumbnail="https://yt3.ggpht.com/-JnpfGgbZmVk/AAAAAAAAAAI/AAAAAAAAAAA/dstjUg4IoVs/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="粵語電影2",
        url="plugin://plugin.video.youtube/search/?q=hong%20kong%20movies%20cantonese"+ID7+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/zh/thumb/f/fe/My_Lucky_Stars.jpg/220px-My_Lucky_Stars.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="韓國電影1",
        url="plugin://plugin.video.youtube/channel/UCE-Az3DaIYjP9lqxSmQJUCw/playlist/PLx6zdlARSHzb7F26GQaDfvKHa7wiRW_VB"+ID8+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/1/13/KoreaSfilm.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="韓國電影2",
        url="plugin://plugin.video.youtube/search/?q=korean%20movies%20chinese%20subtitles"+ID9+"/",
        thumbnail="http://www.hancinema.net/images/logo_hancinema_pure.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="日本電影",
        url="plugin://plugin.video.youtube/search/?q=japanese%20movies%20subtitles"+ID10+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Japan_film_icon.svg/80px-Japan_film_icon.svg.png",
        folder=True )

run()