from operationbd import *

from operationbd import abrirBancoDados

conn = abrirBancoDados('localhost','root','Weslley(2021)','systemouvi')


sql = "select * from manifestation"
resultado = listarBancoDados(conn,sql)

for elemento in resultado:
    print(elemento)



name = input('enter your name:  ')
type = int(input('enter the type '))
description = float(input('digite o preco '))

sql = "INSERT INTO produtos(nome,descricao,preco) VALUES (%s, %s, %s)"
dados = (name,type,description)
insertNoBancoDados(conn,sql,dados)


'''
sql = "INSERT INTO produtos(nome,descricao,preco) VALUES (%s, %s, %s)"
dados = ('Banana','Bana Pacovan',8)
insertNoBancoDados(conn,sql,dados)
'''

def searchProtocol(protocol):
    sql = "select * from manifestation"
    result = listarBancoDados(conn, sql)
    for elemento in result:
        if elemento[0] == protocol:
            print(elemento)


