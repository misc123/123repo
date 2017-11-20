# -*- coding: utf-8 -*-
#------------------------------------------------------------
# YT Karaoke
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.YTkaraoke'
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
    plugintools.log("YTkaraoke.run")
    
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
    plugintools.log("YTkaraoke.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Mikey's Karaoke",
        url="plugin://plugin.video.MikeysKaraoke"+ID1+"/",
        thumbnail="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="The KARAOKE Channel",
        url="plugin://plugin.video.youtube/channel/UCYi9TC1HC_U2kaRAK6I4FSQ"+ID2+"/",
        thumbnail="https://yt3.ggpht.com/-8Ee1BcZtW7g/AAAAAAAAAAI/AAAAAAAAAAA/JqoBo946g0Q/s240-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="KaraFun",
        url="plugin://plugin.video.youtube/channel/UCbqcG1rdt9LMwOJN4PyGTKg/playlists"+ID3+"/",
        thumbnail="https://yt3.ggpht.com/-fYBYIzoKwv0/AAAAAAAAAAI/AAAAAAAAAAA/gOIMUmKxXT8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Sing King Karaoke",
        url="plugin://plugin.video.youtube/channel/UCwTRjvjVge51X-ILJ4i22ew"+ID4+"/",
        thumbnail="https://yt3.ggpht.com/-RQAPMaxL1gE/AAAAAAAAAAI/AAAAAAAAAAA/zawPgoguLwI/s240-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Original Karaoke",
        url="plugin://plugin.video.youtube/channel/UCnM6QQeanPgBRyEMeFmrNnA"+ID5+"/",
        thumbnail="https://i.ytimg.com/i/nM6QQeanPgBRyEMeFmrNnA/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Oldies Love Songs",
        url="plugin://plugin.video.youtube/playlist/PL85FA0BC339A2D54A"+ID6+"/",
        thumbnail="http://cdn-s3.allmusic.com/release-covers/500/0001/641/0001641834.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Golden Oldies",
        url="plugin://plugin.video.youtube/playlist/PL5731F33837BC5BBF"+ID7+"/",
        thumbnail="http://images.8tracks.com/cover/i/008/534/906/oldies_app-8394.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="50s 60s 70s",
        url="plugin://plugin.video.youtube/playlist/PLNVb4XeGx1kJD3Md0xJQIUv8l7z9u3_-Z"+ID8+"/",
        thumbnail="http://cps-static.rovicorp.com/3/JPG_500/MI0000/499/MI0000499483.jpg?partner=allrovi.com",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="70s 80s",
        url="plugin://plugin.video.youtube/playlist/PL86C45E6B701AD75F"+ID9+"/",
        thumbnail="https://i3.radionomy.com/radios/400/bb195f0d-738a-42aa-b717-88dfda048d92.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Karaoke Hits Channel",
        url="plugin://plugin.video.youtube/channel/UCjCBQdXHbIJ_u2Wm-WMb9ow"+ID10+"/",
        thumbnail="https://yt3.ggpht.com/-UiTYorDOlL8/AAAAAAAAAAI/AAAAAAAAAAA/ZE5jWN2xNrw/s240-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rock and Roll Oldies",
        url="plugin://plugin.video.youtube/playlist/PL96CED83AA24CE6DD"+ID11+"/",
        thumbnail="http://images.clipartpanda.com/rock-music-guitar-rock-n-roll-guitar-head.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Kids Songs Karaoke",
        url="plugin://plugin.video.youtube/channel/UCOWgg92ii_Kvakk1HwTmdmg"+ID12+"/",
        thumbnail="https://yt3.ggpht.com/-O6c49V2ivr8/AAAAAAAAAAI/AAAAAAAAAAA/R37sgGvCrzE/s240-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="You Music",
        url="plugin://plugin.video.YouMusic"+ID13+"/",
        thumbnail="",
        folder=True )		
		
run()