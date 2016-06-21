# -*- coding: utf-8 -*-
#------------------------------------------------------------
# YT News
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.YTnews'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID1 = "UC1Sh4WkuFCRM4hyTjaJLrHw"
YOUTUBE_CHANNEL_ID2 = "kartoroTEL"
YOUTUBE_CHANNEL_ID3 = "UCeqUUXaM75wrK5Aalo6UorQ"
YOUTUBE_CHANNEL_ID4 = "UC-8CVMKt5Zlju_i07zhkC-Q"
YOUTUBE_CHANNEL_ID5 = "PLPY0_ooDN1dvClKgo7K1tAS26PeAHmikd"
YOUTUBE_CHANNEL_ID6 = "UCeFbWIhDj_tjTOTe1P3cVHA"
YOUTUBE_CHANNEL_ID7 = "UCsTeCS6s9YoNn2kbQVAgDsQ"
YOUTUBE_CHANNEL_ID8 = "UC4NjmIegGw-HyQCmxwAEZBQ"
YOUTUBE_CHANNEL_ID9 = "UCgwOhn9ghL2jY5qJEzpzSzw"
YOUTUBE_CHANNEL_ID10 = "UC5kySUzP0p4Q4Y1rnQLX_bw"

# Entry point
def run():
    plugintools.log("YTnews.run")
    
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
    plugintools.log("YTnews.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="六點半新聞報導",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail="http://img57.imagetwist.com/th/06751/u1mjcp90nfe2.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="ViuTV新聞報導",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail="https://yt3.ggpht.com/-0lEvcl2d9EQ/AAAAAAAAAAI/AAAAAAAAAAA/SevqkXLhllg/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="蘋果動新聞",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail="https://yt3.ggpht.com/-UnzSE4d_M1s/AAAAAAAAAAI/AAAAAAAAAAA/NeWTKNbP3TY/s240-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="壹週Plus",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID4+"/",
        thumbnail="https://yt3.ggpht.com/-NfnRCKGfeao/AAAAAAAAAAI/AAAAAAAAAAA/Bp_UFIBmGoA/s240-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="最新蕭析",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID5+"/",
        thumbnail="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSaLz_W0D6UR_z8HS3vRSYAcFAmyKEIw2RBWkWku6p0YAWUKPHB5EOxXtw",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="E週刊",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID6+"/",
        thumbnail="https://yt3.ggpht.com/-16m06v5p7I0/AAAAAAAAAAI/AAAAAAAAAAA/GYFZFRdrU88/s240-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="東周網",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID7+"/",
        thumbnail="https://yt3.ggpht.com/-Ak12dd6RJWY/AAAAAAAAAAI/AAAAAAAAAAA/Ks4e7PCESzs/s240-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="東網電視",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID8+"/",
        thumbnail="https://yt3.ggpht.com/-RaYcmdVASWQ/AAAAAAAAAAI/AAAAAAAAAAA/fSo0Yjk_GuQ/s240-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="恩雨之聲",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID9+"/",
        thumbnail="https://yt3.ggpht.com/-g4j3jPE-tcg/AAAAAAAAAAI/AAAAAAAAAAA/-qthveptCm8/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="多倫多 WOWtv",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID10+"/",
        thumbnail="https://yt3.ggpht.com/-gYZVZ2dGwUk/AAAAAAAAAAI/AAAAAAAAAAA/5rJVdrjlPSE/s176-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

run()