
import requests
import lxml.html as html
import pandas as pd
import csv

url = 'https://www.eltiempo.com/deportes/futbol-colombiano/tabla-posiciones'
nombre = '//table[@border="0"]//tr[starts-with(@class, "tabla-escudos")]/td[@class="equipo"]/span/text()'
partidosj = '//table[@border="0"]//tr[starts-with(@class, "tabla-escudos")]/td[@class="c1"][1]/span/text()'
parg = '//table[@border="0"]//tr[starts-with(@class, "tabla-escudos")]/td[@class = "c1"][2]/span/text()'
parp = '//table[@border="0"]//tr[starts-with(@class, "tabla-escudos")]/td[@class = "c1"][3]/span/text()'
pare = '//table[@border="0"]//tr[starts-with(@class, "tabla-escudos")]/td[@class = "c1"][4]/span/text()'
golesf = '//table[@border="0"]//tr[starts-with(@class, "tabla-escudos")]/td[@class = "c1"][5]/span/text()'
golesc = '//table[@border="0"]//tr[starts-with(@class, "tabla-escudos")]/td[@class = "c1"][6]/span/text()'
favorvi  = '//table[@border="0"]//tr[starts-with(@class, "tabla-escudos")]/td[@class = "c1"][7]/span/text()'
contrvis = '//table[@border="0"]//tr[starts-with(@class, "tabla-escudos")]/td[@class = "c1"][8]/span/text()'
gold = '//table[@border="0"]//tr[starts-with(@class, "tabla-escudos")]/td[@class = "c1"][9]/span/text()'
puntos  = '//table[@border="0"]//tr[starts-with(@class, "tabla-escudos")]/td[@class = "puntos"]/span/text()'

response = requests.get(url)

if response.status_code == 200:
    home = response.content.decode('utf-8')
    parsed = html.fromstring(home)

    equipo = parsed.xpath(nombre)
    print(equipo)
    print(len(equipo))
    pj = parsed.xpath(partidosj)
    pg = parsed.xpath(parg)
    pp  = parsed.xpath(parp)
    pe = parsed.xpath(pare)
    gf = parsed.xpath(golesf)
    gc  = parsed.xpath(golesc)
    fv = parsed.xpath(favorvi)
    cv = parsed.xpath(contrvis)
    gd  = parsed.xpath(gold)
    puntaje = parsed.xpath(puntos)

    df = pd.DataFrame({'Nombre': equipo, 'PJ': pj, 'PG': pg, 'PP': pp, 'PE': pe, 'GF': gf, 'GC': gc, 'FV': fv, 'CV': cv, 'GD': gd, 'PUNTOS': puntaje}, 
    columns=['NOMBRE','PJ', 'PG', 'PP', 'PE', 'GF', 'GC', 'FV', 'CV', 'GD', 'PUNTOS'])

    df.to_csv('./tabla.csv')

 



  