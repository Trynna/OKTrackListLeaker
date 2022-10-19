import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {"User-Agent": UserAgent().chrome}


def check_feat(artists, main_artist):
    artists = artists.replace(main_artist, main_artist + ", ")
    if artists[-2:] == ", ":
        artists = artists[:-2]
    return artists


def leak(people_mode):
    ok = "https://ok.ru/music/track/"
    print("OK Tracklist Leaker by Trynna")
    track = int(input("Введите айди первого трека: "))
    num = int(input("Введите предполагаемое количество треков: "))
    gap = 4097

    for x in range(0, num):
        link = ok + str(track)
        req = requests.get(link, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        title = soup.find(class_='ucard-v_h ellip bold __name').text
        artists = soup.find(class_="ucard-v_h ellip __stats").text
        main_artist = soup.find(class_="ucard-v_stats-item-text").text
        artists = check_feat(artists, main_artist)
        if people_mode == False:
            print(f'{x+1}. {artists} — {title} | {link}')
        else:
            print(f'{x+1}. {artists} — {title}')
        track = track + gap


leak(True)
