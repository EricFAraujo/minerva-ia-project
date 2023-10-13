import datetime
import pytz
import speech_recognition as sr
import pyttsx3
import wikipedia
import spacy

audio = sr.Recognizer()
maquina = pyttsx3.init()
nlp = spacy.load('pt_core_news_sm')

# Definir o fuso horário
fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')

hora_atual_brasilia = datetime.datetime.now(fuso_horario_brasilia)

# Gravação de usuário
nome_usuario = input("Por favor, insira seu nome: ")

# Definir as saudações com base no horário
if 6 <= hora_atual_brasilia.hour < 12:
    saudacao = "Bom dia"
elif 12 <= hora_atual_brasilia.hour < 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

# Horário de atividades
horario_cafe_manha = hora_atual_brasilia.replace(hour=7, minute=0, second=0)
horario_trabalho = hora_atual_brasilia.replace(hour=8, minute=0, second=0)
horario_almoco_inicio = hora_atual_brasilia.replace(hour=12, minute=0, second=0)
horario_almoco_fim = horario_almoco_inicio + datetime.timedelta(hours=1)
horario_estudo = hora_atual_brasilia.replace(hour=16, minute=0, second=0)
horario_sono = hora_atual_brasilia.replace(hour=22, minute=0, second=0)

# IA informa as atividades conforme o horário
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

# Função para fazer uma pergunta e obter uma resposta
def perguntar(texto):
    doc = nlp(texto)
    if doc.cats["response"] > 0.5:
        return doc.text
    else:
        return "Desculpe, não entendi a pergunta."

def executa_comando():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language="pt-BR")
            comando = comando.lower()
            if "minerva" in comando:
                comando = comando.replace("minerva", "")
                return comando
    except sr.RequestError as e:
        print(f"Não foi possível obter resultados de reconhecimento de fala; {e}")
    except sr.UnknownValueError:
        print("Não foi possível entender a fala.")
    except Exception as ex:
        print(f"Ocorreu um erro durante o reconhecimento de fala: {ex}")
    return ""

def comando_voz_usuario():
    comando = executa_comando()
    if "horas" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        maquina.say("Agora são " + hora)
        maquina.runAndWait()
    elif "procure por" in comando:
        termo_pesquisa = comando.replace("procure por", "")
        try:
            wikipedia.set_lang("pt")
            resultados = wikipedia.summary(termo_pesquisa, sentences=2)
            maquina.say(resultados)
            maquina.runAndWait()
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Houve um erro de desambiguação: {e}")
            maquina.say("Houve um erro ao buscar o termo. Por favor, seja mais específico.")
            maquina.runAndWait()
        except wikipedia.exceptions.PageError as e:
            print(f"Erro de página: {e}")
            maquina.say("Nada foi encontrado para o termo pesquisado.")
            maquina.runAndWait()

print(mensagem_apresentacao)
saudacao_personalizada = f"{saudacao}, {nome_usuario}!"
print(saudacao_personalizada)
print("Neste momento:", atividade_atual)
comando_voz_usuario()

    

