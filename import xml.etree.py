import xml.etree.ElementTree as ET
import urllib.request as request

def criar_url(ano, dtInicio, dfFim):
    url = "https://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx/ListarProposicoes?sigla=PL&numero=&ano=2011&datApresentacaoIni=14/11/2011&datApresentacaoFim=16/11/2011&parteNomeAutor=&idTipoAutor=&siglaPartidoAutor=&siglaUFAutor=&generoAutor=&codEstado=&codOrgaoEstado=&emTramitacao="
    return url.format(ano, dtInicio, dfFim)

def abre_url(url):
    req = request.urlopen(url)
    if req.getcode() == 200:
        return req.read()
    else:
        return None

def percorre(dados):
    proposicoes = ET.fromstring(dados)
    for proposicao in proposicoes:
        extraiTexto(proposicao)


def extraiTexto(proposicao):
    for tag_filha in proposicao:
        if tag_filha.tag == "txtEmenta":
            print(tag_filha.text.strip())

ano = int(input("Ano: "))
dtInicio = input("Data Início: ")
dtFim = input("Data Fim: ")

url = criar_url(ano, dtInicio, dtFim)
percorre(abre_url(url))
