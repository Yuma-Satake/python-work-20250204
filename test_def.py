#/////////////////////////////////////////////////////////////////////
#テスト要件
#｜＿htmlを生成する以下のソースのリンク先を自分の好きなサイトに変更する
#/////////////////////////////////////////////////////////////////////

#----------------------------------------------------------------------start
#HTML基本タグを生成するデコレータ関数
#---------------------------------------
def html(func):
    def wrapper(*args, **kwargs):
        return "<html>\n" + str(func(*args, **kwargs)) + "\n</html>"
    return wrapper
#---------------------------------------
def head(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return "<head><title>" + arg + "</title></head>\n" + str(func(*args, **kwargs))
        return wrapper
    return decorator
#---------------------------------------
def body(func):
    def wrapper(*args, **kwargs):
        return "<body bgcolor='lavender'>\n" + str(func(*args, **kwargs)) + "</body>"
    return wrapper
#---------------------------------------
def p(func):
    def wrapper(*args, **kwargs):
        return "<p>" + str(func(*args, **kwargs)) + "</p>\n"
    return wrapper
#---------------------------------------
def a(func):
    def wrapper(*args, **kwargs):
        # リンク先を自分の好きなサイト（例: GitHub）に変更
        return "<a href='https://www.github.com'>" + str(func(*args, **kwargs)) + "</a>"
    return wrapper
#----------------------------------------------------------------------end

#---------------------------------------
#HTMLファイルとしてカレントに書き出し関数
#---------------------------------------
def out_file(IDX, arg):
    with open(IDX, mode="w", encoding="utf-8") as f:
        f.write(arg)

#---------------------------------------
#デコレートを保持する関数
#---------------------------------------
@html
@head("タイトル")
@body
@p
@a
def content(txt):
    return txt
#----------------------------------------------------------------------end

#////////////////////////////////////////////////
#実行
#////////////////////////////////////////////////
IDX = "index_def.html"
txt = content("GitHub")  #HTMLの生成
out_file(IDX, txt)       #出力
#////////////////////////////////////////////////