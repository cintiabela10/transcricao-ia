# Transcrição de Palestras com Whisper AI (Offline)

Este projeto realiza a transcrição offline de áudios e vídeos de palestras utilizando a biblioteca open-source **Whisper**, desenvolvida pela OpenAI.

> **Nota:** Por boas práticas de versionamento e para respeitar licenças de distribuição de mídia, os arquivos de áudio não são armazenados neste repositório. O script baixa e processa o áudio localmente durante a execução.

---

## 🚀 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado em sua máquina:

1. **Python 3.8+**
2. **FFmpeg** (necessário para processamento de áudio):
   * **Windows (PowerShell):** `winget install ffmpeg` ou `choco install ffmpeg`
   * **Linux (Ubuntu/Debian):** `sudo apt install ffmpeg`
   * **macOS:** `brew install ffmpeg`

---

## 📦 Instalação

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
   cd NOME_DO_REPOSITORIO

2. Instale as dependências de Python:
    ```bash
    pip install git+[https://github.com/openai/whisper.git](https://github.com/openai/whisper.git)
    pip install yt-dlp

3. Obtenção do Áudio para Teste:
Para rodar os testes com o vídeo da palestra ("Como a IA vai mudar tudo - Miguel Fernandes / TEDxSaoPaulo"), baixe a faixa de áudio localmente executando o comando abaixo no terminal:
    ```bash
    yt-dlp -x --audio-format mp3 "[https://www.youtube.com/watch?v=C38xlWnkezQ](https://www.youtube.com/watch?v=C38xlWnkezQ)" -o "audio_palestra.mp3"
    
4. Executando a Transcrição:
Com o arquivo audio_palestra.mp3 baixado na pasta do projeto, execute o script Python:
    ```bash
    python teste.py
O script carregará o modelo do Whisper selecionado (ex: medium) e gerará o arquivo de texto transcricao.txt com o resultado final.

---

# Créditos e Licença da Mídia
Palestra original: "[Como a IA vai mudar tudo (inclusive você)](https://www.youtube.com/watch?v=C38xlWnkezQ)"

Palestrante: Miguel Fernandes

Fonte: TEDxSaoPaulo no YouTube

Licença do vídeo: CC BY-NC-ND 4.0 (Uso pessoal/educacional para testes de transcrição).