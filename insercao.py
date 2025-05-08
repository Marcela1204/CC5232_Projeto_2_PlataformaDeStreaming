from supabase import *
import datetime
# Credenciais do Supabase

# Credenciais do Supabase
url = "https://yvgkrfqxetzrrpdgakjj.supabase.co"  # Substitua com a URL do seu projeto
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl2Z2tyZnF4ZXR6cnJwZGdha2pqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTUzODAxMywiZXhwIjoyMDYxMTE0MDEzfQ.QbQAi0Iw-lEHspFsuVCtBPLp72T2rZG9Gh1XJApWpZI"  # api key secret

# Inicializar o cliente do Supabase
supabase: Client = create_client(url, key)

def inserirFilme(titulo,duracao,ano,nomeGenero):#terceiro
    #idgenero = supabase.table("generos").select("id_genero").eq("nome", nomeGenero).execute()
    response = supabase.table("filmes").insert({"titulo" : titulo, "duracao" : duracao, "ano_lancamento" : ano}).execute()

def inserirGenero(descricao,nome):#primeiro
    response = supabase.table("generos").insert({"nome" : nome, "descricao" : descricao}).execute()

def inserirAvaliacao(comentario,data,nota,nomeusr,nomeSerie,nomeFilme):#quinto
    idusr = supabase.table("usuarios").select("id_usuario").eq("nome", nomeusr).execute()
    idserie = supabase.table("series").select("id_serie").eq("titulo", nomeSerie).execute()
    idfilme = supabase.table("filmes").select("id_filme").eq("titulo", nomeFilme).execute()
    if idserie.data == []:
        response = supabase.table("avaliacoes").insert({"comentario" : comentario, "data_avaliacao" : data, "nota" : nota, "id_usuario" : idusr.data[0]["id_usuario"], "id_filme" : idfilme.data[0]["id_filme"]}).execute()
    else:
        response = supabase.table("avaliacoes").insert({"comentario" : comentario, "data_avaliacao" : data, "nota" : nota, "id_usuario" : idusr.data[0]["id_usuario"], "id_serie" : idserie.data[0]["id_serie"]}).execute()

def inserirSerie(Ntemp,status,titulo,nomeGenero):#segundo
    #idgenero = supabase.table("generos").select("id_genero").eq("nome", nomeGenero).execute()
    response = supabase.table("series").insert({"numero_temporadas" : Ntemp, "status" : status, "titulo" : titulo}).execute()

def inserirAssinatura(tipo,valor,nome):#sexto
    #idusr = supabase.table("usuarios").select("id_usuario").eq("nome", nome).execute()
    response = supabase.table("assinaturas").insert({"tipo_plano" : tipo, "valor" : valor}).execute()

def inserirUsuario(nome,data,email,assinatura):#quarto
    idAssinatura = supabase.table("assinaturas").select("tipo").eq("id_assinatura", assinatura).execute()
    idPlano = supabase.table("planos").select("id_Plano").eq("id_assinatura", idAssinatura.data[0]["tipo"]).execute()
    response = supabase.table("usuarios").insert({"nome" : nome, "data_nascimento" : data, "email" : email, "id_Plano" : idPlano.data[0]["id_Plano"]}).execute()

def inserirPlano(data_renovacao,desconto,assinatura):
    id_ass = supabase.table("assinaturas").select("id_assinatura").eq("tipo_plano", assinatura).execute()
    response = supabase.table("planos").insert({"data_renovacao" : data_renovacao, "desconto" : desconto, "id_assinatura" : id_ass}).execute()

def inserirGeneroFilme(titulo,genero,classificacao):
    id_genero = supabase.table("generos").select("id_genero").eq("nome", genero).execute()
    id_filme = supabase.table("filmes").select("id_filme").eq("titulo", titulo).execute()
    response = supabase.table("generofilme").insert({"id_genero" : id_genero.data[0]["id_genero"], "id_filme" : id_filme.data[0]["id_filme"], "classificacao_indicativa" : classificacao})

def inserirGeneroSerie(titulo,genero,classificacao):
    id_genero = supabase.table("generos").select("id_genero").eq("nome", genero).execute()
    id_filme = supabase.table("series").select("id_serie").eq("titulo", titulo).execute()
    response = supabase.table("generoserie").insert({"id_genero" : id_genero.data[0]["id_genero"], "id_serie" : id_filme.data[0]["id_serie"], "classificacao_indicativa" : classificacao})


if __name__ == "__main__":
    inserirGenero("acão e aventura", "ação")
    inserirSerie(5, "ativa", "The Witcher", "ação")
    inserirFilme("Vingadores", 120, 2012, "ação")
    inserirUsuario("Lucas", datetime.datetime.strptime("2000-01-01","%Y-%m-%d").strftime("%Y-%m-%d"), "email@generico.com")
    inserirAvaliacao("muito bom", datetime.datetime.strptime("2023-10-01","%Y-%m-%d").strftime("%Y-%m-%d"), 5, "Lucas", "", "Vingadores")
    inserirAssinatura("mensal", 29.90, datetime.datetime.strptime("2023-10-01","%Y-%m-%d").strftime("%Y-%m-%d"), "Lucas")
    #data_obj = datetime.strptime(data_string, "%Y-%m-%d").date()
    #dados para testar a escrita do banco de dados