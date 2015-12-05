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


## By Strings but Working =D

import urllib
import urllib2
import re
import os
import xbmcplugin,xbmcgui,xbmc,xbmcaddon,xbmcgui,requests,cookielib

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
icon_MenuGeneros_crime = os.path.join(home+"\Icons\MenuGeneros",'crime.png')
icon_MenuGeneros_desporto = os.path.join(home+"\Icons\MenuGeneros",'desporto.png')
icon_MenuGeneros_documentario = os.path.join(home+"\Icons\MenuGeneros",'documentario.png')
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

Sleep_Time = (int(addon.getSetting('sleep')) * 1000)
Openload_Browser = addon.getSetting('ntb')

OS=os.name
if "nt" in OS:
    OS = "Windows"


if os.path.isdir(profile+'/DUMP') == False:
    os.mkdir(profile+'/DUMP')

if OS == "Windows":
    if len(xbmcplugin.getSetting(int(sys.argv[1]),'ntb')) > 1:
        if os.path.isfile(profile+'/DUMP/DUMP') == False and "Google Chrome" in Openload_Browser:
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('PirataQB '+addon_version, 'Caso não tenha instalado o Browser Predefenido, aconcelhamos que o instale para o bom funcionamento do Script.')
            file = open(profile+'/DUMP/DUMP', "w")
            file.write("0")
            file.close()

if os.path.isfile(profile+'/DUMP/WELCOME') == False:
    file = open(home+'/README.txt', "r")
    content = file.read()
    dialog = xbmcgui.Dialog()
    ok = dialog.ok('PirataQB '+addon_version,content.decode('utf-8'))
    file = open(profile+'/DUMP/WELCOME',"w")
    file.write("0")
    file.close()

if os.path.isfile(profile+'/DUMP/DUMPMSG_V'+addon_version) == False:
    file = open(home+'/changelog.txt', "r")
    content = file.read()
    dialog = xbmcgui.Dialog()
    ok = dialog.ok('PirataQB '+addon_version,content.decode('utf-8'))
    file = open(profile+'/DUMP/DUMPMSG_V'+addon_version, "w")
    file.write("0")
    file.close()









def addon_log(string):
    xbmc.log("[addon.pirataqb-%s]: %s" %(addon_version, string))


def Save_Search(Search):
    file = open(profile+'/DUMP/SAVE_SEARCH',"w")
    file.write(Search)
    file.close()

def Load_Search():
    if os.path.isfile(profile+'/DUMP/SAVE_SEARCH') == True:
        file = open(profile+'/DUMP/SAVE_SEARCH', "r")
        content = file.read()
        if len(content) > 0:return content
        else:return ""
    else:return ""



