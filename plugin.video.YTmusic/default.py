# -*- coding: utf-8 -*-
#------------------------------------------------------------
# YT Music
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.YTmusic'
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

# Entry point
def run():
    plugintools.log("YTmusic.run")
    
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
    plugintools.log("YTmusic.main_list "+repr(params))
        
    plugintools.add_item( 
        #action="", 
        title="Lypur Piano-Theory",
        url="plugin://plugin.video.youtube/channel/UCpzgTNTgQsR9YYsyOm3k3KQ"+ID1+"/",
        thumbnail="https://yt3.ggpht.com/-1KyjFXrXOvk/AAAAAAAAAAI/AAAAAAAAAAA/h6vqXQ-DI5s/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="PlayPianoTODAY.com",
        url="plugin://plugin.video.youtube/channel/UCA-oSxA0_mTwtvEdOX4yMdA"+ID2+"/",
        thumbnail="https://www.playpianotoday.com/images/play-piano-today-logo_segno.png",
        folder=True )
		        
    plugintools.add_item( 
        #action="", 
        title="Learn piano in 10 lessons",
        url="plugin://plugin.video.youtube/user/danthecomposer"+ID3+"/",
        thumbnail="https://yt3.ggpht.com/-bS0JaBhU1rw/AAAAAAAAAAI/AAAAAAAAAAA/Y26mWoChix0/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JustinGuitar Songs",
        url="plugin://plugin.video.youtube/channel/UCcZd_G62wtsCXd-b7OhQdlw"+ID4+"/",
        thumbnail="https://yt3.ggpht.com/-J5JjwMbMlbg/AAAAAAAAAAI/AAAAAAAAAAA/79T6mW1XlKU/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="JustinGuitar",
        url="plugin://plugin.video.youtube/channel/UCBNkm8o5LiEVLxO8w0p2sfQ"+ID5+"/",
        thumbnail="https://yt3.ggpht.com/-5lZN4lWqIJ4/AAAAAAAAAAI/AAAAAAAAAAA/OTjz43hchDk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Six String Country",
        url="plugin://plugin.video.youtube/user/sixstringcountryhd"+ID6+"/",
        thumbnail="https://yt3.ggpht.com/-ymMAMBus87Y/AAAAAAAAAAI/AAAAAAAAAAA/dkTJASKtEp4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
      
    plugintools.add_item( 
        #action="", 
        title="The Ukulele Teacher",
        url="plugin://plugin.video.youtube/channel/UC1HlihY-iNtOemAlYQq3GXQ"+ID7+"/",
        thumbnail="https://yt3.ggpht.com/-7PP4UcxiVCc/AAAAAAAAAAI/AAAAAAAAAAA/rKKKi4-cc6M/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

run()