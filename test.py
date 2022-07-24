import requests
import Token




class Spotify:

    def test_create_play_list(self):
        header = {'Authorization': Token.token}
        body = "{\"name\":\"New Playlist\",\"description\":\"New playlist description\",\"public\":false}"
        response = requests.post('https://api.spotify.com/v1/users/31lm4gtjolfmbhh22ygqt3ezn3fa/playlists',headers=header, data=body)
        #assert response.status_code == 200
        print(response.text)
        print(response.status_code)

s = Spotify()
s.test_create_play_list()