# Importando bibliotecas usuais para análise de Dados
import pandas as pd
import plotly.express as px
import openai
OPENAI_API_KEY = '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'

# Extração e leitura do banco de dados em Excel
caminho_arquivo = r"C:\Users\T-Gamer\Desktop\Bootcamp-Santander\BootcampPython\Desafio_projeto1\Dados\RODRIGO.xlsx"
banco_de_dados = pd.read_excel(caminho_arquivo)

# Tratamento de dados do banco
banco_de_dados = banco_de_dados.dropna()
banco_de_dados.rename(columns={"Unnamed: 2": "Valor", "PLANILHA DE CONTROLE DE DESPESAS": "Dia"}, inplace=True)

def criar_grafico():
    grafico = px.histogram(banco_de_dados, x="Dia", y="Valor", text_auto = True)
    grafico.show()

#criar_grafico()
openai.api_key = OPENAI_API_KEY

def generate_ai_news():
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em Finanças"
      },
      {
          "role": "user",
          "content": "Crie uma mensagem para Ricardo sobre a importancia do dinheiro e dê dicas de como melhorar no controle de gastos"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

mensagem_gerada = generate_ai_news()
print(mensagem_gerada)

#Percepção pelo gráfico, um grande gasto no inicio e fim do mês. Porem uma queda enorme no meio do mês.