
### 検索ツールサンプル
### これをベースに課題の内容を追記してください
from os import path
import csv

### ４．３に追加してリストをCSVから読み込んで登録できるようにしてみましょう
### 検索ソースリスト取得処理
def get_sources_csv(csv_path) :
    # CSV読み込み
    csv_file = open(csv_path, "r", encoding = "utf-8")
    line = csv.reader(csv_file, delimiter = ",")
    # 検索ソースリストを返却
    return next(line)

### CSV更新処理
def upd_sources_csv(csv_path, new_list) :
    # CSV読み込み
    csv_file = open(csv_path, "w", encoding = "utf-8-sig", newline = "")
    writer = csv.writer(csv_file, delimiter = ",")
    # CSV更新
    writer.writerow(new_list)

# CSVファイルのパス
csv_path = path.dirname(__file__) + "/CHARACTER_LIST.csv"
# 検索ソースリスト
sources = get_sources_csv(csv_path)

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    ### １．入力したワードで、リストを検索して結果をPrint文で表示してみましょう
    # 検索結果
    result = False
    # 検索ソースリストに入力ワードが存在する場合
    if word in sources :
        # 検索結果を更新
        result = True

    # 検索結果=True
    if result :
        # 結果を出力
        print("{}が見つかりました".format(word))

    ### ２．１に追加して結果が存在した場合と、しなかった場合で表示する文言が変わるようにしてみましょう
    # 検索結果=False
    else :
        # 結果を出力
        print("{}は見つかりませんでした".format(word))

        ###３．２に追加して結果が存在しなかった場合に、リストに追加できるようにしてみましょう
        # 検索ソースリストへ追加
        sources.append(word)
        # 検索ソースリストのCSVファイルを更新
        upd_sources_csv(csv_path, sources)

if __name__ == "__main__":
    search()
