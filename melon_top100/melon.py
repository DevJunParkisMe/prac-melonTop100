# from melon_top100 import get_songs
# pip install requests, beautifulsoup4
# https://www.melon.com/chart/index.htm  // 멜론top100 url
# <tbody> => <tr>을 가지고 오면 데이터를 가져올 수 있음
# 100번 반복 후 리스트로 변경
# 결과 반환
# 화면 출력
import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": (
        "Chrome/72.0.3626.121 Safari/537.36"
    )
}
def get_songs():
    res = requests.get("https://www.melon.com/chart/index.htm", headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tbody_tr_tag = soup.select("tbody tr")
    
    song_list = []

    for rank, tr_tag in enumerate(tbody_tr_tag, 1):
        song_no = tr_tag["data-song-no"]
        song_title = tr_tag.select_one("a[href*=playSong]")
        album_title = tr_tag.select_one(".wrap_song_info a[href*=goAlbumDetail]")
        artist = tr_tag.select_one("a[href*=goArtistDetail]")

        song = {
            "rank" : rank,
            "song_no" : song_no,
            "song_title" : song_title.text,
            "album_title" : album_title.text,
            "artist" : artist.text
        }
        
        song_list.append(song)
    return song_list

if __name__ == "__main__":
    for song in get_songs():
        print(song)