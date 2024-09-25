from animeflv import AnimeFLV

# Crear una instancia de la API
with AnimeFLV() as api:
    # Obtener información del anime por ID
    anime_id = input("Anime-ID:")
    anime_info = api.get_anime_info(anime_id)

    for episode in anime_info.episodes[::-1]:
        episode_id = episode.id
        download_links = api.get_links(anime_id, episode_id)
        print(episode.id)
        for link in download_links:
            print(link.url)

