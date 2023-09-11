# Bot do Discord Pitico Com Dados

## 🎯 Objetivo

Este bot foi projetado para auxiliar em várias funções relacionadas à estratégia e transparência financeira dentro da empresa. Ele integra-se ao Google Sheets para fornecer acesso em tempo real a dados financeiros e oferece comandos para interagir com esses dados.

## 🖥 Tecnologias Utilizadas

O bot do Discord Pitico Com Dados foi construído utilizando as seguintes tecnologias:

- Python
- [discord.py](https://discordpy.readthedocs.io/en/stable/) para criar o bot do Discord
- [gspread](https://gspread.readthedocs.io/en/latest/) para interagir com o Google Sheets
- [oauth2client](https://oauth2client.readthedocs.io/en/latest/) para lidar com a autenticação OAuth2
- [Google Sheets](https://www.google.com/sheets) para armazenar e gerenciar dados financeiros

## 📜 Comandos do Bot

### Comandos Gerais

- `!oi`: Receba uma introdução amigável do Pitico, o bot.
- `!ajuda`: Exiba uma lista de comandos disponíveis e suas descrições.

### Comandos do Benefício 1

- `!beneficio1`: Mostre um menu de comandos relacionados ao Benefício 1.
- `!consultar_beneficio1 <nome-completo>`: Verifique o saldo do Benefício 1 de uma pessoa fornecendo seu nome completo.
- `!calcular_beneficio1 <valor>`: Calcule a distribuição do Benefício 1 com base no lucro mensal. Exemplo: `!calcular_beneficio1 12.99`.
- `!itens_beneficio1`: Exiba uma lista de itens que podem ser comprados com o Benefício 1.
- `!status_beneficio1`: Verifique o status atual do Benefício 1.

### Comandos do Benefício 2

- `!consultar_beneficio2 <nome-completo>`: Verifique o saldo do Benefício 2 de uma pessoa fornecendo seu nome completo.

### Comandos de Transparência Financeira

- `!consultar_caixa`: Verifique o saldo de fechamento do mês anterior nas contas bancárias da empresa.

### Perguntas Frequentes

- `!perguntas_frequentes`: Obtenha respostas para perguntas frequentes relacionadas à subárea, Benefício 3 e Benefício 1.

## ⁉ Como Usar

1. Clone este repositório.
2. Instale as dependências listadas no arquivo `requirements.txt`.
3. Obtenha o token do seu bot e insira no código.
4. Insira os IDs das planilhas em `SPREADSHEET_ID` e `id_planilha_beneficio2`.
5. Obtenha as credenciais na Google Cloud Plataform.
6. Execute o bot através do comando `python nome_do_arquivo.py`.
   
Para obter os itens 3, 4, 5, verifique as instruções disponíveis neste [pdf](https://github.com/duartebianca/DiscordBot-PiticoComDiversidade/blob/main/como_criar_bot_discord.pdf).

## ➕ Informações Adicionais

- O bot se conecta ao Google Sheets para acessar dados financeiros, portanto, certifique-se de que os IDs e credenciais do Google Sheets estejam configurados corretamente.
- Para qualquer problema técnico ou dúvida sobre a funcionalidade do bot, entra em contato comigo :).

Aproveite o uso do Pitico Com Dados, seu assistente de transparência financeira e estratégia!
