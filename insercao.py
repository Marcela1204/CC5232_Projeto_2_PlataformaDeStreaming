from supabase import *
# Credenciais do Supabase

# Credenciais do Supabase
url = "https://yvgkrfqxetzrrpdgakjj.supabase.co"  # Substitua com a URL do seu projeto
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl2Z2tyZnF4ZXR6cnJwZGdha2pqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTUzODAxMywiZXhwIjoyMDYxMTE0MDEzfQ.QbQAi0Iw-lEHspFsuVCtBPLp72T2rZG9Gh1XJApWpZI"  # api key secret

# Inicializar o cliente do Supabase
supabase: Client = create_client(url, key)

def inserirFilme(titulo,duracao,ano,nomeGenero):#terceiro
    idgenero = supabase.table("generos").select("id_genero").eq("nome", nomeGenero).execute()
    response = supabase.table("filmes").insert({"titulo" : titulo, "duracao" : duracao, "ano_lancamento" : ano, "id_genero" : idgenero}).execute()

def inserirGenero(descricao,nome):#primeiro
    response = supabase.table("generos").insert({"nome" : nome, "descricao" : descricao}).execute()

def inserirAvaliacao(comentario,data,nota,nomeusr,nomeSerie,nomeFilme):#quinto
    idusr = supabase.table("usuarios").select("id_usuario").eq("nome", nomeusr).execute()
    idserie = supabase.table("series").select("id_serie").eq("nome", nomeSerie).execute()
    idfilme = supabase.table("filmes").select("id_filme").eq("nome", nomeFilme).execute()
    response = supabase.table("avaliacoes").insert({"comentario" : comentario, "data_avaliacao" : data, "nota" : nota, "id_usuario" : idusr, "id_serie" : idserie, "id_filme" : idfilme}).execute()

def inserirSerie(Ntemp,status,titulo,nomeGenero):#segundo
    idgenero = supabase.table("generos").select("id_genero").eq("nome", nomeGenero).execute()
    response = supabase.table("series").insert({"numero_temporadas" : Ntemp, "status" : status, "titulo" : titulo, "id_genero" : idgenero}).execute()

def inserirAssinatura(tipo,valor,dataRenov,nome):#sexto
    idusr = supabase.table("usuarios").select("id_usuarios").eq("nome", nome).execute()
    response = supabase.table("assinaturas").insert({"tipo_plano" : tipo, "valor" : valor, "data_renovacao" : dataRenov, "id_usuario" : idusr}).execute()

def inserirUsuario(nome,data,email):#quarto
    response = supabase.table("usuarios").insert({"nome" : nome, "data_nascimento" : data, "email" : email}).execute()

if __name__ == "__main__":
    inserirGenero("acão e aventura", "ação")
    inserirSerie(5, "em andamento", "The Witcher", "ação")
    inserirFilme("Vingadores", 120, 2012, "ação")
    inserirUsuario("Lucas", "2000-01-01", "email@generico.com")
    inserirAvaliacao("muito bom", "2023-10-01", 5, "Lucas", "", "Vingadores")
    inserirAssinatura("mensal", 29.90, "2023-10-01", "Lucas")
    #dados para testar a escrita do banco de dados