from supabase import *
import datetime
# Credenciais do Supabase

# Credenciais do Supabase
url = "https://yvgkrfqxetzrrpdgakjj.supabase.co"  # Substitua com a URL do seu projeto
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl2Z2tyZnF4ZXR6cnJwZGdha2pqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTUzODAxMywiZXhwIjoyMDYxMTE0MDEzfQ.QbQAi0Iw-lEHspFsuVCtBPLp72T2rZG9Gh1XJApWpZI"  # api key secret

# Inicializar o cliente do Supabase
supabase: Client = create_client(url, key)

def inserirFilme(titulo,duracao,ano,nomeGenero):#terceiro
    idgenero = supabase.table("generos").select("id_genero").eq("nome", nomeGenero).execute()
    response = supabase.table("filmes").insert({"titulo" : titulo, "duracao" : duracao, "ano_lancamento" : ano, "id_genero" : idgenero.data[0]["id_genero"], "genero" : idgenero.data[0]["nome"]}).execute()

def inserirGenero(descricao,nome):#primeiro
    response = supabase.table("generos").insert({"nome" : nome, "descricao" : descricao}).execute()

def inserirAvaliacao(comentario,data,nota,nomeusr,nomeSerie,nomeFilme):#quinto
    idusr = supabase.table("usuarios").select("id_usuario").eq("nome", nomeusr).execute()
    idserie = supabase.table("series").select("id_serie").eq("titulo", nomeSerie).execute()
    idfilme = supabase.table("filmes").select("id_filme").eq("titulo", nomeFilme).execute()
    if idserie.data == []:
        response = supabase.table("avaliacoes").insert({"comentario" : comentario, "data_avaliacao" : data, "nota" : nota, "id_usuario" : idusr.data[0]["id_usuario"], "id_filme" : idfilme.data[0]["id_filme"], "usuario" : idusr.data[0]["nome"]}).execute()
    else:
        response = supabase.table("avaliacoes").insert({"comentario" : comentario, "data_avaliacao" : data, "nota" : nota, "id_usuario" : idusr.data[0]["id_usuario"], "id_serie" : idserie.data[0]["id_serie"], "usuario" : idusr.data[0]["nome"]}).execute()

def inserirSerie(Ntemp,status,titulo,nomeGenero):#segundo
    idgenero = supabase.table("generos").select("id_genero").eq("nome", nomeGenero).execute()
    response = supabase.table("series").insert({"numero_temporadas" : Ntemp, "status" : status, "titulo" : titulo, "id_genero" : idgenero.data[0]["id_genero"], "genero" : idgenero.data[0]["nome"]}).execute()

def inserirAssinatura(tipo,valor,dataRenov,nome):#sexto
    idusr = supabase.table("usuarios").select("id_usuario").eq("nome", nome).execute()
    response = supabase.table("assinaturas").insert({"tipo_plano" : tipo, "valor" : valor, "data_renovacao" : dataRenov, "id_usuario" : idusr.data[0]["id_usuario"], "usuario" : idusr.data[0]["nome"]}).execute()

def inserirUsuario(nome,data,email):#quarto
    response = supabase.table("usuarios").insert({"nome" : nome, "data_nascimento" : data, "email" : email}).execute()

if __name__ == "__main__":
    inserirGenero("acão e aventura", "ação")
    inserirSerie(5, "ativa", "The Witcher", "ação")
    inserirFilme("Vingadores", 120, 2012, "ação")
    inserirUsuario("Lucas", datetime.datetime.strptime("2000-01-01","%Y-%m-%d").strftime("%Y-%m-%d"), "email@generico.com")
    inserirAvaliacao("muito bom", datetime.datetime.strptime("2023-10-01","%Y-%m-%d").strftime("%Y-%m-%d"), 5, "Lucas", "", "Vingadores")
    inserirAssinatura("mensal", 29.90, datetime.datetime.strptime("2023-10-01","%Y-%m-%d").strftime("%Y-%m-%d"), "Lucas")
    #data_obj = datetime.strptime(data_string, "%Y-%m-%d").date()
    #dados para testar a escrita do banco de dados