# -*- coding: utf-8 -*-


#Copyright [C] [Pirataqb - Ricardo Amorim Boavida]
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.




##############################################################
#Antes de mais, os melhores agradeçimentos ao staff PirataQB!#
##############################################################

import urllib
import urllib2
import re
import os
import xbmcplugin,xbmcgui,xbmc,xbmcaddon,xbmcgui



Pirataqb_Host_List = ['http://vidto.me/','http://vidzi.tv/','https://openload.co/','http://videomega.tv/']

class NoRedirection(urllib2.HTTPErrorProcessor):
   def http_response(self, request, response):
       return response
   https_response = http_response


addon = xbmcaddon.Addon('plugin.video.pirataqb')
addon_version = addon.getAddonInfo('version')
profile = xbmc.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
############################## ICONS ##########################################
icon = os.path.join(home, '\icon.png')
icon_pagina_seguinte = os.path.join(home+"\Icons\Menu",'pagseguinte.png')
icon_filmes = os.path.join(home+"\Icons\Menu",'filmes.png')
icon_filmes_HD = os.path.join(home+"\Icons\Menu",'filmeshd.png')
icon_generos = os.path.join(home+"\Icons\Menu",'generos.png')
icon_MenuGeneros_acao = os.path.join(home+"\Icons\MenuGeneros",'acao.png')
icon_MenuGeneros_aventura = os.path.join(home+"\Icons\MenuGeneros",'aventura.png')
icon_MenuGeneros_animacao = os.path.join(home+"\Icons\MenuGeneros",'animacao.png')
icon_MenuGeneros_animacaoPT = os.path.join(home+"\Icons\MenuGeneros",'animacaopt.png')
icon_MenuGeneros_biografia = os.path.join(home+"\Icons\MenuGeneros",'biografia.png')
icon_MenuGeneros_comedia = os.path.join(home+"\Icons\MenuGeneros",'comedia.png')
icon_MenuGeneros_desporto = os.path.join(home+"\Icons\MenuGeneros",'desporto.png')
icon_MenuGeneros_drama = os.path.join(home+"\Icons\MenuGeneros",'drama.png')
icon_MenuGeneros_familiar = os.path.join(home+"\Icons\MenuGeneros",'familiar.png')
icon_MenuGeneros_fantasia = os.path.join(home+"\Icons\MenuGeneros",'fantasia.png')
icon_MenuGeneros_FiccaoCientifica = os.path.join(home+"\Icons\MenuGeneros",'fica.png')
icon_MenuGeneros_guerra = os.path.join(home+"\Icons\MenuGeneros",'guerra.png')
icon_MenuGeneros_historia = os.path.join(home+"\Icons\MenuGeneros",'historia.png')
icon_MenuGeneros_misterio = os.path.join(home+"\Icons\MenuGeneros",'misterio.png')
icon_MenuGeneros_musical = os.path.join(home+"\Icons\MenuGeneros",'musical.png')
icon_MenuGeneros_PT_BR = os.path.join(home+"\Icons\MenuGeneros",'ptbr.png')
icon_MenuGeneros_romance = os.path.join(home+"\Icons\MenuGeneros",'romance.png')
icon_MenuGeneros_terror = os.path.join(home+"\Icons\MenuGeneros",'terror.png')
icon_MenuGeneros_thriller = os.path.join(home+"\Icons\MenuGeneros",'thriller.png')
icon_MenuGeneros_western = os.path.join(home+"\Icons\MenuGeneros",'western.png')
FANART = os.path.join(home, 'fanart.jpg')
###############################################################################
Progresso_File = xbmcgui.DialogProgress()

OS=os.name
if "nt" in OS:
    OS = "Windows"

if OS == "Windows":
    if len(xbmcplugin.getSetting(int(sys.argv[1]),'ntb')) > 1:
        if os.path.isfile(profile+'\DUMP') == False:
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('PirataQB', 'Caso não tenha instalado o Google Chrome, aconcelhamos que o instale para o bom funcionamento do Script.')
            file = open(profile+'\DUMP', "w")
            file.write("0")
            file.close()
        file = open(profile+'\OpenloadBrowser', "w")
        file.write(xbmcplugin.getSetting(int(sys.argv[1]),'ntb'))
        file.close()




