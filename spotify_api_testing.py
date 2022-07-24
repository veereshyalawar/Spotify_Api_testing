import requests
import Token
import pytest

class Test_Spotify:

    def test_get_Current_user_profile(self):
        header ={'Authorization':Token.token}
        response = requests.get('https://api.spotify.com/v1/me',headers=header)
        print(response.status_code)
        assert response.status_code == 200
        #print(response.text)

    def test_get_users_profile(self):
        header = {'Authorization': Token.token}
        response = requests.get('https://api.spotify.com/v1/users/31lm4gtjolfmbhh22ygqt3ezn3fa', headers=header)
        assert response.status_code == 200

    def test_create_play_list(self):
        header = {'Authorization': Token.token}
        body = "{\"name\":\"veeresh\",\"description\":\"New playlist description\",\"public\":false}"
        response = requests.post('https://api.spotify.com/v1/users/31lm4gtjolfmbhh22ygqt3ezn3fa/playlists', headers=header, data=body)
        assert response.status_code == 200

    def test_get_playlist(self):
        header = {'Authorization': Token.token}
        response = requests.get('https://api.spotify.com/v1/playlists/0m9j1vbJTn3j0hD8mrSzOv', headers=header)
        assert response.status_code == 200

    def test_search_items(self):
        header = {'Authorization': Token.token}
        response = requests.get('https://api.spotify.com/v1/search?q=ram&type=track&limit=5&offset=5', headers=header)
        assert response.status_code == 200

    def test_add_items_to_playlist(self):
        header = {'Authorization': Token.token}
        response = requests.post('https://api.spotify.com/v1/playlists/58HryoUxAH5uWt7yRZXXLQ/tracks?uris=spotify%3Atrack%3A4ZNIkO2j6K2c0Nm8zWXmdn',headers=header)
        assert response.status_code == 200

