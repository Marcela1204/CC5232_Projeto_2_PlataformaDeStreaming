from supabase import *
# Credenciais do Supabase

# Credenciais do Supabase
url = "https://yvgkrfqxetzrrpdgakjj.supabase.co"  # Substitua com a URL do seu projeto
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl2Z2tyZnF4ZXR6cnJwZGdha2pqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTUzODAxMywiZXhwIjoyMDYxMTE0MDEzfQ.QbQAi0Iw-lEHspFsuVCtBPLp72T2rZG9Gh1XJApWpZI"  # api key secret

# Inicializar o cliente do Supabase
supabase: Client = create_client(url, key)

def inserirFilme(titulo,duracao,ano,nomeGenero):
    idgenero = supabase.table("generos").select("id_genero").eq("nome", nomeGenero).execute()
    response = supabase.table("filmes").insert({"titulo" : titulo, "duracao" : duracao, "ano_lancamento" : ano, "id_genero" : idgenero}).execute()

def inserirGenero(descricao,nome):
    response = supabase.table("generos").insert({"nome" : nome, "descricao" : descricao}).execute()

def inserirAvaliacao(comentario,data,nota,nomeusr,nomeSerie,nomeFilme):
    idusr = supabase.table("usuarios").select("id_usuario").eq("nome", nomeusr).execute()
    idserie = supabase.table("series").select("id_serie").eq("nome", nomeSerie).execute()
    idfilme = supabase.table("filmes").select("id_filme").eq("nome", nomeFilme).execute()
    response = supabase.table("avaliacoes").insert({"comentario" : comentario, "data_avaliacao" : data, "nota" : nota, "id_usuario" : idusr, "id_serie" : idserie, "id_filme" : idfilme}).execute()

def inserirSerie(Ntemp,status,titulo,nomeGenero):
    idgenero = supabase.table("generos").select("id_genero").eq("nome", nomeGenero).execute()
    response = supabase.table("series").insert({"numero_temporadas" : Ntemp, "status" : status, "titulo" : titulo, "id_genero" : idgenero}).execute()

def inserirAssinatura(tipo,valor,dataRenov,nome):
    idusr = supabase.table("usuarios").select("id_usuarios").eq("nome", nome).execute()
    response = supabase.table("assinaturas").insert({"tipo_plano" : tipo, "valor" : valor, "data_renovacao" : dataRenov, "id_usuario" : idusr}).execute()

def inserirUsuario(nome,data,email):
    response = supabase.table("usuarios").insert({"nome" : nome, "data_nascimento" : data, "email" : email}).execute()