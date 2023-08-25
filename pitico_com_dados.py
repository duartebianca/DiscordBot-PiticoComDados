import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands

TOKEN = ''
SPREADSHEET_ID = ''
id_planilha_beneficio2 = ''
CREDENTIALS_FILE = ''

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.command(name='ajuda')
async def ajuda(ctx):
    embed = discord.Embed(title="O que eu posso fazer? Muita coisa! Ihuuul", description="Lista de comandos disponíveis:")
    embed.add_field(name="!oi", value="Comando para saber mais sobre mim!", inline=False)
    embed.add_field(name="!beneficio1", value="Comando para visualizar a lista de comandos ligados ao Benefício 1.", inline=False)
    embed.add_field(name="!consultar_caixa", value="Comando para verificar quanto tínhamos de saldo ao final do mês anterior nos nossos bancos, o X e o Y.", inline=False)
    embed.add_field(name="!consultar_beneficio2 <nome-completo>", value="Comando para verificar seu saldo de Benefício 2. Para pesquisar, utilize seu nome completo ou conforme escrito da planilha do Benefício 2.", inline=False)
    embed.add_field(name="!perguntas_frequentes", value="Comando para visualizar a lista de comandos relacionadas ao Benefício 3, à Benefício 1 e à própria subárea.", inline=False)

    await ctx.send(embed=embed)

@bot.command(name='beneficio1')
async def beneficio1(ctx):
    embed = discord.Embed(title="Menu - Benefício 1", description="Lista de comandos relacionados ao Benefício 1:")
    embed.add_field(name="!consultar_beneficio1 <nome-completo>", value="Comando para consultar o saldo de Benefício 1 de uma pessoa. Digite seu nome completo ou conforme na planilha do Sistema Benefício 1 (https://docs.google.com/spreadsheets/d/ID_DA_PLANILHA/).", inline=False)
    embed.add_field(name="!calcular_beneficio1 <valor>", value="Comando para calcular a Benefício 1 recebida com base no lucro do mês. Para adicionar o valor, não esqueça de usar '.' no lugar da ','. Exemplo: '!consultar_beneficio1 12.99', para consultar o Benefício 1 de um mês em que o lucro foi R$ 12,99.", inline=False)
    embed.add_field(name="!itens_beneficio1", value="Exibe uma lista a respeito de quais itens você pode utilizar seu Benefício 1.", inline=False)
    embed.add_field(name="!status_beneficio1", value="Permite verificar se o Benefício 1 está congelado ou liberado. A depender da situação do caixa da [Empresa], ou seja, quanto dinheiro temos nas contas bancárias, podemos congelar temporariamente o Benefício 1 para garantir que [a Empresa] não fique sem recursos financeiros.", inline=False)
    await ctx.send(embed=embed)

@bot.command(name='dados&finanças')
async def dados_financas_command(ctx):
    embed = discord.Embed(title="Sobre a Subárea", description="[Escopo de Subárea]")
    embed.add_field(name="[Cargo 1]", value="[Escopo de Cargo 1]", inline=False)
    embed.add_field(name="[Cargo 2]", value="[Escopo de Cargo 2]", inline=False)
    embed.add_field(name="[Cargo 3]", value="[Escopo de Cargo 3]", inline=False)
    await ctx.send(embed=embed)

