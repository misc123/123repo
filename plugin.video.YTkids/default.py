# -*- coding: utf-8 -*-
#------------------------------------------------------------
# YT Kids
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.YTkids'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID1 = "TheChuChuTV"
YOUTUBE_CHANNEL_ID2 = ""
YOUTUBE_CHANNEL_ID3 = ""

# Entry point
def run():
    plugintools.log("YTsports.run")
    
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
    plugintools.log("YTkids.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="ChuChu TV Nursery Rhymes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail="https://yt3.ggpht.com/-QHPC9emY_8c/AAAAAAAAAAI/AAAAAAAAAAA/03fPGkHcBbk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Disney Movies",
        url="plugin://plugin.video.youtube/search/?q=Disney%20movies%20full%20movies%20english"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail="https://cdn-media.disneymoviesanywhere.com/dma/published/live/categories/web/collection-tile_Princesses_web.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Kid's Movies",
        url="plugin://plugin.video.youtube/search/?q=kids%20movies"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail="http://1.bp.blogspot.com/--Qp4tKzwUyY/VMSR2mhoOGI/AAAAAAAAAVc/9oeTpAI7Mcg/s1600/Disney-Movies.png",
        folder=True )
run()