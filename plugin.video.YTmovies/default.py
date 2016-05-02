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

YOUTUBE_CHANNEL_ID1 = "UCuKO160G7i-F4DNLHluzxAQ/playlists"
YOUTUBE_CHANNEL_ID2 = ""
YOUTUBE_CHANNEL_ID3 = "UCE-Az3DaIYjP9lqxSmQJUCw/playlist/PLx6zdlARSHzb7F26GQaDfvKHa7wiRW_VB"
YOUTUBE_CHANNEL_ID4 = ""
YOUTUBE_CHANNEL_ID5 = ""


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
        title="粵語電影1",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail="https://yt3.ggpht.com/-JnpfGgbZmVk/AAAAAAAAAAI/AAAAAAAAAAA/dstjUg4IoVs/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="粵語電影2",
        url="plugin://plugin.video.youtube/search/?q=hong%20kong%20movies%20cantonese"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/zh/thumb/f/fe/My_Lucky_Stars.jpg/220px-My_Lucky_Stars.jpg",
        folder=True )			
		
    plugintools.add_item( 
        #action="", 
        title="韓國電影1",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/1/13/KoreaSfilm.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="韓國電影2",
        url="plugin://plugin.video.youtube/search/?q=korean%20movies%20chinese%20subtitles"+YOUTUBE_CHANNEL_ID4+"/",
        thumbnail="http://www.hancinema.net/images/logo_hancinema_pure.png",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="日本電影",
        url="plugin://plugin.video.youtube/search/?q=japanese%20movies%20subtitles"+YOUTUBE_CHANNEL_ID5+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Japan_film_icon.svg/80px-Japan_film_icon.svg.png",
        folder=True )	
run()