import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

audio = sr.Recognizer()
maquina = pyttsx3.init()

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

comando_voz_usuario()


