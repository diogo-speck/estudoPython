import yt_dlp

escolha = input("Deseja baixar o vídeo ou só o áudio (v/a)? ")
if (escolha == 'a' or escolha == 'A'):
    url = input("URL do vídeo para baixar SOMENTE ÁUDIO: ")

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': r'C:\Users\diogo\OneDrive\Music\%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
else:   
    url = input("URL do vídeo: ")

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': r'C:\Users\diogo\OneDrive\Videos\%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])