def addon_log(string):
    xbmc.log("[addon.pirataqb-%s]: %s" %(addon_version, string))


def makeRequest(url, headers=None):
        try:
            if headers is None:
                headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
            req = urllib2.Request(url,None,headers)
            response = urllib2.urlopen(req)
            data = response.read()
            response.close()
            return data
        except urllib2.URLError, e:
            addon_log('URL: '+url)
            if hasattr(e, 'code'):
                addon_log('We failed with error code - %s.' % e.code)
                #xbmc.executebuiltin("XBMC.Notification(Pirataqb,failed with error code - "+str(e.code)+",10000,"+icon+")")
                msgbox("Erro de Ligação %s." % e.code,1000)
            elif hasattr(e, 'reason'):
                addon_log('We failed to reach a server.')
                addon_log('Reason: %s' %e.reason)
                #xbmc.executebuiltin("XBMC.Notification(Pirataqb,failed to reach the server. - "+str(e.reason)+",10000,"+icon+")")
                msgbox("Erro de Ligação %s." % e.reason,1000)


def get_params():
        param=[]
        paramstring=sys.argv[2]
        print(paramstring)
        if len(paramstring)>=2:
            params=sys.argv[2]
            cleanedparams=params
            if (params[len(params)-1]=='/'):
                params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}
            for i in range(len(pairsofparams)):
                splitparams={}
                splitparams=pairsofparams[i].split('=',1)
                for i in range(len(splitparams)):
                    if(len(splitparams))==2:
                        param[splitparams[0]]=splitparams[1]
        return param


def msgbox(texto,tempo):
    xbmc.executebuiltin("XBMC.Notification(PirataQB,"+str(texto)+","+str(tempo)+","+icon+")")

def getFilmesqb(url,pagina):
    #StaticUrl = url
    if pagina !=0:
        url +='page/'+str(pagina)+'/'
    filmes = []
    http = makeRequest(url)
    http1 = re.compile('<h1><a href="(.+?)"').findall(http)
    for i in range(len(http1)):
        filme = http1[i]
        if len(filme.split('#')) > 0:
            filme = filme.split('#')[0]
            filmes.append(filme)
    return filmes

def addLink(name,url,iconimage,ano="",folder=False,Genero="",Realizador="",Elenco="",Sipnose="",Qualidade="",Tamanho="",Duracao="",Trailer="",IMDB=""):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name ,'Trailer': "plugin://plugin.video.youtube/play/?video_id="+Trailer, "Year": ano,"Rating":IMDB , "Genre": Genero, "Director": Realizador, "Plot": "[COLOR=red]Sinop[COLOR=blue]se[/COLOR][/COLOR] : "+Sipnose+"\r\n"+"[COLOR=red]Elen[COLOR=blue]co[/COLOR][/COLOR] : "+Elenco+"\r\n"+"[COLOR=red]Quali[COLOR=blue]dade[/COLOR][/COLOR] : "+Qualidade+"\r\n"+"[COLOR=red]Tamanho [COLOR=blue]Total[/COLOR][/COLOR] : "+Tamanho+"\r\n"+"[COLOR=red]Dura[COLOR=blue]ção[/COLOR][/COLOR] : "+Duracao} )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=folder)
	return ok

def addFolder(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name} )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)
	return ok

