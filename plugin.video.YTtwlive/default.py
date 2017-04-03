# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Taiwan Live News
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.YTtwlive'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

# Entry point
def run():
    plugintools.log("YTtwlive.run")
    
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
    plugintools.log("YTtwlive.main_list "+repr(params))
		
    plugintools.add_item( 
        #action="", 
        title="新聞直播",
        url="plugin://plugin.video.youtube/playlist/PLjDuWqsWQ3IUvk76CyTBaCWXnHr3MW4IP/",
        thumbnail=icon,
        folder=True )
		
run()
