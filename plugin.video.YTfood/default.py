# -*- coding: utf-8 -*-
#------------------------------------------------------------
# YT Food
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.YTfood'
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

# Entry point
def run():
    plugintools.log("YTfood.run")
    
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
    plugintools.log("YTfood.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="張媽媽廚房",
        url="plugin://plugin.video.youtube/user/mamacheung"+ID1+"/",
        thumbnail="https://yt3.ggpht.com/-wuwa4F3RyBE/AAAAAAAAAAI/AAAAAAAAAAA/Yugf9xG3bMc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="日日煮",
        url="plugin://plugin.video.youtube/channel/UCYDVigTy-NE2KyCqVCiJb_Q"+ID2+"/",
        thumbnail="https://yt3.ggpht.com/-bccB1jY_CJo/AAAAAAAAAAI/AAAAAAAAAAA/gLoRzxLDN0k/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="真英雄素食",
        url="plugin://plugin.video.youtube/channel/UCryUWjfZLd3Q_aiq677kuGA"+ID3+"/",
        thumbnail="http://www.realherokitchen.com.hk/online_lesson_youtube/realherokitchen.gif",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="飲食籽",
        url="plugin://plugin.video.youtube/playlist/PLBtDO8vnUizoFs2546t1DhockqKoC0i1T"+ID4+"/",
        thumbnail="https://yt3.ggpht.com/-qADe85YpptY/AAAAAAAAAAI/AAAAAAAAAAA/czgngNBS3FI/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Wantanmien",
        url="plugin://plugin.video.youtube/channel/UCsy5tUhFYchN8BFdXJtECRQ"+ID5+"/",
        thumbnail="https://yt3.ggpht.com/-mboGmDJr-c4/AAAAAAAAAAI/AAAAAAAAAAA/gtR0e3mpOQM/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Cooking With May Lynn",
        url="plugin://plugin.video.youtube/channel/UCAXO1tbQzZ5kOUg3BVl0eYw"+ID6+"/",
        thumbnail="https://yt3.ggpht.com/-8efBzKvUTuU/AAAAAAAAAAI/AAAAAAAAAAA/2P-lSNWHqOI/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Helen's Recipes-Vietnamese",
        url="plugin://plugin.video.youtube/channel/UCMmZEL8jV1B61NKAXcyW87A"+ID7+"/",
        thumbnail="https://yt3.ggpht.com/-lXWCk1JjtDQ/AAAAAAAAAAI/AAAAAAAAAAA/WimPbqGFPHw/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="CookingWithDog-Japanese w/sub",
        url="plugin://plugin.video.youtube/channel/UCpprBWvibvmOlI8yJOEAAjA"+ID8+"/",
        thumbnail="https://yt3.ggpht.com/-SixK-U1jMsg/AAAAAAAAAAI/AAAAAAAAAAA/n76jU-5KaTk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Maangchi-Korean",
        url="plugin://plugin.video.youtube/channel/UC8gFadPgK2r1ndqLI04Xvvw"+ID9+"/",
        thumbnail="https://yt3.ggpht.com/-d0KStw-ZOOM/AAAAAAAAAAI/AAAAAAAAAAA/0Im0I-Sr9cg/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Food Wishes",
        url="plugin://plugin.video.youtube/channel/UCRIZtPl9nb9RiXc9btSTQNw"+ID10+"/",
        thumbnail="https://i1.ytimg.com/sh/M0InoNcVcRA/showposter.jpg?v=508859c4",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Nickos Kitchen-Bakery",
        url="plugin://plugin.video.youtube/channel/UCffs63OaN2nh-6StR6hzfiQ"+ID11+"/",
        thumbnail="https://yt3.ggpht.com/-R-PA4kxVgkE/AAAAAAAAAAI/AAAAAAAAAAA/JOEZ7x59uWE/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="BBQ Pit Boys",
        url="plugin://plugin.video.youtube/channel/UCjrL1ugI6xGqQ7VEyV6aRAg"+ID12+"/",
        thumbnail="https://yt3.ggpht.com/-w5MgnW1qxCw/AAAAAAAAAAI/AAAAAAAAAAA/ywS4ukZBIaM/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

run()