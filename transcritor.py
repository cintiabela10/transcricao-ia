#código que cria um arquvio txt com a transcrição do áudio e o timestamp de cada frase dita
import whisper

#função para transcrever o arquivo de áudio
def transcrever_arquivo_com_timestamp(modelo, nome_audio, idioma_audio):
    print(f"Iniciando transcrição(Isso pode demorar alguns minutos)...")
    transcricao = modelo.transcribe(nome_audio, language=idioma_audio)

    print("\n--- Texto transcrito com tempo ---")

    nome_arquivo_txt = nome_audio.replace(".mp3", ".txt")
    #cria um arquivo txt e transcreve nele, todo o conteúdo do áudio, junto com os timestamps de cada frase
    with open(nome_arquivo_txt, "w", encoding="utf-8") as arquivo:
        for segmento in transcricao["segments"]:
            frase = (f"[{segmento['start']:.2f}s → {segmento['end']:.2f}s]  {segmento['text']}") #type: ignore
            
            print(frase)
            arquivo.write(f"{frase} \n")
            
    print(f"Arquivo \"{nome_arquivo_txt}\" criado com sucesso.")
 
modelo = ""
nome_audio = ""
continuar = True #Só para o programa não continuar caso o usuário mande encerrar na escolha de modelo.
while True:
    #Testa se o modelo escolhido é válido:
    try:
        print("Modelos disponíveis: ")
        for modelo in whisper.available_models():
            print(modelo)
        modelo_ia = input("Digite o nome do modelo que deseja usar: ")
        print(f"Carregando modelo {modelo_ia}...")
        modelo = whisper.load_model(modelo_ia)
        print("Modelo carregado com sucesso!")
        break
    except RuntimeError:
        tentar_novamente = input("Modelo Inválido! Deseja tentar novamente? s/n: ").lower()
        if tentar_novamente == "s":
            continue
        elif tentar_novamente == "n":
            print("Encerrando...")
            continuar = False
            break

while continuar == True:
    #Verifica se o local/nome do arquivo é válido, incluindo o .mp3 no final.
    try:
        nome_audio = input("Digite o nome do arquivo.mp3 (Caso o arquivo esteja em outra pasta: local/do/arquivo.mp3): ")
        with open(nome_audio, "rb") as audio:
            pass
        break
    except FileNotFoundError:
        tentar_novamente = input("Arquivo Inválido! Deseja tentar novamente? s/n: ").lower()
        if tentar_novamente == "s":
            continue
        elif tentar_novamente == "n":
            print("Encerrando...")
            continuar = False

if continuar == True:
    transcrever_arquivo_com_timestamp(modelo, nome_audio, "pt")
