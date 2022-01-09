import eel
import desktop
import pos_system

app_name="html"
end_point="index.html"
size=(700,600)

#Orderインスタンス化
item_master = pos_system.item_master_csv()
order = pos_system.Order(item_master)

@ eel.expose
def item_order(item_code,item_pieces):
    order.add_item_order(item_code, item_pieces)
    order.view_item_oreder()

@ eel.expose
def order_end():
    order.receipt_output((f"合計{order.total_items:,}個。合計金額{order.total_money:,}円です"))
    eel.view_sum_js(f"支払金額:{order.total_money:,}円")

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)