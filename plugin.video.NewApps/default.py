# -*- coding: utf-8 -*-
#------------------------------------------------------------
# New Apps
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.NewApps'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

ID0 = "" 
ID1 = ""
ID2 = ""
ID3 = ""
ID4 = ""
ID5 = ""


# Entry point
def run():
    plugintools.log("NewApps.run")
    
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
    plugintools.log("NewApps.main_list "+repr(params)) 

    plugintools.add_item( 
        #action="", 
        title="[COLOR=gold]Click 'Yes' when prompted to download:[/COLOR]",	
        url=""+ID0+"/",
        thumbnail="",
        folder=False )

    plugintools.add_item( 
        #action="", 
        title="測試中",
        url="plugin://plugin.video.icdrama"+ID1+"/",
        thumbnail="plugin://plugin.video.icdrama/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="測試中",
        url="plugin://plugin.video.yinyuetai"+ID2+"/",
        thumbnail="plugin://plugin.video.yinyuetai/icon.png",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="3",
        url=""+ID3+"/",
        thumbnail="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="4",
        url=""+ID4+"/",
        thumbnail="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="5",
        url=""+ID5+"/",
        thumbnail="",
        folder=True )

run()