def getLinks(urlfilme):
    # Declarar Variaveis para não serem usadas antes de existirem
    listlinks = []
    listitems =[]
    goodimage=""
    linkattached =""
    Genero=""
    Year="1900"
    Realizador=""
    Elenco=""
    IMDB=""
    Qualidade=""
    Tamanho=""
    Duracao=""
    Sipnose=""
    Trailer=""
    # Obtenção de informação Bruta
    links = makeRequest(urlfilme)
    li = re.compile('<a href="(.+?)"').findall(links)
    trailer = re.compile('<a href="(.+?)" target="_blank">').findall(links)
    info = links.split('<br>')
    titulos = re.compile('<h1 id="news-title">(.+?)</h1>').findall(links)
    imagem = re.compile('<img src="(.+?)"').findall(links)
    # ~Processamento~
    # Trailer
    for i in range(len(trailer)):
        if "https://www.youtube.com/" in trailer[i]:
            Trailer = trailer[i].split('=')[1]
    # Tentar obter infos
    for i in range(len(info)):
        moreinfo = str(info[i]).split('<b>')
        for u in range(len(moreinfo)):
            if "Ano:" in moreinfo[u]:
                bestinfo = str(moreinfo[u]).split('>')[1]
                bestinfo = str(bestinfo).split('<')[0]
                if len(bestinfo) > 1:
                    Year = bestinfo
            elif "Género:" in moreinfo[u]:
                bestinfo = str(moreinfo[u]).split('>')[1]
                bestinfo = str(bestinfo).split('<')[0]
                if len(bestinfo) > 1:
                    Genero = bestinfo
            elif "Realizador:" in moreinfo[u]:
                bestinfo = str(moreinfo[u]).split('>')[1]
                bestinfo = str(bestinfo).split('<')[0]
                if len(bestinfo) > 1:
                    Realizador = bestinfo
            elif "Elenco:" in moreinfo[u]:
                bestinfo = str(moreinfo[u]).split('>')[1]
                bestinfo = str(bestinfo).split('<')[0]
                if len(bestinfo) > 1:
                    Elenco = bestinfo
            elif "Trailer" in moreinfo[u]:
                bestinfo = moreinfo[u].split('>')
                for i in range(len(bestinfo)):
                    if "http://www.pirataqb.com/images/sinopse.png|--" in bestinfo[i]:
                        Sipnose = bestinfo[i+5].split('<')[0]
            elif "Qualidade:" in moreinfo[u]:
                bestinfo = str(moreinfo[u]).split('>')[1]
                bestinfo = str(bestinfo).split('<')[0]
                if len(bestinfo) > 1:
                    Qualidade = bestinfo
            elif "Tamanho Total:" in moreinfo[u]:
                bestinfo = str(moreinfo[u]).split('>')[1]
                bestinfo = str(bestinfo).split('<')[0]
                if len(bestinfo) > 1:
                    Tamanho = bestinfo
            elif "Duração:" in moreinfo[u]:
                bestinfo = str(moreinfo[u]).split('>')[1]
                bestinfo = str(bestinfo).split('<')[0]
                if len(bestinfo) > 1:
                    Duracao = bestinfo
            elif "." in moreinfo[u]:
                try:
                    if "/" in moreinfo[u+1]:
                            Rating = moreinfo[u].split('<')[0]
                            if "." in Rating:
                                    if len(Rating)<=4:
                                        IMDB = Rating
                except:pass
    # Obtenção de imagem
    for i in range(len(imagem)):
        if "http://" in imagem[i]:
            goodimage = imagem[i]
            break
    # Iniciar Link de Arranque.
    Title = titulos[0].decode('utf-8')
    Title = Title.replace('&','-')
    linkattached += "plugin://plugin.video.pirataqb/&#mode=19"+"&#iconimage="+goodimage+"&#name="+Title
    for i in range(len(li)):
        if li[i].startswith("http://vidzi.tv/") or li[i].startswith("http://vidto.me/") or li[i].startswith("http://videomega.tv/")or li[i].startswith("https://openload.co/"):
            if li[i].startswith("https://openload.co/"):
                if OS == "Windows":
                    listlinks.append(li[i])
            else:listlinks.append(li[i])
    # Adicionar Links com separador.
    for u in range(len(listlinks)):
        if u == 0:
            linkattached+= "&#url="+listlinks[u]
        else:linkattached+= "#"+listlinks[u]
    # Adicionar a lista para gerar icones.
    if len(listlinks) > 0:
        addLink(PirataQB_Text_Color_Engine(Title),linkattached,goodimage,Year,False,Genero,Realizador,Elenco,Sipnose,Qualidade,Tamanho,Duracao,Trailer,IMDB)
    # Adicionar item.
    return listitems

