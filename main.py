from animeflv import AnimeFLV
'''
Base Functionality of the future MAnagement System
'''

with AnimeFLV() as api:
    anime_id = input("Anime-ID:")
    anime_info = api.get_anime_info(anime_id)

    for episode in anime_info.episodes[::-1]:
        episode_id = episode.id
        download_links = api.get_links(anime_id, episode_id)
        print(episode.id)
        for link in download_links:
            print(link.url)
