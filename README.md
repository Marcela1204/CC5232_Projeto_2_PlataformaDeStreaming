<div align="center">
  
# PLATAFORMA DE STREAMING
## PROJETO 2: BANCO DE DADOS

</div>
<br>

## Introdução
Projeto criado por:
* [Lucas Kerr](https://github.com/Adelgrin) | RA: 221230329
* [Marcela Nalesso](https://github.com/Marcela1204) | RA: 222220113

* Link do git hub: https://github.com/Marcela1204/CC5232_Projeto_2_PlataformaDeStreaming
* Link do git hub2: https://github.com/Marcela1204/CC5232_Projeto_2_PlataformaDeStreaming.git
<br>

## Descrição do Projeto
- **Objetivo**   
> Desenvolver um sistema de banco de dados para uma plataforma de streaming, com foco na gestão de conteúdos audiovisuais e interação dos usuários. O sistema deverá contemplar as seguintes entidades principais: Usuário, Filme, Série, Gênero, Avaliação e Assinatura.
<br>

- **Tabelas**   
> O banco de dados deverá conter as seguintes informações:   
1. Usuário: id_usuario, nome, e-mail e data de nascimento.   
2. Filme: id_filme, título, duração e ano de lançamento.   *
3. Série: id_serie, título, número de temporadas e status (ativa ou finalizada).   
4. Gênero: id_genero, nome e descrição.   
5. Avaliação: id_ avaliacao, nota, comentário e data da avaliação.   *
6. Assinatura: id_assinatura, tipo de plano, valor e data de renovação.
<br>

> O modelo de dados incluirá relacionamentos do tipo muitos-para-muitos entre:
1. Filmes e Gêneros: um filme pode estar associado a múltiplos gêneros e um gênero pode agrupar diversos filmes.
2. Séries e Gêneros: uma série pode estar associado a múltiplos gêneros e um gênero pode agrupar diversas séries.
<br>

- **Queries** 
> Para demonstrar o funcionamento do banco, foram usadas as seguintes queries:   
1. Listar os usuários com suas assinaturas
2. Mostrar os usuários que fizeram avaliações e o conteúdo avaliado
3. Exibir filmes com suas avaliações e notas médias
4. Listar séries com o número de avaliações
5. Obter os gêneros e quantos conteúdos (filmes ou séries) estão associados a cada um
6. Listar todos os usuários com suas notas e comentários em filmes
7. Listar usuários que avaliaram séries finalizadas
8. Mostrar usuários com sua assinatura e média das notas dadas
9. Filmes com avaliações negativas (< 5) e os usuários que avaliaram
10. Séries ativas com avaliações, nomes dos usuários e notas
<br>


## Execução do Projeto
Passo a passo para exceutar o projeto: 

### Primeiro passo: Instalar bibliotecas 'Python', 'Faker' e 'Supabase'
- Abra o arquivo criarPopularTabela.py no Codespace do Github e instale as três bibliotecas.

### Segundo passo: Verificar URL e KEY do seu banco
- Copie e cole as chaves URL e KEY do seu banco no supabase (localização detalhada no tutorial abaixo) e substitua nas váriàveis url e key do código.
> Dica: Crie seu próprio banco de dados para que não haja problema com permissão no ‘service role’ ao rodar o código!

### Terceiro passo: Execução do código
- Execute o código e, após aparecer a mensagem 'concluído', é possível localizar os dados no banco!
<br>
<div align="center">
  
**ASSISTA O VÍDEO TUTORIAL ABAIXO**
(Teremos um tutorial)


</div>
<br>

## Diagramas

### MER
![image](https://github.com/user-attachments/assets/8d091870-6b6d-44f8-8e05-8c4dc23c0a74)


### MR
![image](https://github.com/user-attachments/assets/2646c4fb-80cb-4a69-bc1a-07a36b7915d5)






***

