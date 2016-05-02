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

YOUTUBE_CHANNEL_ID1 = "UCYDVigTy-NE2KyCqVCiJb_Q"
YOUTUBE_CHANNEL_ID2 = "UCryUWjfZLd3Q_aiq677kuGA"
YOUTUBE_CHANNEL_ID3 = ""
YOUTUBE_CHANNEL_ID4 = "UCsy5tUhFYchN8BFdXJtECRQ"
YOUTUBE_CHANNEL_ID5 = "UCAXO1tbQzZ5kOUg3BVl0eYw"
YOUTUBE_CHANNEL_ID6 = "UCMmZEL8jV1B61NKAXcyW87A"
YOUTUBE_CHANNEL_ID7 = "UCpprBWvibvmOlI8yJOEAAjA"
YOUTUBE_CHANNEL_ID8 = "UC8gFadPgK2r1ndqLI04Xvvw"
YOUTUBE_CHANNEL_ID9 = "UCRIZtPl9nb9RiXc9btSTQNw"
YOUTUBE_CHANNEL_ID10 = "UCffs63OaN2nh-6StR6hzfiQ"
YOUTUBE_CHANNEL_ID11 = "UCjrL1ugI6xGqQ7VEyV6aRAg"

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
        title="日日煮",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail="https://yt3.ggpht.com/-bccB1jY_CJo/AAAAAAAAAAI/AAAAAAAAAAA/gLoRzxLDN0k/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="真英雄素食",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail="http://www.realherokitchen.com.hk/online_lesson_youtube/realherokitchen.gif",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="飲食籽",
        url="plugin://plugin.video.youtube/playlist/PLBtDO8vnUizoFs2546t1DhockqKoC0i1T"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail="https://yt3.ggpht.com/-qADe85YpptY/AAAAAAAAAAI/AAAAAAAAAAA/czgngNBS3FI/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Wantanmien",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID4+"/",
        thumbnail="https://yt3.ggpht.com/-mboGmDJr-c4/AAAAAAAAAAI/AAAAAAAAAAA/gtR0e3mpOQM/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Cooking With May Lynn",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID5+"/",
        thumbnail="https://yt3.ggpht.com/-8efBzKvUTuU/AAAAAAAAAAI/AAAAAAAAAAA/2P-lSNWHqOI/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Helen's Recipes-Vietnamese",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID6+"/",
        thumbnail="https://yt3.ggpht.com/-lXWCk1JjtDQ/AAAAAAAAAAI/AAAAAAAAAAA/WimPbqGFPHw/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="CookingWithDog-Japanese w/sub",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID7+"/",
        thumbnail="https://yt3.ggpht.com/-SixK-U1jMsg/AAAAAAAAAAI/AAAAAAAAAAA/n76jU-5KaTk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Maangchi-Korean",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID8+"/",
        thumbnail="https://yt3.ggpht.com/-d0KStw-ZOOM/AAAAAAAAAAI/AAAAAAAAAAA/0Im0I-Sr9cg/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Food Wishes",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID9+"/",
        thumbnail="https://i1.ytimg.com/sh/M0InoNcVcRA/showposter.jpg?v=508859c4",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Nickos Kitchen-Bakery",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID10+"/",
        thumbnail="https://yt3.ggpht.com/-R-PA4kxVgkE/AAAAAAAAAAI/AAAAAAAAAAA/JOEZ7x59uWE/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="BBQ Pit Boys",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID11+"/",
        thumbnail="https://yt3.ggpht.com/-w5MgnW1qxCw/AAAAAAAAAAI/AAAAAAAAAAA/ywS4ukZBIaM/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

run()