def Download_File(URL,Name,Profile_Dir=True):
    import urllib2
    url = URL
    file_name = Name
    u = urllib2.urlopen(url)
    f = open(profile+'\\'+ file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = (file_size_dl * 100 / file_size)
        Progresso_File.update(int(status), "", "A descarregar "+Name+" ...", "")
    f.close()

def Extract_Zip(File_Name,Delete_Original=True,Profile_Dir=True):
    import zipfile
    path = profile+'\\'+ File_Name
    with zipfile.ZipFile(path, "r") as z:
        z.extractall(profile+"\\")
    if Delete_Original == True:
        os.remove(path)



def makeRequest(url, headers=None,wait=0):
    try:
        if headers is None:
            headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        if wait <> 0 :
            data = response.read()
        else:
            xbmc.sleep(wait)
            data = response.read()
        response.close()
        return data
    except:
        msgbox("Erro na ligação ao servidor",3000)
        return ""


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



def Pesquisa_De_Filmes(Filme,Pagina):
    #if Series == False:
    Url_Pesquisa ='http://www.pirataqb.com/index.php?story={'+Filme+'}&catlist[]=2&catlist[]=14&search_start='+str(Pagina)+'&do=search&subaction=search'
 #Séries   #else:Url_Pesquisa ='http://www.pirataqb.com/index.php?story={'+Filme+'}&catlist[]=26&catlist[]=30&search_start='+str(Pagina)+'&do=search&subaction=search'

    # Fazer Lista de Filmes com este Link
    Pedido = makeRequest(Url_Pesquisa,None,3000)
    Info =  Pedido.split('<h1>')
    Testing = re.compile('<div class="searsh_mess">(.+?)</div>').findall(Pedido)
    print(str(Testing))
    progress = xbmcgui.DialogProgress()
    progress.create('A Carregar', '')
    for i in range(len(Info)):
        if '<a href="' in Info[i]:
            End = Info[i].split('</h1>')[0]
            if ".html" in End:
                if '"' in End:
                    Titulo = End
                    Titulo = Titulo.split('>')[1]
                    Titulo = Titulo.split('<')[0]
                    End = End.split('"')[1]
                    End = End.split('"')[0]
                    progress.update(0,"A inserir : "+PirataQB_Text_Color_Engine(Titulo))
                    Info_By_Link(End)
    Paginas = Pedido.split('<div class="maincont" align="center">')
    for u in range(len(Paginas)):
        if "</div>" in Paginas[u]:
            Info = Paginas[u].split('</div>')[0]
            Real_Paginas = re.compile('href="#">(.+?)</a>').findall(Info)
            for i in range(len(Real_Paginas)):
                if Real_Paginas[i].startswith(str(int(Pagina)+1)):
                    addFolder("Próxima Página","plugin://plugin.video.pirataqb/&#mode=3"+"&#name="+Filme+"&#pagina="+str(int(Pagina)+1),icon_pagina_seguinte)


def Info_By_Link(urlfilme):
    File_Name = "" # For SUBS
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
    print("TITULOS : "+str(titulos))
    imagem = re.compile('<img src="(.+?)"').findall(links)
    try:
        real_name = links.split('<!--/colorstart-->')[1]
        File_Name = real_name.split('<!--colorend-->')[0]
    except:File_Name=""
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
    Title = Title + "%" + File_Name.decode('utf-8')
    linkattached += "plugin://plugin.video.pirataqb/&#mode=19"+"&#iconimage="+goodimage+"&#name="+Title
    for i in range(len(li)):
        if li[i].startswith("http://vidzi.tv/") or li[i].startswith("http://vidto.me/") or li[i].startswith("http://videomega.tv/")or li[i].startswith("https://openload.co/"):
            listlinks.append(li[i])
        else:pass
    # Adicionar Links com separador.
    for u in range(len(listlinks)):
        if u == 0:
            linkattached+= "&#url="+listlinks[u]
        else:linkattached+= "#"+listlinks[u]
    # Adicionar a lista para gerar icones.
    if len(listlinks) > 0:
        addLink(PirataQB_Text_Color_Engine(Title.split('%')[0]),linkattached,goodimage,Year,False,Genero,Realizador,Elenco,Sipnose,Qualidade,Tamanho,Duracao,Trailer,IMDB)
    # Adicionar item.
    return listitems

########################################################################################################################

def getSeriesqb(url,pagina):
    if pagina !=0:
            url +='page/'+str(pagina)+'/'
    Realizador=""
    linkattached =""
    Imagem=""
    Nome_Real=""
    Year=""
    Genero=""
    Elenco=""
    Sipnose=""
    Qualidade=""
    Tamanho=""
    Duracao=""
    Youtube_Trailer=""
    Titulo_Real=""
    IMDB=""
    http = makeRequest(url)
    Splited_to_Get_Link = http.split('<template class="cover-preview-content">')
    for i in range(len(Splited_to_Get_Link)):
        print(Splited_to_Get_Link[i])
        Counter = 0
        BruteInfo = Splited_to_Get_Link[i]
        Preterit_Info = BruteInfo.split('\r\n')
        for i in range(len(Preterit_Info)):
            if '<div style="' in Preterit_Info[i]:
                #print(Preterit_Info[i])
                Titulo = re.compile('title="(.+?)"').findall(Preterit_Info[i])
                Nome = re.compile('<!--/colorstart-->(.+?)<!--colorend-->').findall(Preterit_Info[i])
                IMDB_R = re.compile('<br /><b>(.+?)</b> / 10<br />').findall(Preterit_Info[i])
                _Ano = re.compile('<b>Ano:</b>(.+?)<br />').findall(Preterit_Info[i])
                _Duracao_e_Tamanho = re.compile('<br /><b>Tamanho Total:</b>(.+?)<br /><b>Duração:</b>(.+?)<br />').findall(Preterit_Info[i])
                _Qalidade = re.compile('<br /><b>Qualidade:</b>(.+?)<br />').findall(Preterit_Info[i])
                _Genero = re.compile('<br /><b>Género:</b>(.+?)<br />').findall(Preterit_Info[i])
                _Elenco_Realizacao = re.compile('<b>Realizador:</b>(.+?)<br /><b>Elenco:</b>(.+?)<br /><br />').findall(Preterit_Info[i])
                _Sipnose = re.compile('<img src="/images/sinopse.png" alt="(.+?)" title="(.+?)"  /><!--dle_image_end--><br /><br />(.+?)<br /><br />').findall(Preterit_Info[i])
                for i in range(len(_Sipnose)):
                    for u in range(len(_Sipnose[i])):
                        if u == 2: Sipnose = _Sipnose[i][u]
                for i in range(len(_Elenco_Realizacao)):
                    for u in range(len(_Elenco_Realizacao[i])):
                        if u == 0:Realizador= _Elenco_Realizacao[i][u]
                        else:Elenco= _Elenco_Realizacao[i][u]
                for i in range(len(_Genero)):
                    Genero = _Genero[i]
                for i in range(len(_Qalidade)):
                    Qualidade = _Qalidade[i]
                for i in range(len(_Duracao_e_Tamanho)):
                    for u in range(len(_Duracao_e_Tamanho[i])):
                        if u ==0:Tamanho = _Duracao_e_Tamanho[i][u]
                        else:Duracao = _Duracao_e_Tamanho[i][u]
                for i in range(len(_Ano)):
                    Year = _Ano[i]
                for a in range(len(IMDB_R)):
                    IMDB = IMDB_R[a]
                    break
                for z in  range(len(Nome)):
                    Nome_Real = Nome[z]
                    break
                for t in range(len(Titulo)):
                    Titulo_Real = Titulo[t]
                    print("Your Mega Title : "+Titulo[t])
                #try:Titulo_Real = str(Titulo[0])
                #except:Titulo_Real = "Name_Problems"
                Titulo_Real = Titulo_Real.replace('amp;','')
                Titulo_Real = Titulo_Real.replace('&','-')
                Imagem = re.compile('<img src="(.+?)"').findall(Preterit_Info[i])
                Image = Imagem[0]
                linkattached = "plugin://plugin.video.pirataqb/&#mode=72"+"&#iconimage="+Image+"&#name="+Titulo_Real
                Links_By_Episode = Preterit_Info[i].split('Episódio')
                for r in range(len(Links_By_Episode)):
                    Numero_Episodio = Links_By_Episode[r].split('<')[0]
                    Numero_Episodio = Numero_Episodio.replace(' ','')
                    Numero_Episodio = Numero_Episodio.replace('\r\n','')
                    try:
                  ###################### EP 0X #################################################################
                        if int(Numero_Episodio) >= 0:
                            if int(Numero_Episodio) < 10:
                                Temporada = Nome_Real.split('.')
                                Real_Real_Nome = ""
                                for v in range(len(Temporada)-1):
                                    if "S" in Temporada[v]:
                                        Temporada[v] = Temporada[v] + "E0" + Numero_Episodio
                                    Real_Real_Nome +=Temporada[v] + " "
                            else:
                                Temporada = Nome_Real.split('.')
                                Real_Real_Nome = ""
                                for v in range(len(Temporada)-1):
                                    if "S" in Temporada[v]:
                                        Temporada[v] = Temporada[v] + "E" + Numero_Episodio
                                    Real_Real_Nome +=Temporada[v] + " "
                  ######################## EP XX #################################################################
                            if Counter == 0:linkattached += "&#episodios="+"*"+str(Numero_Episodio)
                            else:linkattached += "*" + str(Numero_Episodio)
                            Counter += 1
                            Lista_de_Links = []
                            Links_Serie = re.compile('<a href="(.+?)" target="_blank">').findall(Links_By_Episode[r])
                            for y in range(len(Links_Serie)):
                                Link = Links_Serie[y]
                                if Link.startswith("http://vidzi.tv/") or Link.startswith("http://vidto.me/") or Link.startswith("http://videomega.tv/")or Link.startswith("https://openload.co/"):
                                    Lista_de_Links.append(Link)
                            for u in range(len(Lista_de_Links)):
                                if u == 0:linkattached+= "$#url="+Lista_de_Links[u]
                                else:linkattached+= "#"+Lista_de_Links[u]
                            linkattached+= "%" + Real_Real_Nome
                    except:pass
                if "url=" and "episodios=" in linkattached:
                    addFolder(Titulo_Real.split('%')[0],linkattached,Image,"",True,Genero,Realizador,Elenco,Sipnose,Qualidade,Tamanho,Duracao,Youtube_Trailer,IMDB)

def getFilmesqb(url,pagina):
        if pagina !=0:
            url +='page/'+str(pagina)+'/'
        Realizador=""
        Imagem=""
        Nome_Real=""
        Year=""
        Genero=""
        Elenco=""
        Sipnose=""
        Qualidade=""
        Tamanho=""
        Duracao=""
        Youtube_Trailer=""
        Titulo_Real=""
        IMDB=""
        http = makeRequest(url)
        Splited_to_Get_Link = http.split('<template class="cover-preview-content">')
        for i in range(len(Splited_to_Get_Link)):
            print(Splited_to_Get_Link[i])
            Lista_de_Links = []
            BruteInfo = Splited_to_Get_Link[i]
            _Links = re.compile('<a href="(.+?)"').findall(BruteInfo)
            _RealName = re.compile('<!--/colorstart-->(.+?)<!--colorend-->').findall(BruteInfo)
            _Titulo = re.compile('<img src="(.+?)" alt="(.+?)" title="(.+?)"  />').findall(BruteInfo)
            _Ano = re.compile('<b>Ano:</b>(.+?)<br />').findall(BruteInfo)
            _Ranking_IMDB = re.compile('<br /><b>(.+?)</b> / 10<br />').findall(BruteInfo)
            _Duracao_e_Tamanho = re.compile('<br /><b>Tamanho Total:</b>(.+?)<br /><b>Duração:</b>(.+?)<br />').findall(BruteInfo)
            _Qalidade = re.compile('<br /><b>Qualidade:</b>(.+?)<br />').findall(BruteInfo)
            _Genero = re.compile('<br /><b>Género:</b>(.+?)<br />').findall(BruteInfo)
            _Elenco_Realizacao = re.compile('<b>Realizador:</b>(.+?)<br /><b>Elenco:</b>(.+?)<br /><br />').findall(BruteInfo)
            _Sipnose = re.compile('<img src="/images/sinopse.png" alt="(.+?)" title="(.+?)"  /><!--dle_image_end--><br /><br />(.+?)<br /><br />').findall(BruteInfo)
            for i in range(len(_Sipnose)):
                for u in range(len(_Sipnose[i])):
                    if u == 2: Sipnose = _Sipnose[i][u]
            for i in range(len(_Elenco_Realizacao)):
                for u in range(len(_Elenco_Realizacao[i])):
                    if u == 0:Realizador= _Elenco_Realizacao[i][u]
                    else:Elenco= _Elenco_Realizacao[i][u]
            for i in range(len(_Genero)):
                Genero = _Genero[i]
            for i in range(len(_Qalidade)):
                Qualidade = _Qalidade[i]
            for i in range(len(_Duracao_e_Tamanho)):
                for u in range(len(_Duracao_e_Tamanho[i])):
                    if u ==0:Tamanho = _Duracao_e_Tamanho[i][u]
                    else:Duracao = _Duracao_e_Tamanho[i][u]
            for i in range(len(_Ranking_IMDB)):
                IMDB = _Ranking_IMDB[i]
            for i in range(len(_Ano)):
                Year = _Ano[i]
            for i in range(len(_Titulo)):
                for u in range(len(_Titulo[i])):
                    if u == 0:
                        Imagem = _Titulo[i][u]
                    if u > 0 :
                        Titulo_Real = _Titulo[i][u]
                        Titulo_Real = Titulo_Real.replace('amp;','')
                        Titulo_Real = Titulo_Real.replace('&','-')
                        break
                if len(Titulo_Real) > 0:
                    break
            for i in range(len(_RealName)):
                Nome_Real = _RealName[i]
                break
            Titulo_Real = Titulo_Real.replace('&','-')
            Titulo_Real = Titulo_Real + "%" + Nome_Real
            for i in range(len(_Links)):
                    Links_Corretos = _Links[i]
                    if "http://www.imdb.com/" in Links_Corretos:
                       IMDB_Link = Links_Corretos
                    elif "https://www.youtube.com/" in Links_Corretos:
                        Youtube_Trailer = Links_Corretos
                        Youtube_Trailer = Youtube_Trailer.split('=')[1]
                    elif "http://vidto.me/" in Links_Corretos:
                        Vidto_Link = Links_Corretos
                        Lista_de_Links.append(Vidto_Link)
                    elif "http://vidzi.tv/" in Links_Corretos:
                        Vidzi_Link = Links_Corretos
                        Lista_de_Links.append(Vidzi_Link)
                    elif "https://openload.co/" in Links_Corretos:
                        Openload_Link = Links_Corretos
                        Lista_de_Links.append(Openload_Link)
                    elif "http://videomega.tv/" in Links_Corretos:
                        Videomega_Link = Links_Corretos
                        Lista_de_Links.append(Videomega_Link)
            linkattached = "plugin://plugin.video.pirataqb/&#mode=19"+"&#iconimage="+Imagem+"&#name="+Titulo_Real
            for u in range(len(Lista_de_Links)):
                if u == 0:linkattached+= "&#url="+Lista_de_Links[u]
                else:linkattached+= "#"+Lista_de_Links[u]
            if len(Titulo_Real) >= 2:
                addLink(PirataQB_Text_Color_Engine(Titulo_Real.split('%')[0]),linkattached,Imagem,Year,False,Genero,Realizador,Elenco,Sipnose,Qualidade,Tamanho,Duracao,Youtube_Trailer,IMDB)
        return Splited_to_Get_Link


def addLink(name,url,iconimage,ano="",folder=False,Genero="",Realizador="",Elenco="",Sipnose="",Qualidade="",Tamanho="",Duracao="",Trailer="",IMDB=""):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name ,'Trailer': "plugin://plugin.video.youtube/play/?video_id="+Trailer, "Year": ano,"Rating":IMDB , "Genre": Genero, "Director": Realizador, "Plot": "[COLOR=red]Sinop[COLOR=blue]se[/COLOR][/COLOR] : "+Sipnose+"\r\n"+"[COLOR=red]Elen[COLOR=blue]co[/COLOR][/COLOR] : "+Elenco+"\r\n"+"[COLOR=red]Quali[COLOR=blue]dade[/COLOR][/COLOR] : "+Qualidade+"\r\n"+"[COLOR=red]Tamanho [COLOR=blue]Total[/COLOR][/COLOR] : "+Tamanho+"\r\n"+"[COLOR=red]Dura[COLOR=blue]ção[/COLOR][/COLOR] : "+Duracao} )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=folder)
	return ok

