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



