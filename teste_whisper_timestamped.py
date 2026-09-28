#código que cria um arquivo json com a transcrição do áudio, as frases ditas, e o timestamp de cada palavra
import whisper_timestamped as whisper
import json

#função para transcrever o arquivo de áudio
def transcrever_arquivo_com_timestamp(modelo_ia, nome_audio, idioma_audio):
    print(f"Carregando o áudio \"{nome_audio}\"")
    audio = whisper.load_audio(nome_audio)

    print(f"Carregando o modelo {modelo_ia}")
    modelo = whisper.load_model(modelo_ia, device="cpu")

    print("Iniciando transcrição(Isso pode demorar alguns minutos)...")
    transcricao_timestamped = whisper.transcribe(modelo, audio, idioma_audio)

    nome_arquivo_json = nome_audio.replace(".mp3", ".json")

    #cria um arquivo json e transcreve nele, o conteúdo do áudio (que já está com os timestamps de cada palavra)
    with open(nome_arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(transcricao_timestamped, arquivo, ensure_ascii=False, indent=2)

    print(f"Arquivo \"{nome_arquivo_json}\" criado com sucesso.")


transcrever_arquivo_com_timestamp("medium", "audio.mp3", "pt")