def addFolder(name,url,iconimage,ano="",folder=False,Genero="",Realizador="",Elenco="",Sipnose="",Qualidade="",Tamanho="",Duracao="",Trailer="",IMDB=""):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name ,'Trailer': "plugin://plugin.video.youtube/play/?video_id="+Trailer, "Year": ano,"Rating":IMDB , "Genre": Genero, "Director": Realizador, "Plot": "[COLOR=red]Sinop[COLOR=blue]se[/COLOR][/COLOR] : "+Sipnose+"\r\n"+"[COLOR=red]Elen[COLOR=blue]co[/COLOR][/COLOR] : "+Elenco+"\r\n"+"[COLOR=red]Quali[COLOR=blue]dade[/COLOR][/COLOR] : "+Qualidade+"\r\n"+"[COLOR=red]Tamanho [COLOR=blue]Total[/COLOR][/COLOR] : "+Tamanho+"\r\n"+"[COLOR=red]Dura[COLOR=blue]ção[/COLOR][/COLOR] : "+Duracao} )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)
	return ok

def PirataQB_Text_Color_Engine(Texto):
    string = Texto
    masterstring = "[COLOR=blue][B][I]"
    for i in range(len(string)):
        if string[i].startswith("("):
            masterstring+= "[/I][/B][/COLOR][COLOR=red][B][I]" + string[i]
        else:masterstring+= string[i]
    masterstring+= "[/I][/B][/COLOR]"
    return masterstring

