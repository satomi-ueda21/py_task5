import eel
import desktop
import pos-system

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
#python側の関数名を書いた後、javascript側の関数名を書く。
def kimetsu_search(word, file_path, file_name):
    search.kimetsu_search(word, file_path, file_name)
    return True

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)