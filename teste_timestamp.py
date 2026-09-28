#código que cria um arquvio txt com a transcrição do áudio e o timestamp de cada frase dita
import whisper

#função para transcrever o arquivo de áudio
def transcrever_arquivo_com_timestamp(modelo_ia, nome_audio, idioma_audio):
    print(f"Carregando modelo {modelo_ia}...")
    modelo = whisper.load_model(modelo_ia)

    print(f"Iniciando transcrição(Isso pode demorar alguns minutos)...")
    transcricao = modelo.transcribe(nome_audio, language=idioma_audio)

    print("\n--- Texto transcrito com tempo ---")

    nome_arquivo_txt = nome_audio.replace(".mp3", ".txt")

    #cria um arquivo txt e transcreve nele, todo o conteúdo do áudio, junto com os timestamps de cada frase
    with open(nome_arquivo_txt, "w", encoding="utf-8") as arquivo:
        for segmento in transcricao["segments"]:
            frase = (f"[{segmento['start']:.2f}s → {segmento['end']:.2f}s]  {segmento['text']}")
            
            print(frase)
            arquivo.write(f"{frase} \n")
            
    print(f"Arquivo \"{nome_arquivo_txt}\" criado com sucesso.")
            

transcrever_arquivo_com_timestamp("medium", "audio.mp3", "pt")