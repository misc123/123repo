# -*- coding: utf-8 -*-
#------------------------------------------------------------
# YT Sports
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.YTsports'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

ID1 = ""
ID2 = ""
ID3 = ""

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
    plugintools.log("YTsports.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="NBA",
        url="plugin://plugin.video.youtube/channel/UCWJ2lWNubArHWmf3FIHbfcQ"+ID1+"/",
        thumbnail="https://yt3.ggpht.com/-iykIxE6HFpM/AAAAAAAAAAI/AAAAAAAAAAA/qho7mLdsPLc/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="NHL",
        url="plugin://plugin.video.youtube/channel/UCqFMzb-4AUf6WAIbl132QKA"+ID2+"/",
        thumbnail="https://yt3.ggpht.com/-FQVi29epjis/AAAAAAAAAAI/AAAAAAAAAAA/P2CB1cyLKFc/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="UFC",
        url="plugin://plugin.video.youtube/channel/UCvgfXK4nTYKudb0rFR6noLA"+ID3+"/",
        thumbnail="https://yt3.ggpht.com/-QeD1gcM_f7k/AAAAAAAAAAI/AAAAAAAAAAA/RrU6oF2FBU0/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
		
run()