def GetQBPage(URL,Page):
    if Page <= 0:
        Page = 1
    FixedPage = Page
    PageCounter = 1
    progress = xbmcgui.DialogProgress()
    progress.create('Aguarde', '')
    Actual = 0
    PagesLoaded = int(addon.getSetting("paginas"))
    for Counter in range(Page,Page+PagesLoaded):
        Page = Counter
        links = getFilmesqb(URL,Page)
        for i in range(len(links)):
            Percentage = ((Actual*100)*PagesLoaded/(len(links)*PagesLoaded)/PagesLoaded)
            if PagesLoaded > 1:progress.update(Percentage,"                                                 Página : [COLOR=blue]"+str(int(PageCounter))+"[/COLOR]/[COLOR=red]"+str(PagesLoaded)+"[/COLOR]","                             Estamos a verificar a Página : [COLOR=blue]"+str(Page)+"[/COLOR]", "")
            else:progress.update(Percentage, "                             Estamos a verificar a Página : [COLOR=blue]"+str(Page)+"[/COLOR]","", "")
            Actual += 1
        PageCounter += 1
        try:
            if test_next_page(URL,Page) == False:
                break
        except:pass
    progress.close()
    if test_next_page(URL,Page): # Evitar saltar para o espaço.
        addLink("[COLOR=red][B][I]página[/I][/B][/COLOR] [COLOR=blue][B][I]seguinte[/I][/B][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&URL="+URL+"&movies_pos="+str(int(FixedPage+PagesLoaded)),icon_pagina_seguinte,"2015",True)

