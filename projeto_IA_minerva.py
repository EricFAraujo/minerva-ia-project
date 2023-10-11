import datetime
import pytz
import spacy

# Passo 1: Definir o fuso horário
fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')

hora_atual_brasilia = datetime.datetime.now(fuso_horario_brasilia)

# Passo 2: Gravação de usuário
nome_usuario = input("Por favor, insira seu nome: ")

# Passo 3: definir as saudações com base no horário
if 6 <= hora_atual_brasilia.hour < 12:
    saudacao = "Bom dia"
elif 12 <= hora_atual_brasilia.hour < 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

# Passo 4: Horário de atividades
horario_cafe_manha = hora_atual_brasilia.replace(hour=7, minute=0, second=0)
horario_trabalho = hora_atual_brasilia.replace(hour=8, minute=0, second=0)
horario_almoco_inicio = hora_atual_brasilia.replace(hour=12, minute=0, second=0)
horario_almoco_fim = horario_almoco_inicio + datetime.timedelta(hours=1)
horario_estudo = hora_atual_brasilia.replace(hour=16, minute=0, second=0)
horario_sono = hora_atual_brasilia.replace(hour=22, minute=0, second=0)

# Passo 5: IA informa as atividades conforme o horário
# Aqui a IA verificará a atividade conforme o horário
atividade_atual = ""
if hora_atual_brasilia < horario_cafe_manha:
    atividade_atual = "É hora do dormir bebê!"
elif horario_cafe_manha <= hora_atual_brasilia < horario_trabalho:
    atividade_atual = "É hora de tomar seu café da manhã."
elif horario_trabalho <= hora_atual_brasilia < horario_almoco_inicio:
    atividade_atual = "Hora de ir trabalhar."
elif horario_almoco_inicio <= hora_atual_brasilia < horario_almoco_fim:
    atividade_atual = "Hora do almoço."
elif horario_almoco_fim <= hora_atual_brasilia < horario_estudo:
    atividade_atual = "Tempo após o almoço"
elif horario_estudo <= hora_atual_brasilia < horario_sono:
    atividade_atual = "É hora de estudar guerreiro"
else:
    atividade_atual = "É hora de dormir feito um bebê"

# Saudação e apresentação da Minerva
nome_IA = "Minerva"
mensagem_apresentacao = f"Olá, eu me chamo {nome_IA}! Fui criada pelo Eric para auxiliá-lo, inicialmente, com afazeres simples do dia-a-dia. Pretendo ser aprimorada todos os dias para que possa me tornar mais eficiente."

# Treinamento do modelo NLP
# Aqui você pode adicionar o código para treinar o modelo NLP usando spaCy

# Função para fazer uma pergunta e obter uma resposta
def perguntar(texto):
    doc = nlp(texto)
    if doc.cats["response"] > 0.5:
        return doc.text
    else:
        return "Desculpe, não entendi a pergunta."

# Exibir a saudação personalizada e a atividade correspondente
print(mensagem_apresentacao)
saudacao_personalizada = f"{saudacao}, {nome_usuario}!"
print(saudacao_personalizada)
print("Neste momento:", atividade_atual)

# Interação com a Minerva
while True:
    pergunta = input("Faça uma pergunta (ou 'sair' para encerrar): ")
    if pergunta.lower() == "sair":
        break
    resposta = perguntar(pergunta)
    print("Minerva:", resposta)

    

