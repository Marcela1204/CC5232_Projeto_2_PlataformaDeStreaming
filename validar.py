from supabase import *

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
            duplicatas += 1
    return duplicatas

duplicatas = {"usuarios" : 0,
             "avaliacoes" : 0,
            "assinaturas" : 0,
            "generos" : 0,
            "series" : 0,
            "filmes" : 0
        }

duplicatas["usuarios"] += verificar_duplicatas(readusuarios, "nome", duplicatas)
duplicatas["avaliacoes"] += verificar_duplicatas(readavaliacoes, "comentario", duplicatas)
duplicatas["assinaturas"] += verificar_duplicatas(readassinaturas, "usuario", duplicatas)
duplicatas["generos"] += verificar_duplicatas(readgeneros, "nome", duplicatas)
duplicatas["series"] += verificar_duplicatas(readseries, "titulo", duplicatas)
duplicatas["filmes"] += verificar_duplicatas(readfilmes, "titulo", duplicatas)

print("Total de duplicatas: \n", duplicatas)

def verificar_nulos(tabela,nulos):
    for i in tabela.data:
        for j in i:
            if i[j] == "":
                nulos += 1
    return nulos
nulos = {"usuarios" : 0,
         "avaliacoes" : 0,
        "assinaturas" : 0,
        "generos" : 0,
        "series" : 0,
        "filmes" : 0
    }
nulos["usuarios"] += verificar_nulos(readusuarios, nulos)
nulos["avaliacoes"] += verificar_nulos(readavaliacoes, nulos)
nulos["assinaturas"] += verificar_nulos(readassinaturas, nulos)
nulos["generos"] += verificar_nulos(readgeneros, nulos)
nulos["series"] += verificar_nulos(readseries, nulos)
nulos["filmes"] += verificar_nulos(readfilmes, nulos)

print("Total de nulos: \n", nulos)


erros = 0
progresso = 0
print("verificando usuarios")
for i in readusuarios.data:
    for j in readavaliacoes.data:
        print("{:.1f}%".format(progresso/(len(readusuarios.data)*len(readavaliacoes.data)) * 100), end="\r")
        if i["nome"] == j["usuario"]:
            if i["id_usuario"] != j["id_usuario"]:
                print(f"Erro: {i['nome']} tem id_usuario diferente em avaliacoes")
                erros += 1
        else:
            print(f"Erro: {i['nome']} existe em usuarios mas não em avaliacoes")
            erros += 1



