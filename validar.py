from supabase import *
from datetime import datetime, timedelta

url = "https://yvgkrfqxetzrrpdgakjj.supabase.co"  # Substitua com a URL do seu projeto
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl2Z2tyZnF4ZXR6cnJwZGdha2pqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTUzODAxMywiZXhwIjoyMDYxMTE0MDEzfQ.QbQAi0Iw-lEHspFsuVCtBPLp72T2rZG9Gh1XJApWpZI"  # api key secret


supabase: Client = create_client(url, key)

readfilmes = supabase.table('filmes').select('*').execute()
readseries = supabase.table('series').select('*').execute()
readgeneros = supabase.table('generos').select('*').execute()
readusuarios = supabase.table('usuarios').select('*').execute()
readavaliacoes = supabase.table('avaliacoes').select('*').execute()
readassinaturas = supabase.table('assinaturas').select('*').execute()

def verificar_duplicatas(tabela,coluna,counterDuplicatas):
    vistos = []
    for i in tabela.data:
        if i[coluna] not in vistos:
            vistos.append(i[coluna])
        else:
            counterDuplicatas += 1
    return counterDuplicatas

duplicatas = {"usuarios" : 0,
             "avaliacoes" : 0,
            "assinaturas" : 0,
            "generos" : 0,
            "series" : 0,
            "filmes" : 0
        }

duplicatas["usuarios"] += verificar_duplicatas(readusuarios, "nome", duplicatas["usuarios"])
duplicatas["avaliacoes"] += verificar_duplicatas(readavaliacoes, "comentario", duplicatas["avaliacoes"])
duplicatas["assinaturas"] += verificar_duplicatas(readassinaturas, "usuario", duplicatas["assinaturas"])
duplicatas["generos"] += verificar_duplicatas(readgeneros, "nome", duplicatas["generos"])
duplicatas["series"] += verificar_duplicatas(readseries, "titulo", duplicatas["series"])
duplicatas["filmes"] += verificar_duplicatas(readfilmes, "titulo", duplicatas["filmes"])

print("Total de duplicatas: \n", duplicatas)

def verificar_nulos(tabela,nulos):
    for i in tabela.data:
        for j in i:
            if i[j] == None:
                nulos += 1
    return nulos
nulos = {"usuarios" : 0,
         "avaliacoes" : 0,
        "assinaturas" : 0,
        "generos" : 0,
        "series" : 0,
        "filmes" : 0
    }
nulos["usuarios"] += verificar_nulos(readusuarios, nulos["usuarios"])
nulos["avaliacoes"] += verificar_nulos(readavaliacoes, nulos["avaliacoes"])
nulos["assinaturas"] += verificar_nulos(readassinaturas, nulos["assinaturas"])
nulos["generos"] += verificar_nulos(readgeneros, nulos["generos"])
nulos["series"] += verificar_nulos(readseries, nulos["series"])
nulos["filmes"] += verificar_nulos(readfilmes, nulos["filmes"])

print("Total de nulos: \n", nulos)


erros = 0
def verificar_erros(tabela1,tabela2,var1,var2,id1,id2):
    erros = 0 
    for i in tabela1.data:
        for j in tabela2.data:
            if i[var1] == j[var2]:
                if i[id1] != j[id2]:
                    print(f"Erro: {i[var1]} tem id_usuario diferente em avaliacoes")
                    erros += 1
    return erros

erros = 0

erros += verificar_erros(readusuarios, readavaliacoes, "nome", "usuario", "id_usuario", "id_usuario")
erros += verificar_erros(readusuarios, readassinaturas, "nome", "usuario", "id_usuario", "id_usuario")
erros += verificar_erros(readgeneros, readfilmes, "nome", "titulo", "id_genero", "id_genero")
erros += verificar_erros(readgeneros, readseries, "nome", "titulo", "id_genero", "id_genero")

print("Total de erros: \n", erros)

print("verificando maioridade")
for i in readusuarios.data:
    hoje = datetime.today()
    maioridade = hoje - timedelta(days=18*365)  # Aproximadamente 18 anos

    if not i["data_nascimento"] or datetime.strptime(i["data_nascimento"], "%Y-%m-%d") > maioridade:
        print(f"Erro: {i['nome']} não é maior de 18 anos ou tem data de nascimento nula")

print("verificando email")
for i in readusuarios.data:
    if i["email"].find("@") == -1 or i["email"].find(".") == -1 or i["email"] == "":
        print(f"Erro: {i['nome']} tem email inválido ou nulo")

print("verificando duracao do filme")

for i in readfilmes.data:
    if i["duracao"] < 0 or i["duracao"] > 300:
        print(f"Erro: {i['titulo']} tem duração inválida")

print("verificando numero de temporadas")
for i in readseries.data:
    if i["numero_temporadas"] < 0 or i["numero_temporadas"] > 20:
        print(f"Erro: {i['titulo']} tem número de temporadas inválido")

print("verificando avaliacoes")

for i in readavaliacoes.data:
    if i["nota"] < 0 or i["nota"] > 5:
        print(f"Erro: {i['usuario']} tem nota inválida")
    if i["comentario"] == "":
        print(f"Erro: {i['usuario']} tem comentario vazio")
    if i["data_avaliacao"] == "":
        print(f"Erro: {i['usuario']} tem data de avaliacao vazia")

print("verificando assinaturas")
for i in readassinaturas.data:
    if i["valor"] <= 0:
        print(f"Erro: {i['usuario']} tem valor de assinatura inválido")





