#/////////////////////////////////////////////////////////////////////
#テスト要件
#｜＿htmlを生成する以下のソースのリンク先を自分の好きなサイトに変更する
#｜＿背景色を変更する
#｜＿リンク先にマウスカーソルが重なった時、色を変更する(hover)
#/////////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////////////////////////////
class MakeHtml():#スーパークラス：HTML基本タグを生成
    #---------------------------------------
    def html(self,arg):
        return "<html>\n" + str(arg) + "\n</html>"
    #---------------------------------------
    def head(self, arg):        
        style = "<style>\na:hover { color: red; }\n</style>\n"
        return "<head><title>" + str(arg) + "</title>\n" + style + "</head>\n"
    #---------------------------------------
    def body(self, arg):        
        return "<body bgcolor='lightblue'>\n" + str(arg) + "\n</body>"
    #---------------------------------------
    def p(self, arg):
        return "<p>" + str(arg) + "</p>\n"
    #---------------------------------------
    def a(self, arg):        
        return "<a href='https://www.openai.com'>" + str(arg) + "</a>"
#/////////////////////////////////////////////////////////////////////
class MakeContent(MakeHtml):  # サブクラス：コンテンツを生成
    def content(self, txt):
        return txt
#/////////////////////////////////////////////////////////////////////
class MakeFile():  # HTMLファイルの出力
    def out_txt(self, IDX, txt):
        with open(IDX, mode="w", encoding="utf-8") as f:
            f.write(txt)
#/////////////////////////////////////////////////////////////////////
content = MakeContent()  # インスタンス生成：HTMLコード

txt = ""
txt = content.a("リンク先: OpenAI")
txt = content.p(txt)
txt = content.body(txt)
txt = content.head("タイトル") + txt
txt = content.html(txt)
#print(txt)  # use_debug

IDX = "index_class.html"
file = MakeFile()  # インスタンス生成：出力ファイル
file.out_txt(IDX, txt)