import moviepy.editor as mp
import sys

def converter_avi_para_mp3(caminho_avi, caminho_mp3):
    """
    Converte um arquivo de vídeo AVI para áudio MP3.
    
    Parâmetros:
    - caminho_avi: caminho completo do arquivo .avi de entrada.
    - caminho_mp3: caminho completo para o arquivo .mp3 de saída.
    """
    try:
        # Carrega o vídeo
        video = mp.VideoFileClip(caminho_avi)
        
        # Extrai a faixa de áudio
        audio = video.audio
        
        # Salva a faixa de áudio como MP3
        audio.write_audiofile(caminho_mp3)
        
        print(f"Conversão concluída: {caminho_mp3}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        # Libera os recursos, se disponíveis
        if 'video' in locals():
            video.close()
        if 'audio' in locals():
            audio.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python converter.py caminho_entrada.avi caminho_saida.mp3")
        sys.exit(1)
    
    arquivo_avi = sys.argv[1]
    arquivo_mp3 = sys.argv[2]
    
    converter_avi_para_mp3(arquivo_avi, arquivo_mp3)
