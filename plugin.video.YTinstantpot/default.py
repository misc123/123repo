# -*- coding: utf-8 -*-
#------------------------------------------------------------
# YT Instant Pot
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.YTinstantpot'
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
    plugintools.log("YTinstantpot.run")
    
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
    plugintools.log("YTinstantpot.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Instant Pot",
        url="plugin://plugin.video.youtube/user/TheInstantpot"+ID1+"/",
        thumbnail="https://yt3.ggpht.com/-3OB9Fj6NFbQ/AAAAAAAAAAI/AAAAAAAAAAA/4c0ClrLlprE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Asian Recipes",
        url="plugin://plugin.video.youtube/channel/UC_CoMTkmck2TFXArC1BYeLg"+ID2+"/",
        thumbnail="https://yt3.ggpht.com/-w7IWCUygxQ0/AAAAAAAAAAI/AAAAAAAAAAA/wOpREZ5ffSo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Flo Lum",
        url="plugin://plugin.video.youtube/user/flolum"+ID3+"/",
        thumbnail="https://yt3.ggpht.com/-2WS6-oPs3WI/AAAAAAAAAAI/AAAAAAAAAAA/tsEPbgdgC9k/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Krafty Kewty",
        url="plugin://plugin.video.youtube/channel/UC7Jx4TTw2mV5mGJxtX_LlwQ"+ID4+"/",
        thumbnail="https://yt3.ggpht.com/-7b_m2YOi9pA/AAAAAAAAAAI/AAAAAAAAAAA/fNV9MQxDBl8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Instant Pot 101",
        url="plugin://plugin.video.youtube/channel/UCoPNXUqoRn-C6oMKTqVP3_A"+ID5+"/",
        thumbnail="https://yt3.ggpht.com/-pmh9qVjJR5A/AAAAAAAAAAI/AAAAAAAAAAA/F_WZiNLThYU/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Traci Davies",
        url="plugin://plugin.video.youtube/playlist/PLr4sx0UkLzen3jY6_KUl9Y79FvcyRNyy_"+ID6+"/",
        thumbnail="https://yt3.ggpht.com/-fZwCNBoKajA/AAAAAAAAAAI/AAAAAAAAAAA/CNi0EBYmlrY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Yvonne Barthe",
        url="plugin://plugin.video.youtube/playlist/PLW0hNjsJItOn8yWHy6Ii1P8_rjd4vS6Co"+ID7+"/",
        thumbnail="https://yt3.ggpht.com/-HoUPfvtTF5E/AAAAAAAAAAI/AAAAAAAAAAA/v2fYstoKb90/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Instant Pot Info, Recipes & Tips",
        url="plugin://plugin.video.youtube/playlist/PLqImw0T9j_Tbc_G6Ld5jJY52da2ZBFT89"+ID8+"/",
        thumbnail="https://yt3.ggpht.com/-1bS1gFeBEVk/AAAAAAAAAAI/AAAAAAAAAAA/Gg1czafnOAE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
				
    plugintools.add_item( 
        #action="", 
        title="Pressure Cooker Recipes",
        url="plugin://plugin.video.youtube/playlist/PLK-rkSuShuyt0o0Z9m58ifoeq0i85lFWs"+ID9+"/",
        thumbnail="https://yt3.ggpht.com/-Jr9_gAI-_mo/AAAAAAAAAAI/AAAAAAAAAAA/Mn6u5Mto8e4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Instant pot recipes - Search",
        url="plugin://plugin.video.youtube/search/?q=instant+pot+recipes"+ID10+"/",
        thumbnail="https://books.google.com/books/content/images/frontcover/UhZBDgAAQBAJ?fife=w300-rw",
        folder=True )
		
run()