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
duplicatas["assinaturas"] += verificar_duplicatas(readassinaturas, "id_assinatura", duplicatas["assinaturas"])
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
def verificar_consistencia(tabela1,tabela2,var1,var2,id1,id2):
    erros = 0 
    for i in tabela1.data:
        for j in tabela2.data:
            if i[var1] == j[var2]:
                if i[id1] != j[id2]:
                    print(f"Erro: {i[var1]} tem id_usuario diferente em avaliacoes")
                    erros += 1
    return erros

erros = 0

erros += verificar_consistencia(readusuarios, readavaliacoes, "nome", "usuario", "id_usuario", "id_usuario")
erros += verificar_consistencia(readusuarios, readassinaturas, "nome", "usuario", "id_usuario", "id_usuario")
erros += verificar_consistencia(readgeneros, readfilmes, "nome", "titulo", "id_genero", "id_genero")
erros += verificar_consistencia(readgeneros, readseries, "nome", "titulo", "id_genero", "id_genero")

print("Total de erros: \n", erros)

print("verificando maioridade")
for i in readusuarios.data:
    hoje = datetime.today()
    maioridade = hoje - timedelta(days=18*365)  # Aproximadamente 18 anos

    if not i["data_nascimento"] or datetime.strptime(i["data_nascimento"], "%Y-%m-%d") > maioridade:
        print(f"Erro: {i['nome']} não é maior de 18 anos ou tem data de nascimento nula")
print("maioridade concluido \n")

print("verificando email")
for i in readusuarios.data:
    if i["email"].find("@") == -1 or i["email"].find(".") == -1 or i["email"] == "":
        print(f"Erro: {i['nome']} tem email inválido ou nulo")
print("email concluido \n")

print("verificando duracao do filme")

for i in readfilmes.data:
    if i["duracao"] < 0 or i["duracao"] > 300:
        print(f"Erro: {i['titulo']} tem duração inválida")
print("duracao concluido \n")

print("verificando numero de temporadas")
for i in readseries.data:
    if i["numero_temporadas"] < 0 or i["numero_temporadas"] > 20:
        print(f"Erro: {i['titulo']} tem número de temporadas inválido")

print("temporadas concluido \n")

print("verificando avaliacoes")

for i in readavaliacoes.data:
    if i["nota"] < 0 or i["nota"] > 5:
        print(f"Erro: {i['usuario']} tem nota inválida")
    if i["comentario"] == "":
        print(f"Erro: {i['usuario']} tem comentario vazio")
    if i["data_avaliacao"] == "":
        print(f"Erro: {i['usuario']} tem data de avaliacao vazia")
print("avaliacoes concluido \n")

print("verificando assinaturas")
for i in readassinaturas.data:
    if i["valor"] <= 0:
        print(f"Erro: {i['usuario']} tem valor de assinatura inválido")
print("assinatura concluido \n")

print("verificando avaliacoes duplicadas")
vistos = []
duplicatas = 0
for i in readavaliacoes.data:
	if (i["usuario"],i["id_filme"]) in vistos or (i["usuario"],i["id_serie"]) in vistos:
		duplicatas += 1
	else:
		if i["id_serie"] == None:
			vistos.append((i["usuario"],i["id_filme"]))
		else:
			vistos.append((i["usuario"],i["id_serie"]))
print("numero de usuarios com avaliacoes duplicadas: \n",duplicatas)

print("verificando consistencia de filmes e avaliacoes")
erros = 0
for i in readfilmes.data:
	#for j in readavaliacoes.data:
    nao_existe = all(d["id_filme"] != i["id_filme"] for d in readavaliacoes.data)
		#if i["id_filme"] != j["id_filme"]  and j["id_filme"] != None:
    if nao_existe:
        erros += 1
print("flmes que não constam na tabela de avaliacoes: \n",erros)


print("verificando consistencia de filmes e avaliacoes")
erros = 0
for i in readseries.data:
	#for j in readavaliacoes.data:
    nao_existe = all(d["id_serie"] != i["id_serie"] for d in readavaliacoes.data)
		#if i["id_serie"] != j["id_serie"] and j["id_serie"] != None:
    if nao_existe:
        erros += 1
print("series que não constam na tabela de avaliacoes: \n",erros)

print("verificando consistencia de assinaturas e usuarios")
erros = 0
for i in readusuarios.data:
		nao_existe = all(d["id_usuario"] != i["id_usuario"] for d in readassinaturas.data)
		if nao_existe:
			erros += 1
print("usuarios sem assinaturas: \n",erros)

print("verificando duplicatas de assinaturas")

vistos = []
erros = 0
for i in readassinaturas.data:
	if i["id_usuario"] in vistos:
		erros += 1
	else:
		vistos.append(i["id_usuario"])
print("assinaturas duplicadas: \n",erros)
		

erros = 0
for i in readgeneros.data:
		nao_existe = all(d["id_genero"] != i["id_genero"] for d in readfilmes.data)
		if nao_existe:
			erros += 1
print("usuarios sem assinaturas: \n",erros)

erros = 0
for i in readgeneros.data:
    nao_existe = all(d["id_genero"] != i["id_genero"] for d in readfilmes.data)
    if nao_existe:
        erros += 1
    nao_existe = all(d["id_genero"] != i["id_genero"] for d in readseries.data)
    if nao_existe:
        erros += 1
print("generos nao atribuidos a nenhuma midia: \n",erros)



