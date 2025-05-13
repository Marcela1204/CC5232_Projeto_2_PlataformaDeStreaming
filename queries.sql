-- Listar os 10 filmes mais bem avaliados (com média de nota)
SELECT f.titulo, ROUND(AVG(a.nota), 2) AS media_nota
FROM filmes f
JOIN avaliacoes a ON f.id_filme = a.id_filme
GROUP BY f.id_filme, f.titulo
ORDER BY media_nota DESC
LIMIT 10;

-- Listar todas as séries ativas com mais de 3 temporadas
SELECT titulo, numero_temporadas
FROM series
WHERE status = 'ativa' AND numero_temporadas > 3;

-- Listar os filmes com sua classificação indicativa mais alta (caso tenha múltiplos gêneros)
SELECT f.titulo, MAX(gf.classificacao_indicativa) AS classificacao_max
FROM filmes f
JOIN genero_filme gf ON f.id_filme = gf.id_filme
GROUP BY f.id_filme, f.titulo;

-- Listar os usuários e seus planos com valor e desconto
SELECT u.nome, u.email, s.tipo_plano, s.valor, p.desconto
FROM usuarios u
JOIN planos p ON u.id_plano = p.id_plano
JOIN assinaturas s ON p.id_assinatura = s.id_assinatura;

-- Contar quantos usuários há por tipo de plano
SELECT s.tipo_plano, COUNT(*) AS qtd_usuarios
FROM usuarios u
JOIN planos p ON u.id_plano = p.id_plano
JOIN assinaturas s ON p.id_assinatura = s.id_assinatura
GROUP BY s.tipo_plano;

-- Listar os usuários que nunca fizeram uma avaliação
SELECT u.nome, u.email
FROM usuarios u
LEFT JOIN avaliacoes a ON u.id_usuario = a.id_usuario
WHERE a.id_avaliacao IS NULL;

-- Média de nota por gênero de filmes
SELECT g.nome AS genero, ROUND(AVG(a.nota), 2) AS media_nota
FROM generos g
JOIN genero_filme gf ON g.id_genero = gf.id_genero
JOIN avaliacoes a ON gf.id_filme = a.id_filme
GROUP BY g.nome;

-- Comentários recentes (últimos 7 dias) com nome do usuário e título da obra
SELECT u.nome, COALESCE(f.titulo, s.titulo) AS titulo, a.comentario, a.data_avaliacao
FROM avaliacoes a
JOIN usuarios u ON a.id_usuario = u.id_usuario
LEFT JOIN filmes f ON a.id_filme = f.id_filme
LEFT JOIN series s ON a.id_serie = s.id_serie
WHERE a.data_avaliacao >= CURRENT_DATE - INTERVAL '7 days'
ORDER BY a.data_avaliacao DESC;

-- Obter a quantidade de avaliações por usuário
SELECT u.nome, COUNT(a.id_avaliacao) AS total_avaliacoes
FROM usuarios u
LEFT JOIN avaliacoes a ON u.id_usuario = a.id_usuario
GROUP BY u.id_usuario, u.nome
ORDER BY total_avaliacoes DESC;

-- Total de filmes e séries por gênero
SELECT g.nome,
       COUNT(DISTINCT gf.id_filme) AS total_filmes,
       COUNT(DISTINCT gs.id_serie) AS total_series
FROM generos g
LEFT JOIN genero_filme gf ON g.id_genero = gf.id_genero
LEFT JOIN genero_serie gs ON g.id_genero = gs.id_genero
GROUP BY g.nome;

-- Valor total arrecadado com os planos (considerando todos os usuários)
SELECT SUM(s.valor * (1 - p.desconto)) AS total_arrecadado
FROM usuarios u
JOIN planos p ON u.id_plano = p.id_plano
JOIN assinaturas s ON p.id_assinatura = s.id_assinatura;

-- Filmes lançados após 2020 com média de avaliação maior que 2
SELECT f.titulo, f.ano_lancamento, ROUND(AVG(a.nota), 2) AS media
FROM filmes f
JOIN avaliacoes a ON f.id_filme = a.id_filme
WHERE f.ano_lancamento > 2000
GROUP BY f.id_filme, f.titulo, f.ano_lancamento
HAVING AVG(a.nota) > 2;
