// let item_code = document.getElementById('item_code')
// let item_pieces = document.getElementById('item_pieces')
// let word = document.getElementById('keyword')
order_button.addEventListener('click', () => {
    if (item_code.value != "" && item_pieces.value != "") {
        eel.item_order(item_code.value, Number(item_pieces.value));
        item_code.value = '';
        item_pieces.value = '';
    }else{
        alert("商品コードと商品個数の両方を入力してください");
    }
})

end_button.addEventListener('click', () => {
    if (item_code.value == "" && item_pieces.value == "") {
        eel.order_end();
    } else {
        alert("オーダーボタンを押してください。")
    }
})

eel.expose(view_log_js)
function view_log_js(text){
    document.getElementById('order_list').value += text + "\n";
}
eel.expose(view_sum_js)
function view_sum_js(price) {
    document.getElementById('total_money').value = price;
}
eel.expose(alert_js)
function alert_js(text) {
    alert(text)
}

