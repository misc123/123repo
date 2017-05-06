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
ID14 = ""
ID15 = ""
ID16 = ""
ID17 = ""
ID18 = ""
ID19 = ""
ID20 = ""

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
        title="香港新聞台",
        url="plugin://plugin.video.youtube/channel/UC1Sh4WkuFCRM4hyTjaJLrHw"+ID1+"/",
        thumbnail="https://yt3.ggpht.com/-pEN6mbclUZQ/AAAAAAAAAAI/AAAAAAAAAAA/lURW_nVyLxE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="香港新聞最前線",
        url="plugin://plugin.video.youtube/channel/UC2Sm3oY4VL3wzEvcO44b-ow"+ID2+"/",
        thumbnail="https://yt3.ggpht.com/-8Kc1YVDl5-8/AAAAAAAAAAI/AAAAAAAAAAA/0-CH5h3SGbM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="ViuTV新聞報導",
        url="plugin://plugin.video.youtube/channel/UCxIE4UYD76RdetMRhzaYGzA"+ID3+"/",
        thumbnail="https://yt3.ggpht.com/-0lEvcl2d9EQ/AAAAAAAAAAI/AAAAAAAAAAA/SevqkXLhllg/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="我係香港人",
        url="plugin://plugin.video.youtube/channel/UCODPdv6Gu8ZknI0eCKgP5ag"+ID4+"/",
        thumbnail="https://yt3.ggpht.com/-upO0s5u6P2k/AAAAAAAAAAI/AAAAAAAAAAA/m8xhnV-G2hs/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="明報加東版新聞",
        url="plugin://plugin.video.youtube/user/MingPaoToronto"+ID5+"/",
        thumbnail="https://yt3.ggpht.com/-b-yT1RhZyc4/AAAAAAAAAAI/AAAAAAAAAAA/GQUASiScP9w/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="加國新聞-MiTV Live",
        url="plugin://plugin.video.youtube/search/?q=%e5%8a%a0%e5%9c%8b%e6%96%b0%e8%81%9e-MiTV&amp;search_type=channel"+ID6+"/",
        thumbnail="https://yt3.ggpht.com/-AMd9zheIuto/AAAAAAAAAAI/AAAAAAAAAAA/OaGtTPU3PsI/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="多倫多 WOWtv",
        url="plugin://plugin.video.youtube/channel/UC5kySUzP0p4Q4Y1rnQLX_bw"+ID7+"/",
        thumbnail="https://yt3.ggpht.com/-gYZVZ2dGwUk/AAAAAAAAAAI/AAAAAAAAAAA/5rJVdrjlPSE/s176-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
				
    plugintools.add_item( 
        #action="", 
        title="最新蕭析",
        url="plugin://plugin.video.youtube/playlist/PLPY0_ooDN1dvClKgo7K1tAS26PeAHmikd"+ID8+"/",
        thumbnail="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSaLz_W0D6UR_z8HS3vRSYAcFAmyKEIw2RBWkWku6p0YAWUKPHB5EOxXtw",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="東網直播",
        url="plugin://plugin.video.youtube/play/?video_id=WrkVwCYvRPk"+ID9+"/",
        thumbnail="https://yt3.ggpht.com/-FEbIRZGjkRc/AAAAAAAAAAI/AAAAAAAAAAA/YqZKSXZbYwU/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=False )
		
    plugintools.add_item( 
        #action="", 
        title="巴士的報",
        url="plugin://plugin.video.youtube/channel/UCCBNE0MbFaSooy7ZhJwXSrg"+ID10+"/",
        thumbnail="http://vignette2.wikia.nocookie.net/evchk/images/c/c8/1518122_130516053785319_320316523_n.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="頭條POPNews",
        url="plugin://plugin.video.youtube/user/headlinepopnews"+ID11+"/",
        thumbnail="https://yt3.ggpht.com/-gsXqCDtsVko/AAAAAAAAAAI/AAAAAAAAAAA/tHW-ABLhjuM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="頭條日報",
        url="plugin://plugin.video.youtube/user/hkheadlinenews"+ID12+"/",
        thumbnail="https://yt3.ggpht.com/-Ycjhca-2-8w/AAAAAAAAAAI/AAAAAAAAAAA/f19V5Nz5_x0/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="蘋果動新聞",
        url="plugin://plugin.video.youtube/channel/UCeqUUXaM75wrK5Aalo6UorQ"+ID13+"/",
        thumbnail="https://yt3.ggpht.com/-UnzSE4d_M1s/AAAAAAAAAAI/AAAAAAAAAAA/NeWTKNbP3TY/s240-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="壹週Plus",
        url="plugin://plugin.video.youtube/channel/UC-8CVMKt5Zlju_i07zhkC-Q"+ID14+"/",
        thumbnail="https://yt3.ggpht.com/-NfnRCKGfeao/AAAAAAAAAAI/AAAAAAAAAAA/Bp_UFIBmGoA/s240-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="E週刊",
        url="plugin://plugin.video.youtube/channel/UCeFbWIhDj_tjTOTe1P3cVHA"+ID15+"/",
        thumbnail="https://yt3.ggpht.com/-16m06v5p7I0/AAAAAAAAAAI/AAAAAAAAAAA/GYFZFRdrU88/s240-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="東Touch",
        url="plugin://plugin.video.youtube/user/EastTOUCHhk"+ID16+"/",
        thumbnail="https://yt3.ggpht.com/-2UPyDul4IZk/AAAAAAAAAAI/AAAAAAAAAAA/9sZwPI1aLm8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="東周網",
        url="plugin://plugin.video.youtube/channel/UCsTeCS6s9YoNn2kbQVAgDsQ"+ID17+"/",
        thumbnail="https://yt3.ggpht.com/-Ak12dd6RJWY/AAAAAAAAAAI/AAAAAAAAAAA/Ks4e7PCESzs/s240-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="東網電視",
        url="plugin://plugin.video.youtube/channel/UC4NjmIegGw-HyQCmxwAEZBQ"+ID18+"/",
        thumbnail="https://yt3.ggpht.com/-RaYcmdVASWQ/AAAAAAAAAAI/AAAAAAAAAAA/fSo0Yjk_GuQ/s240-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="恩雨之聲",
        url="plugin://plugin.video.youtube/channel/UCgwOhn9ghL2jY5qJEzpzSzw"+ID19+"/",
        thumbnail="https://yt3.ggpht.com/-g4j3jPE-tcg/AAAAAAAAAAI/AAAAAAAAAAA/-qthveptCm8/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="RTHK 香港電台",
        url="plugin://plugin.video.youtube/channel/UC6of7UYhctnYmqABjUqzuxw/playlists"+ID20+"/",
        thumbnail="https://yt3.ggpht.com/-56G6ZUapa8E/AAAAAAAAAAI/AAAAAAAAAAA/vU473yawuv8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
        
run()