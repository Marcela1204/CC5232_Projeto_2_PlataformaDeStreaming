import base64
def str_xor(message, key):
    #return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1,s2)])
    # Aplica XOR entre a mensagem e a chave
    encrypted = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message))
    # Codifica o resultado em Base64 e limita a 20 caracteres
    return base64.urlsafe_b64encode(encrypted.encode()).decode()[:20]

import faker
import random
from insercaoencrypt import *
from aleatorizacao import *

def encryptPopular(numUsuarios,numMidias,senha):
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
            avaliacoes.append(avaliacao)
        progresso += 1 
        print("{:.1f}%".format(progresso/len(midias) * 100), end="\r")
    progresso = 0
    print("indexando assinaturas")
    for l in pessoas:
        tipo = faker.Faker().random_element(assinex)
        assinaturas.append({"usuario": l["nome"], "tipo": tipo, "data_renovacao": faker.Faker().date_this_year().strftime("%Y-%m-%d"), "valor" : assvalores[tipo]})
        progresso += 1
        print("{0}%".format(progresso/len(pessoas) * 100), end="\r")

    generos = [
        "Ação", "Comédia", "Drama", "Fantasia", "Terror", 
        "Ficção Científica", "Romance", "Suspense", "Animação", "Documentário"
    ]
    progresso = 0
    print("gerando generos")
    for i in generos:
        fake = faker.Faker()
        encryptInserirGenero(str_xor(fake.sentence(nb_words=2),senha), str_xor(i,senha),senha)
        progresso += 1
        print("{:.1f}%".format(progresso/len(generos) * 100), end="\r")
    progresso = 0
    print("gerando series")
    status = ["ativa", "finalizada"]
    fake = faker.Faker()
    for i in series:
        encryptInserirSerie(random.randint(1, 5), str_xor(fake.random_element(status),senha), str_xor(i,senha), str_xor(gerar_genero_filme(),senha),senha)
        progresso += 1
        print("{:.1f}%".format(progresso/len(series) * 100), end="\r")
    progresso = 0
    print("gerando filmes")
    for i in filmes:
        encryptInserirFilme(str_xor(i,senha), random.randint(60, 180), random.randint(2000, 2023), str_xor(gerar_genero_filme(),senha),senha)
        progresso += 1
        print("{:.1f}%".format(progresso/len(filmes) * 100), end="\r")
    progresso = 0
    print("gerando usuarios")
    for i in pessoas:
        encryptInserirUsuario(str_xor(i["nome"],senha), i["data_nascimento"], str_xor(i["email"],senha),senha)
        progresso += 1
        print("{:.1f}%".format(progresso/len(pessoas) * 100), end="\r")
    progresso = 0
    print("gerando avaliacoes")
    for i in avaliacoes:
        if i["tipo"] == "filme":
            encryptInserirAvaliacao(str_xor(i["comentario"],senha), i["data"], i["nota"], str_xor(i["usuario"],senha), "", str_xor(i["nome"],senha),senha)
        else:
            encryptInserirAvaliacao(str_xor(i["comentario"],senha), i["data"], i["nota"], str_xor(i["usuario"],senha), str_xor(i["nome"],senha), "",senha)
        progresso += 1
        print("{:.1f}%".format(progresso/len(avaliacoes) * 100), end="\r")
    progresso = 0
    print("gerando assinaturas")
    for i in assinaturas:
        encryptInserirAssinatura(str_xor(i["tipo"],senha), i["valor"], i["data_renovacao"], str_xor(i["usuario"],senha),senha)
        progresso += 1
        print("{:.1f}%".format(progresso/len(assinaturas) * 100), end="\r")

if __name__ == "__main__":
    #senha = input("forneça sua senha ")
    senha = "senha"
    encryptPopular(10,10,senha)