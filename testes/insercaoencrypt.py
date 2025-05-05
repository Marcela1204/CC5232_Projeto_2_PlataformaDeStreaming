from supabase import *
import datetime
import base64
def str_xordec(encrypted_message, key):
    #return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1,s2)])
    # Decodifica a mensagem criptografada de Base64
    encrypted = base64.urlsafe_b64decode(encrypted_message.encode()).decode()
    # Aplica XOR novamente para obter a mensagem original
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(encrypted))

# Credenciais do Supabase

# Credenciais do Supabase
url = "https://yvgkrfqxetzrrpdgakjj.supabase.co"  # Substitua com a URL do seu projeto
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl2Z2tyZnF4ZXR6cnJwZGdha2pqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NTUzODAxMywiZXhwIjoyMDYxMTE0MDEzfQ.QbQAi0Iw-lEHspFsuVCtBPLp72T2rZG9Gh1XJApWpZI"  # api key secret

# Inicializar o cliente do Supabase
supabase: Client = create_client(url, key)

def encryptInserirFilme(titulo,duracao,ano,nomeGenero,senha):#terceiro
    #nome = str_xordec(nomeGenero,senha)
    nome = nomeGenero
    idgenero = supabase.table("generos").select("id_genero").eq("nome", nome).execute()
    response = supabase.table("filmes").insert({"titulo" : titulo, "duracao" : duracao, "ano_lancamento" : ano, "id_genero" : idgenero.data[0]["id_genero"]}).execute()

def encryptInserirGenero(descricao,nome,senha):#primeiro
    senha = senha
    response = supabase.table("generos").insert({"nome" : nome, "descricao" : descricao}).execute()

def encryptInserirAvaliacao(comentario,data,nota,nomeusr,nomeSerie,nomeFilme,senha):#quinto
    #nomeus = str_xordec(nomeusr,senha)
    #nomeser = str_xordec(nomeSerie,senha)
    #nomefil = str_xordec(nomeFilme,senha)
    nomeus = nomeusr
    nomeser = nomeSerie
    nomefil = nomeFilme
    idusr = supabase.table("usuarios").select("id_usuario").eq("nome", nomeus).execute()
    idserie = supabase.table("series").select("id_serie").eq("titulo", nomeser).execute()
    idfilme = supabase.table("filmes").select("id_filme").eq("titulo", nomefil).execute()
    if idserie.data == []:
        response = supabase.table("avaliacoes").insert({"comentario" : comentario, "data_avaliacao" : data, "nota" : nota, "id_usuario" : idusr.data[0]["id_usuario"], "id_filme" : idfilme.data[0]["id_filme"]}).execute()
    else:
        response = supabase.table("avaliacoes").insert({"comentario" : comentario, "data_avaliacao" : data, "nota" : nota, "id_usuario" : idusr.data[0]["id_usuario"], "id_serie" : idserie.data[0]["id_serie"]}).execute()

def encryptInserirSerie(Ntemp,status,titulo,nomeGenero,senha):#segundo
    #nome = str_xordec(nomeGenero,senha)
    nome = nomeGenero
    idgenero = supabase.table("generos").select("id_genero").eq("nome", nome).execute()
    response = supabase.table("series").insert({"numero_temporadas" : Ntemp, "status" : status, "titulo" : titulo, "id_genero" : idgenero.data[0]["id_genero"]}).execute()

def encryptInserirAssinatura(tipo,valor,dataRenov,nome,senha):#sexto
    nomeus = str_xordec(nome,senha)
    nomeus = nome
    idusr = supabase.table("usuarios").select("id_usuario").eq("nome", nomeus).execute()
    response = supabase.table("assinaturas").insert({"tipo_plano" : tipo, "valor" : valor, "data_renovacao" : dataRenov, "id_usuario" : idusr.data[0]["id_usuario"]}).execute()

def encryptInserirUsuario(nome,data,email,senha):#quarto
    response = supabase.table("usuarios").insert({"nome" : nome, "data_nascimento" : data, "email" : email}).execute()

if __name__ == "__main__":
    encryptInserirGenero("acão e aventura", "ação")
    encryptInserirSerie(5, "ativa", "The Witcher", "ação")
    encryptInserirFilme("Vingadores", 120, 2012, "ação")
    encryptInserirUsuario("Lucas", datetime.datetime.strptime("2000-01-01","%Y-%m-%d").strftime("%Y-%m-%d"), "email@generico.com")
    encryptInserirAvaliacao("muito bom", datetime.datetime.strptime("2023-10-01","%Y-%m-%d").strftime("%Y-%m-%d"), 5, "Lucas", "", "Vingadores")
    encryptInserirAssinatura("mensal", 29.90, datetime.datetime.strptime("2023-10-01","%Y-%m-%d").strftime("%Y-%m-%d"), "Lucas")
    #data_obj = datetime.strptime(data_string, "%Y-%m-%d").date()
    #dados para testar a escrita do banco de dados