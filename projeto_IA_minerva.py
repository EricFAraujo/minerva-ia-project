import datetime
import pytz
import speech_recognition as sr
import pyttsx3
import wikipedia
import spacy
import webbrowser

# Variável global para armazenar o nome do usuário
nome_usuario = ""

audio = sr.Recognizer()
maquina = pyttsx3.init()
nlp = spacy.load('pt_core_news_sm')

# Flag para verificar se a apresentação já foi feita
apresentacao_feita = False

# Função para inserir o nome do usuário uma vez
def inserir_nome():
    global nome_usuario
    nome_usuario = input("Por favor, insira seu nome: ")
    saudacao = determinar_saudacao()  # Utiliza a função para determinar a saudação dinâmica
    maquina.say(f"{saudacao}, {nome_usuario}! Bem-vindo à Minerva.")
    maquina.runAndWait()

# Função para determinar a saudação com base no horário atual
def determinar_saudacao():
    hora_atual = datetime.datetime.now().hour
    if 6 <= hora_atual < 12:
        return "Bom dia"
    elif 12 <= hora_atual < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

# Função para apresentação inicial da Minerva
def apresentacao_minerva():
    maquina.say("Olá, eu sou a Minerva, sua assistente virtual. Fui projetada para ajudá-lo em tarefas diárias e responder a perguntas. Como posso ajudar você hoje?")
    maquina.runAndWait()

# Função para fazer uma pergunta e obter uma resposta
def perguntar(texto):
    doc = nlp(texto)
    if doc.cats["response"] > 0.5:
        return doc.text
    else:
        return "Desculpe, não entendi a pergunta."

# Função para executar os comandos de voz do usuário
def executa_comando():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language="pt-BR")
            comando = comando.lower()
            return comando
    except sr.RequestError as e:
        print(f"Não foi possível obter resultados de reconhecimento de fala; {e}")
    except sr.UnknownValueError:
        print("Não foi possível entender a fala.")
    except Exception as ex:
        print(f"Ocorreu um erro durante o reconhecimento de fala: {ex}")
    return ""

# Função para executar os comandos do usuário
def comando_voz_usuario():
    global nome_usuario
    global apresentacao_feita
    # Se o nome do usuário não estiver definido, solicita o nome
    if not nome_usuario:
        inserir_nome()
    # Restante do código...
    while True:
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
        elif "abrir youtube" in comando:
            webbrowser.open("https://www.youtube.com")
            maquina.say("Abrindo o YouTube.")
            maquina.runAndWait()
        elif "abrir playlist" in comando:
            playlist_url = "https://www.youtube.com/watch?v=GTT1GkJV2hU"
            webbrowser.open(playlist_url)
            maquina.say("Abrindo a playlist no YouTube.")
            maquina.runAndWait()
        elif "até logo minerva" in comando:
            maquina.say("Foi ótimo falar com você, até breve.")
            maquina.runAndWait()
            break  # Sai do loop e encerra a conversa
        elif "me fale sobre você" in comando:
            apresentacao_minerva()  # Adiciona a apresentação da Minerva quando solicitada pelo usuário
        else:
            maquina.say("Desculpe, não entendi o comando.")
            maquina.runAndWait()

# Exemplo de chamada da função comando_voz_usuario
comando_voz_usuario()