def PirataQB_Resolver(url):
    resolved_url=None
    for i in range(len(Pirataqb_Host_List)):
        if Pirataqb_Host_List[i] in url:
            if "http://vidto.me/" in url:
                try:
                    from resources.lib.resolvers import vidto
                    resolved_url = vidto.resolve(url)
                except:
                    import urlresolver
                    resolved_url = urlresolver.resolve(url)
            elif "http://vidzi.tv/" in url:
                try:
                    import urlresolver
                    resolved_url = urlresolver.resolve(url)
                except:
                    import urlresolver
                    from resources.lib.resolvers import vidzi
                    resolved_url = vidzi.resolve(url)
            elif "https://openload.co/" in url:
                import urlresolver
                from resources.lib.resolvers import openload
                resolved_url=""
                try:
                    resolved_url = openload.resolve(url)
                except:
                    if len(resolved_url) <= 1 and OS == "Windows":
                        Progresso_File.update(50, "", "Iremos lançar uma janela de browser para obter o link desejado.", "")
                        xbmc.sleep(Sleep_Time)
                        resolved_url = resolving_OpenLoad(url)
            elif "http://videomega.tv/" in url:
                import urlresolver
                from resources.lib.resolvers import videomega
                try:resolved_url = urlresolver.resolve(url)
                except:resolved_url = videomega.resolve(url)
    return resolved_url

