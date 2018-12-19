from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs
import time

app=Flask(__name__)

@app.route('/index')
def index():
    print("hi")
    print("how are you?")
    return """
    <h1>oh~ I'm different.</h1>
    <ima src = "https://scontent-ort2-2.cdninstagram.com/vp/16405cd4248f738b40c08667d0101c14/5C7ECD5B/t51.2885-15/e35/c181.0.717.717/s480x480/33238868_261524791257174_2585023614394826752_n.jpg">
    """
    
@app.route('/naver_toon')
def naver_toon():
    
    today=time.strftime('%a').lower()
    
    url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week' + today
    
    response = requests.get(url).text
    soup = bs(response, 'html.parser')
    
    toons=[]
    
    li=soup.select('.img_list li')
    url_base = 'https//comic.naver.com'
    for item in li:
        toon = {
            'title':item.select('dt a')[0].text,
            'url':url_base + item.select('dt a')[0]['href'],
            'img':item.select('.thumb img')[0]['src']
        }
        toons.append(toon)
    
    print(toons)
    
    return render_template('naver_toon.html', t = toons)
    

    