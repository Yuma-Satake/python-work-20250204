#/////////////////////////////////////////////////////////////////////
#テスト要件
#｜＿htmlを生成する以下のソースのリンク先を自分の好きなサイトに変更する
#/////////////////////////////////////////////////////////////////////

#----------------------------------------------------------------------strat
#HTML基本タグを生成するデコレータ関数
#---------------------------------------
def html(func):
    def wrapper(*args,**kargs):
        return "<html>\n"+str(func(*args,**kargs))+"\n</html>"
    return wrapper
#---------------------------------------
def head(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return "<head><title>"+arg+"</title></head>\n"+str(func(*args, **kwargs))
        return wrapper
    return decorator
#---------------------------------------
def body(func):
    def wrapper(*args,**kargs):
        return "<body bgcolor='lavender'>\n"+str(func(*args,**kargs))+"</body>"
    return wrapper
#---------------------------------------
def p(func):
    def wrapper(*args,**kargs):
        return "<p>"+str(func(*args,**kargs))+"</p>\n"
    return wrapper
#---------------------------------------
def a(func):
    def wrapper(*args,**kargs):
        return "<a href='#'>"+str(func(*args,**kargs))+"</a>"
    return wrapper
#----------------------------------------------------------------------end

#---------------------------------------
#HTMLファイルとしてカレントに書き出し関数
#---------------------------------------
def out_file(IDX,arg):
    with open(IDX,mode="w",encoding="utf-8") as f:
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
#print(content("リンク先"))#use_test
IDX="index_def.html"
txt=content("リンク先:test_def")  #HTMLの生成
#print(txt)#use_debug
out_file(IDX,txt)                #出力
#////////////////////////////////////////////////