from iview_class import *

ART = 'art-default.png'
ICON = 'icon-default.png'

def Start():
	
	Plugin.AddViewGroup('List', viewMode='List', mediaType='items')
	Plugin.AddViewGroup('InfoList', viewMode='InfoList', mediaType='items')

@handler('/video/abc', 'ABC iView', art=ART, thumb=ICON)
def MainMenu():
    
	
	oc = ObjectContainer(view_group='List', title2 = 'ABC iView')


	#oc.add(VideoClipObject(key = RTMPVideoURL(url = 'rtmp://203.18.195.10/ondemand' + '?auth=7B8F0402DD370FF9299E', clip = 'mp4:comedy/madashell_02_08', swf_url = 'http://www.abc.net.au/iview/images/iview.jpg'), rating_key = '123',title = 'TEST'))

	cats = iView_Config.List_Categories()
	
	for key in cats:
		 	
		oc.add(DirectoryObject(
				key = Callback(GetSeriesByCaegory, category=key),
				title = cats[key]
				))
	
	return oc

@route('/video/abc/series/{category}')
def GetSeriesByCaegory(category):
	
	cat = iView_Category(category)
	
	oc = ObjectContainer(view_group='List', title2 = cat.title)
	
	series = cat.series_list
	
	for item in series:

		oc.add(DirectoryObject(
				key = Callback(GetEpisodesBySeries, series=item[0]),
				title = item[1]
				))
	
	return oc
	
@route('/video/abc/episode/{series}')
def GetEpisodesBySeries(series):
	
	show = iView_Series(series)
	
	oc = ObjectContainer(view_group='InfoList', title2 = show.title)
	
	episodes = show.episodes
	
	for item in episodes:
		
		oc.add(VideoClipObject(
				key = RTMPVideoURL(url = iView_Config.RTMP_URL(), clip = iView_Config.CLIP_PATH() + item[3], swf_url = iView_Config.SWF_URL),
				title = item[1],
				summary = item[2],
				thumb = item[4],
				rating_key = item[3]
				))
	
	return oc
	

	