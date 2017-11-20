# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Adult Channels

#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.adult'
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
ID11 = ""
ID12 = ""
ID13 = ""

# Entry point
def run():
    plugintools.log("adult.run")
    
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
    plugintools.log("adult.main_list "+repr(params)) 

    plugintools.add_item( 
        #action="", 
        title="Video Devil",
        url="plugin://plugin.video.videodevil"+ID1+"/",
        thumbnail="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Adult Hideout",
        url="plugin://plugin.video.adulthideout"+ID2+"/",
        thumbnail="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Fantasti.cc",
        url="plugin://plugin.video.fantasticc"+ID3+"/",
        thumbnail="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Empflix",
        url="plugin://plugin.video.empflix"+ID4+"/",
        thumbnail="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Erotik",
        url="plugin://plugin.video.erotik"+ID5+"/",
        thumbnail="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="LubeTube",
        url="plugin://plugin.video.lubetube"+ID6+"/",
        thumbnail="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tube8",
        url="plugin://plugin.video.tube8"+ID7+"/",
        thumbnail="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Ultra White Cream",
        url="plugin://plugin.video.uwc"+ID8+"/",
        thumbnail="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="xxTrucoxx",
        url="plugin://plugin.video.xxtrucoxx"+ID9+"/",
        thumbnail="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="You Jizz",
        url="plugin://plugin.video.you.jizz"+ID10+"/",
        thumbnail="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jizz Planet",
        url="plugin://plugin.video.jizzplanet"+ID11+"/",
        thumbnail="",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Wood Rocket",
        url="plugin://plugin.video.woodrocket"+ID12+"/",
        thumbnail="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JavStream",
        url="plugin://plugin.video.javstream"+ID13+"/",
        thumbnail="",
        folder=True )

run()