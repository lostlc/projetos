#calculando a idade de uma pessoa em python...
print("******Qual sua idade?******")

from datetime import datetime

def calcular_idade(ano_nascimento, mes_nascimento, dia_nascimento):
  """Calcula a idade com base na data de nascimento.

  Args:
    ano_nascimento: O ano de nascimento.
    mes_nascimento: O mês de nascimento.
    dia_nascimento: O dia de nascimento.

  Returns:
    A idade em anos.
  """
  data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
  data_atual = datetime.now()
  idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
  return idade

# Solicita a data de nascimento ao usuário
ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
dia = int(input("Digite o dia de nascimento: "))

# Calcula a idade
idade = calcular_idade(ano, mes, dia)

# Imprime a idade
print(f"A idade é: {idade} anos")