import eel
import desktop
import pos_system

app_name="html"
end_point="index.html"
size=(700,600)

#Orderインスタンス化
order = pos_system.Order

@ eel.expose
def item_order(item_code,item_pieces):
    res = order.add_item_order(item_code, item_pieces)
    print(res)



desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)