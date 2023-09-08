from pathlib import Path

# To change

# Telegram
telegram_token = "telegram_token"
chat_id = "chat_id"

# Idealista
idealista_search_url = (
    "https://www.idealista.com/alquiler-viviendas/valencia-valencia/con-precio-hasta_1000"
    "/?ordenado-por=fecha-publicacion-desc"
)

# Not change
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
}
dir_root = Path(__file__).parent.parent
path_to_file = f"{dir_root}/assets/apartments.csv"
