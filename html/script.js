// ログイン前はオーダー部分非表示
document.getElementById("contents").style.display = "none";
//ログイン後オーダー部分表示
login_button.addEventListener('click', async () => {
    const number = await eel.pos_login(worker_code.value)();
    console.table(number)
    if (number){
        document.getElementById("contents").style.display = "block";
    } else {
        alert("従業員コードが違います")
    }
})

// オーダーボタンの動作
order_button.addEventListener('click', () => {
    if (item_code.value != "" && item_pieces.value != "") {
        eel.item_order(item_code.value, Number(item_pieces.value));
        item_code.value = '';
        item_pieces.value = '';
    }else{
        alert("商品コードと商品個数の両方を入力してください");
    }
})

// 完了ボタンの動作
end_button.addEventListener('click', () => {
    if (item_code.value == "" && item_pieces.value == "") {
        eel.order_end();
    } else {
        alert("オーダーボタンを押してください。");
    }
})

// 支払ボタンの動作
payment_button.addEventListener('click', () => {
    if (amount_pay.value != "" ) {
        eel.account_order(Number(amount_pay.value));
    } else {
        alert("支払金額を入力してください。");
    }
})

// リセットボタンの動作
reset_button.addEventListener('click', async () => {
    const res = await eel.order_reset()();
    if (res) {
        document.getElementById('order_list').value = "";
        document.getElementById('total_money').value = "";
        document.getElementById('amount_pay').value = "";
        document.getElementById('change_money').value = "";
    }
})

// それぞれの表示部分の関数
eel.expose(view_log_js)
function view_log_js(text){
    document.getElementById('order_list').value += text + "\n";
}
eel.expose(view_sum_js)
function view_sum_js(price) {
    document.getElementById('total_money').value = price;
}
eel.expose(change_money_js)
function change_money_js(price) {
    document.getElementById('change_money').value = price;
}
eel.expose(alert_js)
function alert_js(text) {
    alert(text)
}

