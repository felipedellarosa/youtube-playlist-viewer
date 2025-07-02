# 🎬 YouTube Playlist View Tracker

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-%3E%3D1.20.0-orange)](https://streamlit.io/)
[![API](https://img.shields.io/badge/YouTube_API-v3-red)](https://developers.google.com/youtube/v3)

---

## 🚀 Visão Geral

Este projeto é uma aplicação web simples feita em **Python** usando **Streamlit**, que permite consultar o número de visualizações dos vídeos dentro de uma playlist do YouTube.

Basta colar o **link completo da playlist**, e o app irá extrair o ID automaticamente, buscar os vídeos usando a API do YouTube Data v3 e exibir uma tabela com o título e o número de views de cada vídeo.

---

## 🎯 Funcionalidades

- Interface simples e intuitiva via navegador
- Entrada do link completo da playlist (não precisa pegar o ID manualmente)
- Busca até 25 vídeos por vez da playlist
- Exibição dos títulos e visualizações em tabela
- Uso de **API Key pública** para evitar autenticação OAuth complexa
- Fácil configuração e deploy

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia               | Versão         | Link                             |
|-------------------------|----------------|---------------------------------|
| Python                  | 3.7+           | [python.org](https://python.org)|
| Streamlit               | >=1.20.0       | [streamlit.io](https://streamlit.io) |
| Google API Python Client| >=2.70.0       | [googleapis.github.io](https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html) |

---

## 🎬 Como Usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
pip install -r requirements.txt
streamlit run app.py


