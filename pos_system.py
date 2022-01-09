import pandas as pd
import datetime
import eel

now = datetime.datetime.now()
CSV_PATH = "./item_master.csv"
RECEIPT_PATH = str("./receipt_{0:%m%d_%H%M}.txt").format(now)

#CSVからマスターデータの読み込み
def item_master_csv():
    item_master = []
    df = pd.read_csv(CSV_PATH, dtype={"item_code":object}, header=0)
    for item_code, item_name, price in zip(df["item_code"], df["item_name"], df["price"]):
        item_master.append(Item(item_code, item_name, price))
    return item_master

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price


    # def get_price(self):
    #     return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_order_count = []
        self.item_master=item_master
        self.total_money = 0
        self.total_items = 0

    #オーダー時の商品コードと個数をそれぞれリストに格納
    def add_item_order(self,item_code,item_pieces):
        self.item_order_list.append(item_code)
        self.item_order_count.append(item_pieces)

    #商品コードが一致する商品名と価格を返す
    def get_item_order(self,order_code):
        for code in self.item_master:
            if order_code == code.item_code:
                return code.item_name, code.price

    #オーダー受付
    def register_order(self):
        while True:
            item_code = input("オーダーする商品コードを入力してください。"
                              "オーダーを終了するときは0と入力してください>>>")
            if int(item_code) != 0:
                item_pieces = int(input("オーダーする商品の個数を入力してください>>>"))
                self.add_item_order(item_code, item_pieces)
            else:
                break

    # def view_item_list(self):
    #     for item in self.item_order_list:
    #         print("商品コード:{}".format(item))

    #オーダーされた商品内容と合計金額を表示
    def view_item_oreder(self):
        order_code = self.item_order_list[-1]
        item_piece = self.item_order_count[-1]
        res = self.get_item_order(order_code)
        if res != None:
            print(f"商品コード:{order_code} 商品名:{res[0]} 価格:{res[1]:,} 個数:{item_piece:,}")
            self.receipt_output(f"商品コード:{order_code} 商品名:{res[0]} 価格:{res[1]:,} 個数:{item_piece:,}")
            self.total_money = self.total_money + int(res[1] * item_piece)
            self.total_items = self.total_items + int(item_piece)
            eel.view_log_js(f"商品コード:{order_code} 商品名:{res[0]} 価格:{res[1]:,} 個数:{item_piece:,}")
            eel.view_sum_js(f"現在合計:{self.total_money:,}円")
        else:
            print(f"商品コード{order_code}は存在しません。")
            eel.alert_js(f"商品コード{order_code}は存在しません。")
        print(f"合計{self.total_items:,}個。合計金額{self.total_money:,}円です")
        # self.receipt_output(f"合計{self.total_items:,}個。合計金額{self.total_money:,}円です")


    #支払金額を受け付け後、お釣りを表示する
    def account_item_order(self):
        while True:
            self.amount_pay = int(input("支払金額を入力してください>>>"))
            self.change_money = self.amount_pay - self.total_money
            if self.change_money >= 0:
                print(f"{self.amount_pay:,}円いただきました。お釣りは{self.change_money:,}円です。")
                self.receipt_output(f"{self.amount_pay:,}円いただきました。お釣りは{self.change_money:,}円です。")
                break
            else:
                print("お金が足りません。もう一度支払金額を入力してください。")
                eel.alert_js("お金が足りません。もう一度支払金額を入力してください。")

    #テキストファイルに出力
    def receipt_output(self, text):
        with open(RECEIPT_PATH, mode='a', encoding="utf-8_sig") as f:
            f.write(text + '\n')


### メイン処理
def main():
    # マスタ登録
    item_master = item_master_csv()
    # item_master.append(Item("001","りんご",100))
    # item_master.append(Item("002","なし",120))
    # item_master.append(Item("003","みかん",150))

    # オーダー登録
    order=Order(item_master)
    order.register_order()
    # order.add_item_order()
    # order.add_item_order("002")
    # order.add_item_order("003")

    # オーダー表示
    # order.view_item_list()
    order.view_item_oreder()
    order.account_item_order()


if __name__ == "__main__":
    # order_code = input("オーダーする商品コードを入力してください>>>")
    main()