@bot.command(name='perguntas_frequentes')
async def perguntas_frequentes_command(ctx):
    embed = discord.Embed(title="Perguntas Frequentes", description="Algumas dúvidas que normalmente surgem sobre a subárea, Benefício 3 e Benefício 1.")
    embed.add_field(name="Inteligência de Dados & Finanças", value="Para saber mais sobre a subárea, utilize o !dados&finanças. Isso exibirá o escopo da área e os cargos, além de um link para a página do Notion que explica Inteligência de Dados & Finanças.", inline=False)
    embed.add_field(name="Benefício 3", value="Reembolsos de Benefício 3: solicitação até o X dia do mês, valor de Y, uso Z. Link para solicitar reembolsos em 2023: [LINK].\nNão é acumulativo, mas você pode solicitar adiantamento.\nVocê pode utilizar mais de um benefício para fazer um reembolso.\nSe o valor da nota for maior que o valor que você tiver disponível para fazer a compra (Exemplo: Nota de R$172,00, benefício com R$60,00 restantes), adicione o valor disponível no campo de valor do formulário (Ou seja, coloque R$ 60,00, não R$ 172,00).", inline=False)
    embed.add_field(name="Benefício 1", value="O Benefício 1 deve ser sempre solicitada ao time. Você pode fazer consultas, como os itens permitidos, seu saldo e o status da Benefício 1, dentre outras coisas, utilizando !beneficio1. Em caso de pedir para que se pague um boleto, lembre-se de se certificar que a nota fiscal será emitida. Você pode fazer pedidos de Benefício 1 utilizando o cartão ou com notas em nome de outras pessoas, mas é necessário enviar uma cópia da identidade dessa pessoa. Por isso, é recomendado que seja no seu nome ou no de parentes próximos.", inline=False)
    embed.add_field(name="✅ Boas Práticas - Pedido de Reembolso", value="Evitar extensões de arquivo que não sejam compatíveis com todos os dispositivos;\nNomear, se possível, os arquivos como reembolso_seunome_motivo ou como algo descritivo;\nQuando possível, pedir no mesmo card de reembolso, a não ser que sejam itens muito distintos/nem todos tenham sido aprovados;\nColocar o valor exato do seu reembolso, não arredondar.", inline=False)
    await ctx.send(embed=embed)
  
@bot.command(name='oi')
async def hello_command(ctx):
    await ctx.send('Oi! Meu nome é Pitico. Você deve conhecer minha versão de pelúcia. Trago consultas sobre Dinheiros e outras informações. Para saber tudo que eu posso fazer, peça !ajuda.\n')

@bot.command(name='itens_beneficio1')
async def itens_beneficio1_command(ctx):
    embed = discord.Embed(title="Quais itens eu posso comprar com meu Benefício 1?", description="O Benefício 1 possui algumas diretrizes e requer que os produtos sejam acompanhados de nota fiscal. Caso o item desejado não esteja listado abaixo, é necessário consultar o time de Inteligência de Dados & Finanças para obter a aprovação correspondente.")
    embed.add_field(name="[Lista 1]", value="Item 1; Item 2; Item 3; [...]; Item n.", inline=False)
    embed.add_field(name="[Lista 2]", value="Item 1; Item 2; Item 3; [...]; Item n.", inline=False)
    embed.add_field(name="[Lista 3]", value="Item 1; Item 2; Item 3; [...]; Item n.", inline=False)
    embed.add_field(name="[Lista 4]", value="Item 1; Item 2; Item 3; [...]; Item n.", inline=False)
    embed.add_field(name="Outros", value="Item 1; Item 2; Item 3; [...]; Item n.", inline=False)
    await ctx.send(embed=embed)

@bot.command(name='status_beneficio1')
async def status_beneficio1_command(ctx):
  status_da_beneficio1 = consulta_status_beneficio1()
  await ctx.send(f'Atualmente, o Benefício 1 está {status_da_beneficio1}.')

@bot.command(name='consultar_caixa')
async def consultar_caixa_command(ctx):
  valor_caixa = consulta_valor_caixa()
  await ctx.send(f'No mês anterior, nosso caixa fechou com R${valor_caixa}.')

@bot.command(name='consultar_beneficio1')
async def consultar_beneficio1_command(ctx, *args):
  nome_completo = ' '.join(args)
  saldo = consultar_saldo_Benefício 1(nome_completo)
  if saldo is not None:
      await ctx.send(f'O saldo de Benefício 1 de {nome_completo} é: {saldo}.')
  else:
      await ctx.send(f'Não foi encontrado saldo de Benefício 1 para {nome_completo} na planilha.')

@bot.command(name='consultar_beneficio2')
async def consultar_beneficio2_command(ctx, *args):
  seu_nome_completo = ' '.join(args)
  saldo_beneficio2 = consultar_beneficio2_reparo(seu_nome_completo)
  if saldo_beneficio2 is not None:
      await ctx.send(f'O saldo do Benefício 2 de {seu_nome_completo} é: {saldo_beneficio2}. Esse valor é válido até o final da gestão.')
  else:
      await ctx.send(f'Não foi encontrado saldo de Benefício 2 para {seu_nome_completo} na planilha.')

