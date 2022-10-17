#Code by Nguyen Tuan Anh
import requests
class Instagram():
    def __init__(self,cookies,id_post,text) -> None:
        self.cookies = cookies
        self.id_post = id_post
        self.text = text
        self.csrftoken=cookies.split('csrftoken=')[1].split(';')[0]
        self.headers = {
            'authority': 'www.instagram.com',
            'cookie': self.cookies,
            'origin': 'https://www.instagram.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'x-csrftoken': self.csrftoken,
            'x-instagram-ajax': '1005991556',
        }
        self.data ={
            'comment_text': self.text,
            'replied_to_comment_id': '',
        }
    def Api_folow(self,id_post):
        response = requests.post(f'https://www.instagram.com/web/friendships/{id_post}/follow/', headers=self.headers).text
        if 'ok' in response:
            return True
        else:
            return False
    def Api_like(self,id_post):
        response = requests.post(f'https://www.instagram.com/web/likes/{id_post}/like/',headers=self.headers).text
        if 'ok' in response:
            return True
        else:
            return False
        
    def Api_cmt(self,id_post):
        response = requests.post(f'https://www.instagram.com/web/comments/{id_post}/add/',headers=self.headers, data=self.data).text
        if 'ok' in response:
            return True
        else:
            return False
    def Api_like_cmt(self,id_post):
        response = requests.post(f'https://www.instagram.com/web/comments/like/{id_post}/',headers=self.headers).text
        if 'ok' in response:
            return True
        else:
            return False
cookies = ''
id_post = ''
text = ''
IG = Instagram(cookies,id_post,text)
#folow = IG.Api_folow(id_post)
#like = IG.Api_like(id_post)
#cmt = IG.Api_cmt(id_post)
#like_cmt = IG.Api_like_cmt(id_post)