def resolving_OpenLoad(url):
    #UNDER GNU By Ricardo Boavida (Windows)
    from selenium import webdriver
    if "Mozilla Firefox" in Openload_Browser:
        if os.path.isfile(profile+"\Mozilla Firefox\_firefox.exe") == False:
            Download_File("https://raw.githubusercontent.com/pirataqb/PirataQB-Repo/master/Mozilla%20Firefox.zip","Mozilla Firefox.zip")
            Extract_Zip("Mozilla Firefox.zip")
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        ffprofile = webdriver.FirefoxProfile()
        ffprofile.add_extension(extension=home+'\selenium\webdriver\_adblock_plus.xpi')
        binary = FirefoxBinary(profile+"\Mozilla Firefox\_firefox.exe")
        browser = webdriver.Firefox(firefox_profile=ffprofile,firefox_binary=binary)
    elif "Google Chrome" in Openload_Browser:
        chop = webdriver.ChromeOptions()
        chop.add_extension(home+"\selenium\webdriver\chrome\Wadblockplus.crx")
        browser = webdriver.Chrome(home+"\selenium\webdriver\chrome\chromedriver.exe",chrome_options = chop, service_args=["--verbose",'--log-path='+home+'\selenium\webdriver\chrome\chromedriver_log.txt'])
    browser.set_window_size(0, 0)
    browser.get(url) # Load page
    xbmc.sleep(Sleep_Time)
    browser.set_window_size(0, 0)
    browser.find_element_by_id('mediaspace_wrapper').click()
    browser.set_window_size(0, 0)
    xbmc.sleep(Sleep_Time)
    li = re.compile('src="(.+?)"').findall(browser.page_source.encode("utf-8"))
    for i in range(len(li)):
        if li[i].startswith("https://openload"):
            MasterURL = li[i]
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

def Menu_Inicial():
    addFolder("Menu Filmes","plugin://plugin.video.pirataqb/&#mode=5",icon_filmes)
    addFolder("Menu Séries","plugin://plugin.video.pirataqb/&#mode=6",icon_filmes_HD)

def Menu_Filmes():
    addFolder("Filmes","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/",icon_filmes)
    #addFolder("Séries_Trial","plugin://plugin.video.pirataqb/&#mode=4&movies_pos=1&URL=http://www.pirataqb.com/series-online/",icon_filmes_HD)
    addFolder("Generos","plugin://plugin.video.pirataqb/&#mode=2",icon_generos)
    addFolder("Pesquisa","plugin://plugin.video.pirataqb/&#mode=3",icon_generos)

def Menu_Series():
    #addFolder("Filmes","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/",icon_filmes)
    addFolder("Séries","plugin://plugin.video.pirataqb/&#mode=4&movies_pos=1&URL=http://www.pirataqb.com/series-online/",icon_filmes_HD)
    #addFolder("Pesquisa de Séries","plugin://plugin.video.pirataqb/&#mode=30",icon_generos)

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

print("PARAMS : "+str(params))

url=None
name=None
mode=None
playlist=None
iconimage=None
fanart=FANART
playlist=None
fav_mode=None
regexs=None
Movies_Pos=None
SelectionURL=None

Subs=""

pagina=""

Episodios=None

try:
    url=urllib.unquote_plus(params["#url"]).decode('utf-8')
except:
    pass
