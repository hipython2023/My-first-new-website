from flask import *
from getmusic import *
from getimg import *
from getmovie import *
app = Flask(__name__)

#"/"路由
#{
@app.route('/')
def index():
    try:
        with open("dress.pickle","r",encoding="UTF-8") as file:
            pic = file.read()
    except:
        pic = "/static/images/g25.gif"
    try:
        with open("music.pickle","r",encoding="UTF-8") as file:
            music = file.read()
    except:
        music = "http://music.163.com/song/media/outer/url?id=1901371647.mp3"
    return render_template("index.html",x = pic,music=music)
#}

#"/search"路由：显示search页面
#{
@app.route("/search")
def search():
    return render_template("search.html")
#}

@app.route("/search_form")
def search_form():
    a = request.values.get("word")
    search = request.values.get("A组")
    if search=="video":
        url="https://search.bilibili.com/all?keyword="+a
    elif search=="shop":
        url="https://search.jd.com/Search?keyword="+a
    elif search=="music":
        url="https://music.163.com/#/search/m/?s="+a
    elif search=="image":
        url="https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCw2LDIsMyw1LDEsNCw3LDgsOQ%3D%3D&word="+a
    elif search=="txt":
        url="https://wenku.baidu.com/search?ie=utf-8&word="+a
    elif search=="word":
        url="https://baike.baidu.com/item/"+a
    elif search=="article":
        url="/article"
    elif search=="joke":
        url="/joke"
    return redirect(url)

#"/music"路由
#{
@app.route("/music")
def music():
    music = get_music()
    return render_template("music.html",music_list=music)
#}

#"/movie"路由
#{
@app.route("/movie")
def movie():
    movie = get_movie()
    return render_template("movie.html",movie_list=movie)
#}

#"/photo"路由
#{
@app.route("/photo")
def photo():
    img = get_img()
    return render_template("photo.html",img_list=img)
#}

#"/me"路由
#{
@app.route("/me")
def me():
    return render_template("me.html")
#}

#"/dress"路由
#{
@app.route("/dress")
def dress():
    return render_template("dress.html")
#}

#"/set_music"路由
#{
@app.route("/set_music")
def set_music():
    global music
    index_music = request.values.get("music")
    with open("music.pickle","w",encoding="UTF-8") as file:
        file.write(index_music)
    return redirect("/")
#}

#"/show_img"路由
#{
@app.route("/show_img")
def show_img():
    index_img = request.values.get("img")
    with open("dress.pickle","w",encoding="UTF-8") as file:
        file.write(index_img)
    return redirect("/")
#}

#"/recommend"路由
#{
@app.route("/recommend")
def recommend():
    return render_template("recommend.html")
#}

#"/article"路由
#{
@app.route("/article")
def article():
    return render_template("article.html")
#}

#"/joke"路由
#{
@app.route("/joke")
def joke():
    return render_template("joke.html")
#}

#"/wrong"路由
#{
@app.route("/wrong")
def wrong():
    return render_template("wrong.html")
#}

app.run()