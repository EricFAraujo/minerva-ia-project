import datetime
import pytz
import speech_recognition as sr
import pyttsx3
import wikipedia
import spacy
import webbrowser
import random
import torch

# Variável global para armazenar o nome do usuário
nome_usuario = ""

audio = sr.Recognizer()
maquina = pyttsx3.init()
nlp = spacy.load('pt_core_news_sm')

# Flag para verificar se a apresentação já foi feita
apresentacao_feita = False

class EstimulacaoCognitiva:
    def __init__(self):
        self.sequencia_numeros = []
        self.pontuacao = 0

    def gerar_sequencia(self, comprimento):
        # Gera uma sequência aleatória de números
        self.sequencia_numeros = [random.randint(1, 9) for _ in range(comprimento)]
        return self.sequencia_numeros

    def verificar_resposta(self, resposta):
        # Verifica se a resposta está correta
        resposta_correta = self.sequencia_numeros
        return resposta == resposta_correta

    def iniciar_atividade(self):
        nivel_dificuldade = 3  # Começa com um nível de dificuldade moderado
        comprimento_sequencia = 3  # Comprimento inicial da sequência

        while True:
            # Gera e exibe a sequência
            sequencia = self.gerar_sequencia(comprimento_sequencia)
            maquina.say(f"Memorize a sequência: {sequencia}")
            maquina.runAndWait()

            # Solicita a resposta da criança
            resposta_usuario = ouvir_resposta()

            # Verifica a resposta
            try:
                correta = self.verificar_resposta([int(digito) for digito in resposta_usuario])
            except ValueError:
                maquina.say("Ops, parece que houve um erro. Vamos tentar novamente.")
                continue

            # Atualiza a pontuação e nível de dificuldade
            if correta:
                maquina.say("Parabéns, você acertou!")
                self.pontuacao += 1
                comprimento_sequencia += 1  # Aumenta a dificuldade
            else:
                maquina.say("Ops, parece que houve um erro. Vamos tentar novamente.")
                self.pontuacao = max(0, self.pontuacao - 1)  # Reduz a pontuação em caso de erro

            # Pergunta se a criança quer continuar
            continuar = input("Quer continuar? (Sim/Não): ").lower()
            if continuar != "sim":
                maquina.say(f"Sua pontuação final: {self.pontuacao}")
                break

def inserir_nome():
    global nome_usuario
    nome_usuario = input("Por favor, insira seu nome: ")
    saudacao = determinar_saudacao()
    maquina.say(f"{saudacao}, {nome_usuario}! Bem-vindo à Minerva.")
    maquina.runAndWait()

def determinar_saudacao():
    hora_atual = datetime.datetime.now().hour
    if 6 <= hora_atual < 12:
        return "Bom dia"
    elif 12 <= hora_atual < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

def apresentacao_minerva():
    maquina.say("Olá, sou a Minerva, sua assistente virtual. Como posso ajudar você hoje?")
    maquina.runAndWait()

def jogo_educativo():
    maquina.say("Vamos jogar um jogo educativo!")
    maquina.runAndWait()

    perguntas_respostas = {
        "Quanto é 2 + 2?": "4",
        "Qual é a capital do Brasil?": "Brasília",
        "Quantos planetas existem no sistema solar?": "8",
        "Qual é a fórmula química da água?": "H2O",
        "Quem escreveu 'Dom Quixote'?": "Miguel de Cervantes",
        "Quanto é 5 + 5?": "10",
        "Quanto é 8 - 3?": "5",
        "Quanto é 3 x 4?": "12",
        "Quanto é 18 ÷ 3?": "6",
        "Quem pintou a Mona Lisa?": "Leonardo da Vinci",
        "Quanto é 7 + 9?": "16",
        "Quanto é 15 - 7?": "8",
        "Quanto é 6 x 8?": "48",
        "Quanto é 20 ÷ 4?": "5",
        "Qual é o maior animal terrestre?": "Elefante",
        "Quem descobriu a gravidade?": "Isaac Newton",
        "Quanto é 9 + 6?": "15",
        "Quanto é 12 - 9?": "3",
        "Quanto é 5 x 7?": "35",
        "Quanto é 36 ÷ 6?": "6",
        "Qual é a maior montanha do mundo?": "Monte Everest",
        "Quanto é 8 + 7?": "15",
        "Quanto é 20 - 14?": "6",
        "Quanto é 9 x 4?": "36",
        "Quanto é 45 ÷ 9?": "5",
        "Qual é o maior felino brasileiro?": "Onça-pintada",
        "Quantos ossos tem um esqueleto humano adulto?": "206",
    }

    # Convertendo as chaves do dicionário em uma lista
    perguntas_sorteadas = random.sample(list(perguntas_respostas.keys()), 5)
    pontuacao = 0

    for pergunta in perguntas_sorteadas:
        resposta_correta = perguntas_respostas[pergunta]

        maquina.say(pergunta)
        maquina.runAndWait()

        resposta_usuario = ouvir_resposta()

        if resposta_usuario.lower() == resposta_correta.lower():
            maquina.say("Parabéns, você acertou!")
            pontuacao += 1
        else:
            maquina.say(f"Ops, a resposta correta era {resposta_correta}.")

    if pontuacao == 5:
        maquina.say("Parabéns, você acertou todas as perguntas! Se quiser jogar novamente, é só pedir.")
    else:
        maquina.say("Não tem problema se você não conseguiu. Podemos tentar de novo! Eu irei te ajudar, ok?")

def assistencia_organizacao():
    maquina.say(f"{nome_usuario}, vou ajudá-lo a organizar suas tarefas. O que você gostaria de fazer hoje?")
    maquina.runAndWait()

    tarefas = []

    while True:
        maquina.say("Diga-me uma tarefa ou diga 'finalizar' para encerrar.")
        maquina.runAndWait()

        tarefa = ouvir_resposta()

        if tarefa.lower() == "finalizar":
            break
        else:
            tarefas.append(tarefa)

    if tarefas:
        maquina.say("Aqui estão suas tarefas para hoje:")
        for idx, tarefa in enumerate(tarefas, start=1):
            maquina.say(f"{idx}. {tarefa}")
        maquina.runAndWait()
    else:
        maquina.say("Sem tarefas para hoje. Bom descanso!")

def ouvir_resposta():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = audio.listen(source)
            resposta = audio.recognize_google(voz, language="pt-BR")
            print(f"Você disse: {resposta}")
            return resposta
    except sr.RequestError as e:
        print(f"Não foi possível obter resultados de reconhecimento de fala; {e}")
    except sr.UnknownValueError:
        print("Não foi possível entender a fala.")
    except Exception as ex:
        print(f"Ocorreu um erro durante o reconhecimento de fala: {ex}")
    return ""

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

def comando_voz_usuario():
    global nome_usuario
    global apresentacao_feita

    if not nome_usuario:
        inserir_nome()

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
            break
        elif "me fale sobre você" in comando:
            apresentacao_minerva()
        elif "jogo" in comando:
            jogo_educativo()
        elif "assistência" in comando:
            assistencia_organizacao()
        elif "estimulação cognitiva" in comando:
            atividade_cognitiva = EstimulacaoCognitiva()
            atividade_cognitiva.iniciar_atividade()
        else:
            maquina.say("Desculpe, não entendi o comando.")
            maquina.runAndWait()

comando_voz_usuario()