try:
    Episodios=urllib.unquote_plus(params["#%23episodios"]).decode('utf-8')
except:
    pass
try:
    Links_Serie=urllib.unquote_plus(params["#links_serie"]).decode('utf-8')
except:
    pass
try:
    Movies_Pos=urllib.unquote_plus(params["#movies_pos"]).decode('utf-8')
except:
    pass
try:
    pagina=urllib.unquote_plus(params["%23pagina"]).decode('utf-8')
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
    name=urllib.unquote_plus(params["%23name"])#.decode('utf-8')
except:
    pass
try:
    name=urllib.unquote_plus(params["#%23name"]).decode('utf-8')
except:
    pass
try:
    iconimage=urllib.unquote_plus(params["#iconimage"]).decode('utf-8')
except:
    pass
try:
    iconimage=urllib.unquote_plus(params["%23iconimage"]).decode('utf-8')
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
    Menu_Inicial()

elif mode==1: # Pesquisar
    GetQBPage(SelectionURL,int(Movies_Pos))

elif mode==2: # Separador Filmes por Generos
    addFolder("[COLOR=red]Aç[COLOR=blue]ão[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/acao/",icon_MenuGeneros_acao)
    addFolder("[COLOR=red]Aven[COLOR=blue]tura[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/aventura/",icon_MenuGeneros_aventura)
    addFolder("[COLOR=red]Anima[COLOR=blue]ção[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/animacao/",icon_MenuGeneros_animacao)
    addFolder("[COLOR=red]Animação [COLOR=blue](PT-PT)[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/animacao-em-portugues/",icon_MenuGeneros_animacaoPT)
    addFolder("[COLOR=red]Biogra[COLOR=blue]fia[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/biografia/",icon_MenuGeneros_biografia)
    addFolder("[COLOR=red]Comé[COLOR=blue]dia[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/comedia/",icon_MenuGeneros_comedia)
    addFolder("[COLOR=red]Cri[COLOR=blue]me[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/crime/",icon_MenuGeneros_crime)
    addFolder("[COLOR=red]Despor[COLOR=blue]to[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/desporto/",icon_MenuGeneros_desporto)
    addFolder("[COLOR=red]Documen[COLOR=blue]tário[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/generos/documentario/",icon_MenuGeneros_documentario)
    addFolder("[COLOR=red]Dra[COLOR=blue]ma[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/drama/",icon_MenuGeneros_drama)
    addFolder("[COLOR=red]Fami[COLOR=blue]liar[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/familiar/",icon_MenuGeneros_familiar)
    addFolder("[COLOR=red]Fanta[COLOR=blue]sia[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/fantasia/",icon_MenuGeneros_fantasia)
    addFolder("[COLOR=red]Gue[COLOR=blue]rra[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/guerra/",icon_MenuGeneros_guerra)
    addFolder("[COLOR=red]Histó[COLOR=blue]ria[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/historia/",icon_MenuGeneros_historia)
    addFolder("[COLOR=red]Misté[COLOR=blue]rio[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/misterio/",icon_MenuGeneros_misterio)
    addFolder("[COLOR=red]Musi[COLOR=blue]cal[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/musical/",icon_MenuGeneros_musical)
    addFolder("[COLOR=red]Portugês -[COLOR=blue] Brasileiro[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/portugues-brasileiro/",icon_MenuGeneros_PT_BR)
    addFolder("[COLOR=red]Roman[COLOR=blue]ce[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/romance/",icon_MenuGeneros_romance)
    addFolder("[COLOR=red]Terr[COLOR=blue]or[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/terror/",icon_MenuGeneros_terror)
    addFolder("[COLOR=red]Thri[COLOR=blue]ller[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/thriller/",icon_MenuGeneros_thriller)
    addFolder("[COLOR=red]West[COLOR=blue]ern[/COLOR][/COLOR]","plugin://plugin.video.pirataqb/&#mode=1&movies_pos=1&URL=http://www.pirataqb.com/filmes-online/western/",icon_MenuGeneros_western)