def PirataQB_Text_Color_Engine(Texto):
    string = Texto
    masterstring = "[COLOR=blue][B][I]"
    #firstpart, secondpart = string[:len(string)/2], string[len(string)/2:]
    for i in range(len(string)):
        if string[i].startswith("("):
            masterstring+= "[/I][/B][/COLOR][COLOR=red][B][I]" + string[i]
        else:masterstring+= string[i]
    masterstring+= "[/I][/B][/COLOR]"
    #final = "[COLOR=red][B][I]"+firstpart+"[/I][/B][/COLOR][COLOR=blue][B][I]"+secondpart+"[/I][/B][/COLOR]"
    return masterstring

def GetQBPage(URL,Page):
    progress = xbmcgui.DialogProgress()
    progress.create('Aguarde', 'A Carregar Lista')
    links = getFilmesqb(URL,Page)
    for i in range(len(links)):
        getLinks(links[i])
        progress.update((i*100)/len(links), "", "", "")
    progress.close()
    if test_next_page(URL,Page): # Evitar saltar para o espaço.
        addLink("[COLOR=red][B][I]página[/I][/B][/COLOR] [COLOR=blue][B][I]seguinte[/I][/B][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&URL="+URL+"&movies_pos="+str(int(Page)+1),icon_pagina_seguinte,"2015",True)

def PirataQB_Resolver(url):
    resolved_url=None
    for i in range(len(Pirataqb_Host_List)):
        if Pirataqb_Host_List[i] in url:
            if "http://vidto.me/" in url:
                from resources.lib.resolvers import vidto
                resolved_url = vidto.resolve(url)
                break
            elif "http://vidzi.tv/" in url:
                import urlresolver
                resolved_url = urlresolver.resolve(url)
                break
            elif "https://openload.co/" in url:
                import urlresolver
                Progresso_File.update(50, "", "Iremos lançar uma janela de browser para obter o link desejado.", "")
                xbmc.sleep(3000)
                resolved_url = resolving_OpenLoad(url)
                break
            elif "http://videomega.tv/" in url:
                from resources.lib.resolvers import videomega
                resolved_url = videomega.resolve(url)
                break
    return resolved_url
########################################################################################################################
#def ask_Resolved_Openload(url):
#    headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
#    req = urllib2.Request("http://localhost:81/index.py?_Webtest_"+url,None,headers)
#    response = urllib2.urlopen(req)
#    data = ""
#    while not len(data) > 1 :
#        try:
#                data = response.read()
#        except:pass
#    response.close()
#    data = data.split(':')[1] + ":" +data.split(':')[2]
#    data = data.split('<')[0]
#    return data
########################################################################################################################

def resolving_OpenLoad(url):
    #UNDER GNU By Ricardo Boavida (Windows-Linux-MacOSX)
    from selenium import webdriver
    file = open(profile+'\OpenloadBrowser', 'r')
    BO = file.readline()
    if "Mozilla Firefox" in BO:
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        ffprofile = webdriver.FirefoxProfile()
        ffprofile.add_extension(extension=home+'\selenium\webdriver\_adblock_plus.xpi')
        binary = FirefoxBinary(home+"\selenium\webdriver\Mozilla Firefox\_firefox.exe")#'C:\Python27\Mozilla Firefox\Firefox.exe')
        browser = webdriver.Firefox(firefox_profile=ffprofile,firefox_binary=binary) #
    elif "Google Chrome" in BO:
        chop = webdriver.ChromeOptions()
        chop.add_extension(home+"\selenium\webdriver\chrome\Wadblockplus.crx")
        browser = webdriver.Chrome(home+"\selenium\webdriver\chrome\chromedriver.exe",chrome_options = chop, service_args=["--verbose",'--log-path='+home+'\selenium\webdriver\chrome\chromedriver_log.txt'])
    browser.set_window_size(0, 0)
    browser.get(url) # Load page
    browser.set_window_size(0, 0)
    browser.find_element_by_id('mediaspace_wrapper').click()
    browser.set_window_size(0, 0)
    xbmc.sleep(1000)
    li = re.compile('src="(.+?)"').findall(browser.page_source.encode("utf-8"))
    for i in range(len(li)):
        if li[i].startswith("https://openload"):
            MasterURL = li[i].split('?')[0]
    browser.quit()
    return MasterURL

