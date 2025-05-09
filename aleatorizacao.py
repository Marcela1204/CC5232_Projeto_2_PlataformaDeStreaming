import faker
import random
from insercao import *

def gerar_nome_filme_serie():
    fake = faker.Faker()
    # Gera um nome aleatório de filme combinando palavras
    nome_filme = f"{fake.word().capitalize()} {fake.word().capitalize()}"
    return nome_filme

def gerar_genero_filme():
    generos = [
        "Ação", "Comédia", "Drama", "Fantasia", "Terror", 
        "Ficção Científica", "Romance", "Suspense", "Animação", "Documentário"
    ]
    fake = faker.Faker()
    return fake.random_element(generos)

def gerar_dados_pessoa():
    fake = faker.Faker()
    nome = fake.name()
    email = fake.email()
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=40).strftime("%Y-%m-%d")
    return {"nome": nome, "email": email, "data_nascimento": data_nascimento}

def gerar_avaliacao(nomeF,usuario,tipo):
    fake = faker.Faker()
    comentario = fake.sentence(nb_words=10)
    data = fake.date_this_year().strftime("%Y-%m-%d")
    nota = fake.random_int(min=1, max=5)
    #usuario = fake.name()
    #if fake.boolean():  # Decide aleatoriamente entre filme ou série
        #tipo = "filme"
        #nome = gerar_nome_filme_serie()
    #else:
        #tipo = "serie"
        #nome = gerar_nome_filme_serie()
    return {
        "comentario": comentario,
        "data": data,
        "nota": nota,
        "usuario": usuario,
        "tipo": tipo,
        "nome": nomeF
    }
if __name__ == "__main__":
    pessoas = []
    filmes = []
    series = []
    midias = []
    avaliacoes = []
    assinaturas = []
    planos = []
    #todos os dados a serem inseridos no banco
    assinex = ["premium", "basico", "familia"]
    assvalores = {"premium": 49.90, "basico": 29.90, "familia": 39.90}
    for _ in range(10):
        pessoas.append(gerar_dados_pessoa())
    for _ in range(5):
        series.append(gerar_nome_filme_serie())
        filmes.append(gerar_nome_filme_serie())
    midias = filmes[:] + series[:]
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
    for l in pessoas:
        tipo = faker.Faker().random_element(assinex)
        desconto = faker.Faker().pyfloat(min_value=0,max_value=.5)
        planos.append({"data_renovacao" : faker.Faker().date_this_year().strftime("%Y-%m-%d"), "desconto" : desconto})
        assinaturas.append({"usuario": l["nome"], "tipo": tipo, "data_renovacao": faker.Faker().date_this_year().strftime("%Y-%m-%d"), "valor" : assvalores[tipo]*desconto})

    
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
        print("{0}%".format(progresso/len(generos) * 100), end="\r")
    progresso = 0
    print("gerando series")
    for i in series:
        inserirSerie(random.randint(1, 5), "ativa", i, gerar_genero_filme())
        progresso += 1
        print("{0}%".format(progresso/len(series) * 100), end="\r")
    progresso = 0
    print("gerando filmes")
    for i in filmes:
        inserirFilme(i, random.randint(60, 180), random.randint(2000, 2023), gerar_genero_filme())
        progresso += 1
        print("{0}%".format(progresso/len(filmes) * 100), end="\r")
    progresso = 0
    print("gerando usuarios")
    for i in pessoas:
        inserirUsuario(i["nome"], i["data_nascimento"], i["email"])
        progresso += 1
        print("{0}%".format(progresso/len(pessoas) * 100), end="\r")
    progresso = 0
    print("gerando avaliacoes")
    for i in avaliacoes:
        if i["tipo"] == "filme":
            inserirAvaliacao(i["comentario"], i["data"], i["nota"], i["usuario"], "", i["nome"])
        else:
            inserirAvaliacao(i["comentario"], i["data"], i["nota"], i["usuario"], i["nome"], "")
        progresso += 1
        print("{0}%".format(progresso/len(avaliacoes) * 100), end="\r")
    progresso = 0
    print("gerando assinaturas")
    for i in assinaturas:
        inserirAssinatura(i["tipo"], i["valor"], i["usuario"])
        for j in planos:
            inserirPlano(j["data_renovacao"],j["desconto"],i["tipo"])
            progresso += 1
            print("{0}%".format(progresso/(len(assinaturas)*len(planos)) * 100), end="\r")
    print("gerando classificacao etaria")
    progresso = 0
    classificacoes = ["L", "10", "12", "14", "16", "18"]
    for i in series:
        inserirGeneroSerie(i,faker.Faker().random_element(classificacoes))
        progresso +=1
        print("{0}%".format(progresso/len(series) * 50))
    for i in filmes:
        inserirGeneroFilme(i,faker.Faker().random_element(classificacoes))
        progresso +=1
        print("{0}%".format(progresso/len(filmes) * 50))

    