elif mode==3: # Pesquisa Avançada Filmes
    DoIt_OrNot = False
    #dialog = xbmcgui.Dialog()
    #fastnames = ['Filmes','Séries']
    #quest = dialog.select('Genero : ', fastnames)
    #if quest == 1 :DoIt_OrNot=True
    #elif quest == 2:DoIt_OrNot=False
    #elif quest == -1:quit()
    Movie=""
    if name == "" or name == None:
        dialog = xbmcgui.Dialog()
        Movie = dialog.input('Pesquisa',Load_Search(), type=xbmcgui.INPUT_ALPHANUM)
        if len(Movie) >= 4:
            Save_Search(Movie)
            Pesquisa_De_Filmes(Movie,1)
        elif len(Movie) <= 4 and len(Movie) <> 0:
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('Pesquisa','A pesquisa requer pelo menos 4 caracteres.','')
            while len(Movie) < 4 or Movie <> -1:
                dialog = xbmcgui.Dialog()
                Movie = dialog.input('Pesquisa',Load_Search(), type=xbmcgui.INPUT_ALPHANUM)
                if Movie == -1:
                    mode=None
                    break
            Save_Search(Movie)
            Pesquisa_De_Filmes(Movie,1)
    elif len(pagina) > 0:
            Pesquisa_De_Filmes(name,pagina)
    if len(Movie) <= 0 and len(pagina) <= 0:
        Menu_Inicial()

elif mode == 4:
    getSeriesqb(SelectionURL,int(Movies_Pos))

elif mode == 5:
    Menu_Filmes()

elif mode == 6:
    Menu_Series()

elif mode==19: # Reproduzir
    Progresso_File.create('Aguarde', 'A Processar o Link.')
    xbmc.sleep(1000)
    resolved = PirataQB_Resolver(url)
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    listitem = xbmcgui.ListItem( label = str(PirataQB_Text_Color_Engine(name.split('%')[0])), iconImage =str(iconimage), thumbnailImage = xbmc.getInfoImage( "ListItem.Thumb" ), path=str(resolved))
    Progresso_File.update(75, "", "A Equipa [COLOR=red][B]Pirata[/B][/COLOR][COLOR=blue]qb[/COLOR] deseja-lhe uma boa sessão!", "")
    xbmc.sleep(Sleep_Time)
    xbmc.Player().play(str(resolved),listitem)
    Progresso_File.close()
    subs=""
    if addon.getSetting("subtitles") == "true":
        if len(name.split('%')) > 0:
            try:
                print("My Subs Name are : "+name.split('%')[1])
                from resources.lib import subtitles
                try: subs = subtitles.getsubtitles(name.split('%')[1],addon.getSetting("sublang1"),addon.getSetting("sublang2"))
                except:msgbox("Erro a pesquisar legendas",1000)
            except:pass
            if subs !=None:
                xbmc.sleep(Sleep_Time)
                xbmc.Player().setSubtitles(subs.encode("utf-8"))
        else:print("TOTAL NAME OF FAIL : "+name)

elif mode == 72: # Construir Items (Séries)
    Episodio=""
    Serie = name
    linkattached=""
    Split = str(Episodios.decode('utf-8')).split('*')
    for i in range(0,len(Split)):
        if "%" in Split[i]:
            _A_Tua_Legenda = Split[i].split('%')[1]
        if i == 0:Episodio = Split[i]
        else:
            Episodio = Split[i]
            Episodio = Episodio.split('$')[0]
        if len(Episodio) > 0:
            Links = Split[i]
            if "$" in Links:
                Links = Links.split('$')[1]
                linkattached = "plugin://plugin.video.pirataqb/&#mode=19&#iconimage="+iconimage.encode('utf-8')+"&#name="+Serie.split('%')[0]+"- Episodio "+Episodio+"%"+_A_Tua_Legenda+"&"+Links.encode('utf-8')
                addLink(Serie.split('%')[0]+" - "+" Episodio "+Episodio,linkattached,iconimage.encode('utf-8'))


Set_Vista(addon.getSetting('Tp Vista'))
xbmcplugin.endOfDirectory(int(sys.argv[1]))











































########################################################################################################################
#if Serie_Or_Not == True:
 #               Preterit_Info = BruteInfo.split('\r\n')
  #              for i in range(len(Preterit_Info)):
   #                 if "<template class=" in Preterit_Info[i]:
    #                    Links_By_Episode = Preterit_Info[i].split('Episódio')
     #                   for i in range(len(Links_By_Episode)):
      #                      Lista_De_Links_Do_Episodio = []
       #                     Numero_Episodio = Links_By_Episode[i].split('<')[0]
        #                    Numero_Episodio = Numero_Episodio.replace(' ','')
         #                   Numero_Episodio = Numero_Episodio.replace('\r\n','')
          #                  for u in range(len(Lista_de_Links)):
           #                     if u == 0:linkattached+= "&#url="+Lista_de_Links[u]+"["+Numero_Episodio+"]"
            #                    else:linkattached+= "#"+Lista_de_Links[u]+"["+Numero_Episodio+"]"
#
########################################################################################################################




















######################################################## Dinossaurs #########################################################
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