@bot.command(name='calcular_beneficio1')
async def calcular_beneficio1_command(ctx, valor_em_texto):
  valor = float(valor_em_texto)
  hierarquia3, hierarquia1, hierarquia2 = calcula_beneficio1_total(valor)
  await ctx.send(f'Com um lucro líquido de R${valor: .2f} no mês, cada pessoa recebe:\n'+ f'Hierarquia 1: R${hierarquia1: .2f}\n' + f'Hierarquia 2: R${hierarquia2: .2f}\n' + f'Hierarquia 3: R${hierarquia 3: .2f}\n')
  
def consultar_saldo_beneficio1(nome_completo):
    # Autenticação no Google Sheets
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scopes=scope)
    client = gspread.authorize(credentials)

    # Acesso à planilha
    planilha = client.open_by_key(SPREADSHEET_ID)
    guia = planilha.worksheet('PESSOAS')  # A 27ª guia (índice 26)
    nomes = guia.col_values(1)  # Coluna A contendo os nomes
    saldos_Benefício 1 = guia.col_values(29)  # Coluna AC contendo os saldos de Benefício 1
    # Encontrar o saldo de Benefício 1 com base no nome
    if nome_completo in nomes:
        indice = nomes.index(nome_completo) + 1
        saldo = saldos_Benefício 1[indice - 1]
        return saldo
    elif nome_completo not in nomes:
      return None

def calcula_beneficio1_total (lucro_mes:float) -> float:
  scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scopes=scope)
  client = gspread.authorize(credentials)
  
  planilha = client.open_by_key(SPREADSHEET_ID)
  
  #linkado com worksheet 'Nova Benefício 1 (23.1)'
  guia = planilha.worksheet('Nova Benefício 1 (23.1)')
  
  Benefício 1 = lucro_mes * 0.2
  
  qtd_op = guia.acell('Q15').numeric_value
  qtd_di = guia.acell('Q13').numeric_value
  qtd_on = guia.acell('Q14').numeric_value
  
  op_weight = guia.acell('Q4').numeric_value
  di_weight = guia.acell('Q2').numeric_value
  on_weight = guia.acell('Q3').numeric_value
  
  base = qtd_op * op_weight + qtd_di * di_weight + qtd_on * on_weight
  
  brl_per_base = Benefício 1/base
  
  dest_op = brl_per_base * op_weight
  dest_di = brl_per_base * di_weight
  dest_on = brl_per_base * on_weight
  
  return dest_op, dest_di, dest_on 

def consulta_status_beneficio1():
  scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scopes=scope)
  client = gspread.authorize(credentials)
  # Acesso à planilha
  planilha = client.open_by_key(SPREADSHEET_ID)
  guia = planilha.worksheet('Infos_adicionais')
  
  status = guia.acell('A2').value  # Obtendo o valor da célula A2
  return status

def consultar_beneficio2(seu_nome_completo):
  scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scopes=scope)
  client = gspread.authorize(credentials)
  # Acesso à planilha
  planilha = client.open_by_key(id_planilha_beneficio2)
  guia = planilha.worksheet('2023.2')
  
  nomes = guia.col_values(1)  # Coluna A contendo os nomes
  saldos_beneficio2 = guia.col_values(4) 
    # Encontrar o saldo de Benefício 2 com base no nome
  if seu_nome_completo in nomes:
    indice = nomes.index(seu_nome_completo) + 1
    saldo = saldos_beneficio2[indice - 1]
    return saldo
  elif seu_nome_completo not in nomes:
    return None

def consulta_valor_caixa():
  scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scopes=scope)
  client = gspread.authorize(credentials)
  # Acesso à planilha
  planilha = client.open_by_key(SPREADSHEET_ID)
  guia = planilha.worksheet('Infos_adicionais')   # Chamando planilha pelo id unico
  status = guia.acell('B2').value  # Obtendo o valor da célula A2
  return status


bot.run(TOKEN)