def test_next_page(Url,Page):
    Pagina = Page
    Bool = False
    Gurl = Url
    if Page !=0:
        Gurl +='page/'+str(Page)+'/'
    page = makeRequest(Gurl)
    http1 = re.compile('<a href="(.+?)"').findall(page)
    for i in range(len(http1)):
        if Url in http1[i]:
            if str(int(Pagina+1)) in http1[i]:
                Bool = True
                break
            else:Bool = False
    return Bool

def Select_Link(Link):
    fastlinks = []
    fastnames = []
    link = str(Link.encode('utf-8'))

    if "#" in link:
        sp = Link.encode('utf-8').split('#') # Partir Link por (#)
        for i in range(len(sp)):
            fast = str(sp[i])
            fast = fast.replace(";", "", 10)
            if fast.startswith("http://vidzi.tv/"): # Verificar o nome a Por
                fast += "*Vidzi.tv"
            elif fast.startswith("http://vidto.me/"):
                fast += "*Vidto.me"
            elif fast.startswith("http://videomega.tv/"):
                fast += "*VideoMega [COLOR=gold](HD)[/COLOR]"
            elif fast.startswith("https://openload.co/"):
                fast += "*OpenLoad.co [COLOR=gold](HD)[/COLOR]"
            fastlinks.append(str(fast))
        for i in range(len(fastlinks)):
            if "*" in fastlinks[i]:
                fastnames.append(fastlinks[i].split('*')[1]) # Mostar apenas nomes
        dialog = xbmcgui.Dialog()
        quest = dialog.select('Escolha o Link : ', fastnames)
        for i in range(len(fastlinks)):
            if quest ==-1:
                mode=None
                url=""
            elif quest == i:
                url = str(fastlinks[i].split('*')[0]) # Selecionar o Link
    return url

def Set_Vista(Nome):
    if Nome == "Miniatura":
        xbmc.executebuiltin("Container.SetViewMode(500)")
    elif Nome == "Amplo":
        xbmc.executebuiltin("Container.SetViewMode(505)")
    elif Nome == "Lista Grande":
        xbmc.executebuiltin("Container.SetViewMode(51)")
    elif Nome == "Lista":
        xbmc.executebuiltin("Container.SetViewMode(1)")

try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_DATE)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_GENRE)
except:
    pass


params=get_params()

url=None
name=None
mode=None
playlist=None
iconimage=None
fanart=FANART
playlist=None
fav_mode=None
regexs=None
legenda=None
Movies_Pos=None
SelectionURL=None


try:
    url=urllib.unquote_plus(params["#url"]).decode('utf-8')
except:
    pass
try:
    Movies_Pos=urllib.unquote_plus(params["#movies_pos"]).decode('utf-8')
except:
    pass
try:
    Movies_Pos=urllib.unquote_plus(params["movies_pos"]).decode('utf-8')
except:
    pass
try:
    name=urllib.unquote_plus(params["#name"])
except:
    pass
try:
    iconimage=urllib.unquote_plus(params["#iconimage"]).decode('utf-8')
except:
    pass
try:
    mode=int(params["mode"])
except:
    pass
try:
    mode=int(params["#mode"])
except:
    pass
try:
    SelectionURL=urllib.unquote_plus(params["URL"]).decode('utf-8')
except:
    pass
try:
    SelectionURL=urllib.unquote_plus(params["#URL"]).decode('utf-8')
except:
    pass


if Movies_Pos is None or Movies_Pos <= 1:
    Movies_Pos=1

if not url is None:
    url = Select_Link(url)
    if url == "":
        mode=None

