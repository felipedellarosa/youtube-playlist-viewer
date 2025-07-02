import streamlit as st
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Inicializa o serviço do YouTube
youtube = build("youtube", "v3", developerKey=API_KEY)

def extrair_id_playlist(link):
    query = urlparse(link).query
    params = parse_qs(query)
    return params.get("list", [None])[0]

st.title("📺 Visualizações de Playlist do YouTube")

link = st.text_input("Cole o link da playlist do YouTube:")

if link:
    playlist_id = extrair_id_playlist(link)
    if playlist_id:
        with st.spinner("Buscando vídeos..."):
            request = youtube.playlistItems().list(
                part="contentDetails",
                maxResults=25,
                playlistId=playlist_id
            )
            response = request.execute()
            ids = [item["contentDetails"]["videoId"] for item in response["items"]]

            request = youtube.videos().list(
                part="snippet,statistics",
                id=",".join(ids)
            )
            response = request.execute()

            data = []
            for video in response["items"]:
                data.append({
                    "Título": video["snippet"]["title"],
                    "Visualizações": video["statistics"]["viewCount"]
                })

            st.success("Pronto!")
            st.table(data)
    else:
        st.error("Link inválido. Certifique-se de colar um link de playlist do YouTube.")
