# Usando API do Gemini

from dotenv import load_dotenv
from google import * # Todo arrumar
import os
import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import pyttsx3
import time
import subprocess # pode abrir praticamente qualquer programa, até local
import webbrowser # links

# =========================
# Configurações
# =========================

FS = 44100
DURACAO = 5

# =========================
# Inicialização
# =========================

load_dotenv()

client = genai.Client( # Todo arrumar
    api_key=os.getenv("GEMINI_API_KEY")
)

print("Chave encontrada:", bool(os.getenv("GEMINI_API_KEY")))

# Carrega o Whisper UMA VEZ
print("Carregando Whisper...")
model = whisper.load_model("base")

# Inicializa voz
voz = pyttsx3.init()

# Cria chat com memória
chat_gemini = client.chats.create(
    model="gemini-2.5-flash"
)

# =========================
# Funções
# =========================

def falar(texto):
    """Fala o texto em voz alta."""
    voz.say(texto)
    voz.runAndWait()


def executar_comando(prompt):

    prompt = prompt.lower()

    if "youtube" in prompt:
        webbrowser.open("https://youtube.com")
        falar("Abrindo YouTube.")
        return True

    if "google" in prompt:
        webbrowser.open("https://google.com")
        falar("Abrindo Google.")
        return True

    if "bloco de notas" in prompt:
        subprocess.Popen(["notepad"])
        falar("Abrindo bloco de notas.")
        return True

    if "calculadora" in prompt:
        subprocess.Popen(["calc"])
        falar("Abrindo calculadora.")
        return True

    return False


def perguntar_gemini(prompt):
    """Envia mensagem para o Gemini com retry."""

    for tentativa in range(5):
        try:
            response = chat_gemini.send_message(prompt)
            return response.text

        except Exception as e:
            print(f"Tentativa {tentativa + 1} falhou:")
            print(e)

            if tentativa < 4:
                print("Tentando novamente em 5 segundos...")
                time.sleep(5)

    return "Não consegui obter uma resposta após várias tentativas."


# =========================
# Modo voz
# =========================

modo_voz = input("Deseja usar comando de voz (s/n): ").lower()

if modo_voz == "s":

    while True:

        print("\nFale... (diga 'encerrar' para sair)")

        audio = sd.rec(
            int(DURACAO * FS),
            samplerate=FS,
            channels=1
        )

        sd.wait()

        write("audio.wav", FS, audio)

        resultado = model.transcribe(
            audio.flatten(),
            language="pt"
        )

        prompt = resultado["text"].strip()

        print(f"\nVocê: {prompt}")

        if not prompt:
            continue

        if "encerrar" in prompt.lower():
            falar("Encerrando.")
            break

        # Executa comandos locais
        if executar_comando(prompt):
            continue

        resposta = perguntar_gemini(prompt)

        print(f"\nDiogAI: {resposta}")
        falar(resposta)

# =========================
# Modo texto
# =========================

else:

    while True:

        prompt = input("\nVocê: ")

        if prompt.lower() == "encerrar":
            break

        if executar_comando(prompt):
            continue

        resposta = perguntar_gemini(prompt)

        print(f"\nDiogAI: {resposta}")