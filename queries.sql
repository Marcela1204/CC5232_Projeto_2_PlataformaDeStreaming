-- Listar os usuários com suas assinaturas
SELECT u.id_usuario, u.nome, u.email, a.tipo_plano, a.valor, a.data_renovacao
FROM usuarios u
LEFT JOIN assinaturas a ON u.id_usuario = a.id_usuario;


-- Mostrar os usuários que fizeram avaliações e o conteúdo avaliado
SELECT u.nome AS usuario, 
       f.titulo AS filme, 
       s.titulo AS serie, 
       a.nota, a.comentario, a.data_avaliacao
FROM avaliacoes a
JOIN usuarios u ON u.id_usuario = a.id_usuario
LEFT JOIN filmes f ON a.id_filme = f.id_filme
LEFT JOIN series s ON a.id_serie = s.id_serie;


-- Exibir filmes com suas avaliações e notas médias
SELECT f.titulo, 
       AVG(a.nota) AS media_nota, 
       COUNT(a.id_avaliacao) AS total_avaliacoes
FROM filmes f
LEFT JOIN avaliacoes a ON f.id_filme = a.id_filme
GROUP BY f.titulo;


-- Listar séries com o número de avaliações
SELECT s.titulo, COUNT(a.id_avaliacao) AS total_avaliacoes
FROM series s
LEFT JOIN avaliacoes a ON s.id_serie = a.id_serie
GROUP BY s.titulo;


-- Obter os gêneros e quantos conteúdos (filmes ou séries) estão associados a cada um
SELECT g.nome AS genero,
       COUNT(DISTINCT f.id_filme) AS total_filmes,
       COUNT(DISTINCT s.id_serie) AS total_series
FROM generos g
LEFT JOIN filmes f ON g.id_genero = f.id_genero
LEFT JOIN series s ON g.id_genero = s.id_genero
GROUP BY g.nome;


-- Listar todos os usuários com suas notas e comentários em filmes
SELECT u.nome, f.titulo AS filme, a.nota, a.comentario
FROM avaliacoes a
JOIN usuarios u ON u.id_usuario = a.id_usuario
JOIN filmes f ON f.id_filme = a.id_filme;


-- Listar usuários que avaliaram séries finalizadas
SELECT DISTINCT u.nome, s.titulo AS serie, a.nota
FROM avaliacoes a
JOIN usuarios u ON u.id_usuario = a.id_usuario
JOIN series s ON s.id_serie = a.id_serie
WHERE s.status = 'finalizada';


-- Mostrar usuários com sua assinatura e média das notas dadas
SELECT u.nome, a.tipo_plano, a.valor, AVG(av.nota) AS media_notas
FROM usuarios u
LEFT JOIN assinaturas a ON a.id_usuario = u.id_usuario
LEFT JOIN avaliacoes av ON av.id_usuario = u.id_usuario
GROUP BY u.nome, a.tipo_plano, a.valor;


-- Filmes com avaliações negativas (< 5) e os usuários que avaliaram
SELECT f.titulo AS filme, u.nome AS usuario, a.nota, a.comentario
FROM avaliacoes a
JOIN usuarios u ON u.id_usuario = a.id_usuario
JOIN filmes f ON f.id_filme = a.id_filme
WHERE a.nota < 5;


-- Séries ativas com avaliações, nomes dos usuários e notas
SELECT s.titulo AS serie, u.nome AS usuario, a.nota, a.comentario
FROM avaliacoes a
JOIN series s ON s.id_serie = a.id_serie
JOIN usuarios u ON u.id_usuario = a.id_usuario
WHERE s.status = 'ativa';
