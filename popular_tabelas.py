import faker
import random
from insercao import *
from aleatorizacao import *

def popular(numUsuarios,numMidias):
    pessoas = []
    filmes = []
    series = []
    midias = []
    avaliacoes = []
    assinaturas = []
    #todos os dados a serem inseridos no banco
    assinex = ["premium", "basico", "familia"]
    assvalores = {"premium": 49.90, "basico": 29.90, "familia": 39.90}
    progresso = 0
    print("indexando usuarios")
    for _ in range(numUsuarios):
        pessoas.append(gerar_dados_pessoa())
        progresso += 1
        print("{:.1f}%".format(progresso/numUsuarios * 100), end="\r")
    progresso = 0
    print("indexando midias")
    for _ in range(numMidias//2):
        series.append(gerar_nome_filme_serie())
        filmes.append(gerar_nome_filme_serie())
        progresso += 1
        print("{:.1f}%".format(progresso/(numMidias//2) * 100), end="\r")
    midias = filmes[:] + series[:]
    progresso = 0
    print("indexando avaliacoes")
    for i in midias:
        for j in pessoas:
            if i in filmes:
                tipo = "filme"
            else:
                tipo = "serie"
            avaliacao = gerar_avaliacao(i, j["nome"],tipo)
            #print(f"Avaliação para {avaliacao['tipo']} '{avaliacao['nome']}' por {avaliacao['usuario']}:")
            #print(f"Comentário: {avaliacao['comentario']}")
            #print(f"Data: {avaliacao['data']}")
            #print(f"Nota: {avaliacao['nota']}")
            #print()
            avaliacoes.append(avaliacao)
            progresso += 1 
            print("{:.1f}%".format(progresso/len(midias)*len(pessoas) * 100), end="\r")
    progresso = 0
    print("indexando assinaturas")
    for l in pessoas:
        tipo = faker.Faker().random_element(assinex)
        assinaturas.append({"usuario": l["nome"], "tipo": tipo, "data_renovacao": faker.Faker().date_this_year().strftime("%Y-%m-%d"), "valor" : assvalores[tipo]})
        progresso += 1
        print("{0}%".format(progresso/len(pessoas) * 100), end="\r")

    
    #print(pessoas)
    generos = [
        "Ação", "Comédia", "Drama", "Fantasia", "Terror", 
        "Ficção Científica", "Romance", "Suspense", "Animação", "Documentário"
    ]
    progresso = 0
    print("gerando generos")
    for i in generos:
        fake = faker.Faker()
        inserirGenero(fake.sentence(nb_words=2), i)
        progresso += 1
        print("{:.1f}%".format(progresso/len(generos) * 100), end="\r")
    progresso = 0
    print("gerando series")
    status = ["ativa", "finalizada"]
    for i in series:
        inserirSerie(random.randint(1, 5), faker.Faker.random_element(status), i, gerar_genero_filme())
        progresso += 1
        print("{:.1f}%".format(progresso/len(series) * 100), end="\r")
    progresso = 0
    print("gerando filmes")
    for i in filmes:
        inserirFilme(i, random.randint(60, 180), random.randint(2000, 2023), gerar_genero_filme())
        progresso += 1
        print("{:.1f}%".format(progresso/len(filmes) * 100), end="\r")
    progresso = 0
    print("gerando usuarios")
    for i in pessoas:
        inserirUsuario(i["nome"], i["data_nascimento"], i["email"])
        progresso += 1
        print("{:.1f}%".format(progresso/len(pessoas) * 100), end="\r")
    progresso = 0
    print("gerando avaliacoes")
    for i in avaliacoes:
        if i["tipo"] == "filme":
            inserirAvaliacao(i["comentario"], i["data"], i["nota"], i["usuario"], "", i["nome"])
        else:
            inserirAvaliacao(i["comentario"], i["data"], i["nota"], i["usuario"], i["nome"], "")
        progresso += 1
        print("{:.1f}%".format(progresso/len(avaliacoes) * 100), end="\r")
    progresso = 0
    print("gerando assinaturas")
    for i in assinaturas:
        inserirAssinatura(i["tipo"], i["valor"], i["data_renovacao"], i["usuario"])
        progresso += 1
        print("{:.1f}%".format(progresso/len(assinaturas) * 100), end="\r")

if __name__ == "__main__":
    popular(10,20)#numero de usuarios(10) e numero de midias(20)