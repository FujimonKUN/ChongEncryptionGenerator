import jaconv  # jaconvを読み込み
import tkinter as tk  # tkinterをtkと名付け読み込み
import pyperclip  # pyperclipを読み込み
import sys  # sysを読み込み

root = tk.Tk()  # rootといウインドウを作成
root.title("チョング語暗号化システム")  # ウインドウタイトル
root.geometry("700x200")  # ウインドウサイズ
root.resizable(width=False, height=False)  # ウインドウサイズを固定


def btn_click():  # 命を捧げよボタンを押した時の関数
    kekka.delete(0, tk.END)  # kekkaの内容をクリーン
    fukugen.delete(0, tk.END)  # fukugenの内容をクリーン
    moji = txt.get()  # txtの内容を取得する事をmojiと定義

    result = moji.encode("utf-8")  # mojiをUTF-8にエンコードすることをresultと定義
    henkan = result.decode("cp932", errors="ignore")
    # resultからエンコードされた文字をcp932にデコードする事をhenkanと定義
    # この際、エラーが起きても無視する(errors="ignore")という引数をつける
    # ここでcp932でデコードされたutf-8が出てくる
    # わけがわからないよ

    fukugenhenkan = henkan.encode("cp932")
    # henkanから出てきた情報をcp932にエンコードすることをfukugenhenkanと定義
    # ここで文字とはお別れだ

    kekkafukugen = fukugenhenkan.decode("utf-8", errors="ignore")
    # fukugenhenkanから出てきた情報をutf-8にデコード、これをkekkafukugenと定義
    # これでcp932で変換された見える文字が出てくる

    kekka.insert(0, henkan)  # kekkaのテキストボックスに結果が出たhenkanを代入する
    fukugen.insert(0, kekkafukugen)  # fukugenというテキストボックスに結果が出たkekkafukugenを代入する
    pyperclip.copy(henkan)  # クリップボードにhenkanの内容をコピーする


def copyfukugen():  # fukugenの内容をコピーする関数
    fukugennaiyou = fukugen.get()  # fukugenの内容を取得することをfukugennaiyouと定義
    pyperclip.copy(fukugennaiyou)  # クリップボードにfukugennaiyouの内容をコピーする


def fukugensuru():
    fukugen.delete(0, tk.END)
    fukugensurunari = kekka.get()
    fukugensimasu = fukugensurunari.encode("cp932")
    fukugen_dekimasita = fukugensimasu.decode("utf-8", errors="ignore")
    fukugen.insert(0, fukugen_dekimasita)


def clearboxing():  # ボックスをクリーンする関数
    txt.delete(0, tk.END)  # txtのテキストボックスを内容を削除する
    kekka.delete(0, tk.END)  # kekkaのテキストボックスの内容を削除する
    fukugen.delete(0, tk.END)  # fukugenというテキストボックスの内容を削除する


def exityamete():  # やめていかないで
    sys.exit(0)  # ソフトを終了する


label = tk.Label(text="生み出したい怪言語")  # labelというラベル
label.place(x=100, y=40)  # labelの位置
txt = tk.Entry(width=50)  # labelのテキストボックス "txt"
txt.place(x=230, y=40)  # txtの位置

label2 = tk.Label(text="出てきた怪言語")  # label2というラベル
label2.place(x=100, y=70)  # label2の位置
kekka = tk.Entry(width=50)  # label2のテキストボックス "kekka"
kekka.place(x=230, y=70)  # kekkaの位置

label3 = tk.Label(text="復元された怪言語")  # label3というラベル
label3.place(x=100, y=100)  # label3の位置
fukugen = tk.Entry(width=50)  # label3のテキストボックス "fukguen"
fukugen.place(x=230, y=100)  # fukugenの場所

btn = tk.Button(root, text='命を捧げよ', command=btn_click)  # btnというボタン
# 押すとbtn_clickが実行される
btn.place(x=0, y=0)  # btnの位置

fukugenbutton = tk.Button(root, text="復元する", command=fukugensuru)
fukugenbutton.place(x=0, y=40)

clearbox = tk.Button(root, text="存在を抹消", command=clearboxing)  # clearboxというボタン
# 押すとclearboxingが実行される
clearbox.place(x=97, y=0)  # clearboxの位置

exitbutton = tk.Button(root, text="やめろ押すな", command=exityamete)  # exitbuttonというボタン
# 押すとexityameteが実行される
exitbutton.place(x=0, y=160)  # exitbuttonの位置

fukugencopy = tk.Button(root, text="復元コピー", command=copyfukugen)  # fukugencopyと言うボタン
# 押すとcopyfukugenが実行される
fukugencopy.place(x=197, y=0)  # fukugencopyの位置

lookeverytimes = tk.Label(root, text="電磁波攻撃を気にせずに、プライバシーに闇を")
lookeverytimes.place(x=230, y=150)

donotalive = tk.Label(root, text="著作権はすべて、チョング王にあり")  # donotaliveというラベル
donotalive.place(x=250, y=170)  # donotaliveの位置

versions = tk.Label(root, text="ver 1.0.1")  # バージョン表記
versions.place(x=630, y=170)  # versionsの位置

root.mainloop()  # tkinterで無限ループさせるもの、これがないとウインドウが表示されてもボタン類が表示されない
