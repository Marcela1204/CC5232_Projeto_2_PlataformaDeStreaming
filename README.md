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
O modelo de dados incluirá relacionamentos do tipo muitos-para-muitos entre:
1. Filmes e Gêneros: um filme pode estar associado a múltiplos gêneros e um gênero pode agrupar diversos filmes.
2. Usuários e Avaliações: cada usuário pode realizar múltiplas avaliações e cada conteúdo pode ser avaliado por vários usuários.
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

- **Queries** 
> Para demonstrar o funcionamento do banco, foram usadas as seguintes queries:   
1.  
2.  
3.    
4.   
5. 
6. 
7. 
8. 
9. 
10. 
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
![image](https://github.com/user-attachments/assets/f1f1a83d-8876-4714-94d1-1dc7f682ca83)

### MR
![image](https://github.com/user-attachments/assets/bafacdac-17aa-48fb-963e-83c267e08c8e)





***

