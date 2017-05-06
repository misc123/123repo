# -*- coding: utf-8 -*-
#------------------------------------------------------------
# YT Invest
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.YTinvest'
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
    plugintools.log("YTinvest.run")
    
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
    plugintools.log("YTinvest.main_list "+repr(params))
		
    plugintools.add_item( 
        #action="", 
        title="港股策略王－Live",
        url="plugin://plugin.video.youtube/kodion/search/query/?q=%e6%b8%af%e8%82%a1%e7%ad%96%e7%95%a5%e7%8e%8b"+ID1+"/",
        thumbnail="https://yt3.ggpht.com/-rPVbP794xd8/AAAAAAAAAAI/AAAAAAAAAAA/nJ11sH69qeA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
				
    plugintools.add_item( 
        #action="", 
        title="耀才財經台－現場直播",
        url="plugin://plugin.video.youtube/search/?q=%e8%80%80%e6%89%8d%e8%b2%a1%e7%b6%93%e7%9b%b4%e6%92%ad"+ID2+"/",
        thumbnail="https://yt3.ggpht.com/-2a1p3IUP7-8/AAAAAAAAAAI/AAAAAAAAAAA/UMTRAk7NL9g/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="財華社現代電視",
        url="plugin://plugin.video.youtube/user/FintvVideo"+ID3+"/",
        thumbnail="https://yt3.ggpht.com/-Pgty_r-Yrtc/AAAAAAAAAAI/AAAAAAAAAAA/YY60W5swy2o/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="我要做股神",
        url="plugin://plugin.video.youtube/user/SyLingHim"+ID4+"/",
        thumbnail="https://yt3.ggpht.com/-RbitIqe2HBE/AAAAAAAAAAI/AAAAAAAAAAA/zpLnipmv9fE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="香港經濟日報",
        url="plugin://plugin.video.youtube/user/hketvideo"+ID5+"/",
        thumbnail="https://yt3.ggpht.com/-rQ0zIgmg7pQ/AAAAAAAAAAI/AAAAAAAAAAA/dD7nK9UCFc0/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="香港樓市財經頻道",
        url="plugin://plugin.video.youtube/channel/UC7dKKkd0NiE81kpjqnDx0KA"+ID6+"/",
        thumbnail="https://yt3.ggpht.com/-diP4l17qQqk/AAAAAAAAAAI/AAAAAAAAAAA/AmJp4ET7IKg/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Sky Finance Channel",
        url="plugin://plugin.video.youtube/channel/UCupQ2FWhKSlfJYwIUfGMDdw"+ID7+"/",
        thumbnail="https://yt3.ggpht.com/-FmZ8Dd-toZg/AAAAAAAAAAI/AAAAAAAAAAA/fGn-gyVSZts/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
run()