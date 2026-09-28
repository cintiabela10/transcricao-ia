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
   git clone https://github.com/cintiabela10/transcricao-ia.git
   cd transcricao-ia
   ```

2. Instale as dependências de Python para o script utilizando Whisper:

   ```bash
   pip install git+https://github.com/openai/whisper.git
   pip install yt-dlp
   ```

3. Dependências adicionais para o script com timestamps (`whisper_timestamped`):

   O script que gera transcrições com timestamps detalhados (`teste_whisper_timestamped.py`) utiliza a biblioteca `whisper-timestamped`, que requer dependências adicionais.
   Instale-as com:

   ```bash
   pip install whisper-timestamped
   pip install onnxruntime torchaudio
   ```

   > **Observação:** As bibliotecas `onnxruntime` e `torchaudio` são necessárias para o recurso de detecção de atividade de voz (VAD) do `whisper-timestamped`.

4. Obtenção do Áudio para Teste:

   Para rodar os testes com o vídeo da palestra ("Como a IA vai mudar tudo - Miguel Fernandes / TEDxSaoPaulo"), baixe a faixa de áudio localmente executando o comando abaixo no terminal:

   ```bash
   yt-dlp -x --audio-format mp3 "https://www.youtube.com/watch?v=C38xlWnkezQ" -o "audio.mp3"
   ```

5. Executando a Transcrição com Whisper:

   Com o arquivo `audio.mp3` baixado na pasta do projeto, execute:

   ```bash
   python teste.py
   ```

   O script carregará o modelo do Whisper selecionado (ex: `medium`) e gerará o arquivo de texto com o resultado final.

6. Executando a Transcrição com Timestamps:

   Para gerar uma transcrição contendo os horários de início e fim de cada segmento de fala, execute:

   ```bash
   python teste_timestamp.py
   ```

   O script criará um arquivo `.txt` com a transcrição
   
7. Executando a Transcrição com a biblioteca Whisper_Timestamped:

   Para gerar uma transcrição contendo os horários de início e fim de cada palavra, execute:

   ```bash
   python teste_whisper_timestamped.py
   ```

   O script criará um arquivo `.json` com a transcrição
    
---

# Créditos e Licença da Mídia
Palestra original: "[Como a IA vai mudar tudo (inclusive você)](https://www.youtube.com/watch?v=C38xlWnkezQ)"

Palestrante: Miguel Fernandes

Fonte: TEDxSaoPaulo no YouTube

Licença do vídeo: CC BY-NC-ND 4.0 (Uso pessoal/educacional para testes de transcrição).
