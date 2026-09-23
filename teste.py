import whisper
#função para transcrever os arquivos de audio com WhisperAI para facilitar testes.
def transcrever_arquivo(modelo, local_arquivo, idioma, nome_arquivo):
    print(f"Carregando modelo {modelo}...")
    model = whisper.load_model(modelo)

    print(f"Iniciando transcrição(Isso pode demorar alguns minutos)...")
    result = model.transcribe(local_arquivo, language=idioma)

    print("\n--- Texto Transcrito ---")
    print(result["text"])

    #Cria um arquivo txt com o texto transcrito
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(result["text"])

transcrever_arquivo("medium", "audio.mp3", "pt", "teste_medium.txt")