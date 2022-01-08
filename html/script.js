// let file_path = document.getElementById('file-path')
// let file_name = document.getElementById('file-name')
// let word = document.getElementById('keyword')
order_button.addEventListener('click', () => {
    if (item_code.value != "" && item_pieces.value != "") {
        eel.item_order(item_code.value, int(item_pieces.value));
        item_code.value = '';
        item_pieces.value = '';
    }else{
        alert("商品コードと商品個数の両方を入力してください");
    }
})


eel.expose(view_log_js)
function view_log_js(text){
    document.getElementById('order-list').value += text + "\n";
}
