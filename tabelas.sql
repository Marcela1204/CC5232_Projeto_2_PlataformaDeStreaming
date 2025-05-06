CREATE SCHEMA IF NOT EXISTS public;
SET search_path TO public;

-- Tabela Usuário
create table usuarios (
    id_usuario serial primary key,
    nome varchar(100) not null,
    email varchar(100) not null unique,
    data_nascimento date not null
);

-- Tabela Gênero
create table generos (
    id_genero serial primary key,
    nome varchar(100) not null unique,
    descricao text not null
);

-- Tabela Filme
create table filmes (
    id_filme serial primary key,
    titulo varchar(200) not null,
    genero text,
    duracao integer not null,  -- Duração em minutos
    ano_lancamento integer not null,
    id_genero integer references generos(id_genero)
);

-- Tabela Série
create table series (
    id_serie serial primary key,
    titulo varchar(200) not null,
    numero_temporadas integer not null,
    genero text,
    status varchar(20) not null check (status in ('ativa', 'finalizada')),
    id_genero integer references generos(id_genero)
    
);

-- Tabela Avaliação
create table avaliacoes (
    id_avaliacao serial primary key,
    nota integer not null check (nota >= 1 and nota <= 10), -- Nota de 1 a 10
    comentario text,
    data_avaliacao timestamp,
    usuario text,
    id_usuario integer references usuarios(id_usuario),
    id_serie integer references series(id_serie),
    id_filme integer references filmes(id_filme)
);

-- Tabela Assinatura
create table assinaturas (
    id_assinatura serial primary key,
    usuario text,
    tipo_plano varchar(50) not null,  -- Exemplo: "mensal", "anual"
    valor numeric(10, 2) not null,  -- Valor da assinatura
    data_renovacao date not null,
    id_usuario integer references usuarios(id_usuario)
);
