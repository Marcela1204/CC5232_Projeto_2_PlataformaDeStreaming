import faker

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
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=40)
    return {"nome": nome, "email": email, "data_nascimento": data_nascimento}

def gerar_avaliacao(nomeF,usuario,tipo):
    fake = faker.Faker()
    comentario = fake.sentence(nb_words=10)
    data = fake.date_this_year()
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
    #todos os dados a serem inseridos no banco
    assinex = ["premium", "basico", "familia"]
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
        assinaturas.append({"usuario": l["nome"], "tipo": faker.Faker().random_element(assinex), "data_renovacao": faker.Faker().date_this_year()})

    
    print(pessoas)