if mode==None: # Menu
    addFolder("Filmes","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes/",icon_filmes)
    addFolder("Filmes HD","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-hd/",icon_filmes_HD)
    addFolder("Generos","plugin://plugin.video.pirataqb/&#mode=2",icon_generos)

elif mode==1: # Pesquisar
    GetQBPage(SelectionURL,int(Movies_Pos))

elif mode==2: # Separador Generos
    addFolder("[COLOR=red]Aç[COLOR=blue]ão[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/acao/",icon_MenuGeneros_acao)
    addFolder("[COLOR=red]Aven[COLOR=blue]tura[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/aventura/",icon_MenuGeneros_aventura)
    addFolder("[COLOR=red]Ani[COLOR=blue]mação[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/animacao/",icon_MenuGeneros_animacao)
    addFolder("[COLOR=red]Ani[COLOR=blue]mação (PT-PT)[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/animacao-em-portugues/",icon_MenuGeneros_animacaoPT)
    addFolder("[COLOR=red]Bio[COLOR=blue]grafia[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/biografia/",icon_MenuGeneros_biografia)
    addFolder("[COLOR=red]Comé[COLOR=blue]dia[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/comedia/",icon_MenuGeneros_comedia)
    addFolder("[COLOR=red]Cri[COLOR=blue]me[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/crime/",icon_MenuGeneros_comedia)
    addFolder("[COLOR=red]Des[COLOR=blue]porto[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/desporto/",icon_MenuGeneros_desporto)
    addFolder("[COLOR=red]Docu[COLOR=blue]mentário[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/documentario/",icon_MenuGeneros_desporto)
    addFolder("[COLOR=red]Dra[COLOR=blue]ma[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/drama/",icon_MenuGeneros_drama)
    addFolder("[COLOR=red]Fami[COLOR=blue]liar[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/familiar/",icon_MenuGeneros_familiar)
    addFolder("[COLOR=red]Fan[COLOR=blue]tasia[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/fantasia/",icon_MenuGeneros_fantasia)
    addFolder("[COLOR=red]Gue[COLOR=blue]rra[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/guerra/",icon_MenuGeneros_guerra)
    addFolder("[COLOR=red]Histó[COLOR=blue]ria[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/historia/",icon_MenuGeneros_historia)
    addFolder("[COLOR=red]Misté[COLOR=blue]rio[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/misterio/",icon_MenuGeneros_misterio)
    addFolder("[COLOR=red]Musi[COLOR=blue]cal[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/musical/",icon_MenuGeneros_musical)
    addFolder("[COLOR=red]Portu[COLOR=blue]gês - Brasileiro[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/portugues-brasileiro/",icon_MenuGeneros_PT_BR)
    addFolder("[COLOR=red]Roman[COLOR=blue]ce[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/romance/",icon_MenuGeneros_romance)
    addFolder("[COLOR=red]Te[COLOR=blue]rror[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/terror/",icon_MenuGeneros_terror)
    addFolder("[COLOR=red]Thri[COLOR=blue]ller[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/thriller/",icon_MenuGeneros_thriller)
    addFolder("[COLOR=red]Wes[COLOR=blue]tern[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/generos/western/",icon_MenuGeneros_western)

elif mode==19: # Reproduzir
    Progresso_File.create('Aguarde', 'A Processar o Link.')
    xbmc.sleep(1000)
    resolved = PirataQB_Resolver(url)
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    listitem = xbmcgui.ListItem( label = str(PirataQB_Text_Color_Engine(name)), iconImage =str(iconimage), thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ), path=str(resolved))
    Progresso_File.update(75, "", "A Equipa [COLOR=red][B]Pirata[/B][/COLOR][COLOR=blue]qb[/COLOR] deseja-lhe uma boa sessão!", "")
    xbmc.sleep(3000)
    xbmc.Player().play(str(resolved),listitem)
    Progresso_File.close()

Set_Vista(xbmcplugin.getSetting(int(sys.argv[1]),'Tp Vista'))
xbmcplugin.endOfDirectory(int(sys.argv[1]))