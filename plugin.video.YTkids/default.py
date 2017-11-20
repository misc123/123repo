# -*- coding: utf-8 -*-
#------------------------------------------------------------
# YT Kids
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.YTkids'
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
    plugintools.log("YTkids.run")
    
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
    plugintools.log("YTkids.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="PAW Patrol",
        url="plugin://plugin.video.youtube/kodion/search/query/?q=PAW%20Patrol"+ID1+"/",
        thumbnail="http://cardiffmummysays.com/wp-content/uploads/2016/04/Paw-Patrol-3.png",
        folder=True )
 
    plugintools.add_item( 
        #action="", 
        title="Curious George",
        url="plugin://plugin.video.youtube/kodion/search/query/?q=Curious%20George"+ID2+"/",
        thumbnail="http://www.wgbh.org/imageassets2/curiousgeorge.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Disney Movies",
        url="plugin://plugin.video.youtube/search/?q=Disney%20movies%20full%20movies%20english"+ID3+"/",
        thumbnail="https://cdn-media.disneymoviesanywhere.com/dma/published/live/categories/web/collection-tile_Princesses_web.jpg",
        folder=True )
        		
    plugintools.add_item( 
        #action="", 
        title="Kid's Movies",
        url="plugin://plugin.video.youtube/search/?q=kids%20movies"+ID4+"/",
        thumbnail="http://1.bp.blogspot.com/--Qp4tKzwUyY/VMSR2mhoOGI/AAAAAAAAAVc/9oeTpAI7Mcg/s1600/Disney-Movies.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Disney Songs",
        url="plugin://plugin.video.youtube/playlist/PLY8ZoU3QxiG3I4XtrmWwCSDh7Pt6y09zL"+ID5+"/",
        thumbnail="https://i5.walmartimages.com/asr/b189fd24-505c-43b5-b6e5-c41bb7dddae3_1.be1f8a6e57319371bdd8096ff96c59b0.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nursery Rhymes Karaoke",
        url="plugin://plugin.video.youtube/playlist/PL8664D410C80B373F"+ID6+"/",
        thumbnail="http://a3.mzstatic.com/us/r30/Purple/v4/11/87/00/1187004b-64a9-eda9-de74-df7ddff21016/screen480x480.jpeg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="ChuChu TV Nursery Rhymes",
        url="plugin://plugin.video.youtube/user/TheChuChuTV"+ID7+"/",
        thumbnail="https://yt3.ggpht.com/-QHPC9emY_8c/AAAAAAAAAAI/AAAAAAAAAAA/03fPGkHcBbk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

run()