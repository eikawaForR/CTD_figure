# CTDグラフ化ツール

CTDのデータをグラフにするものです．<br>

現在は実行した際に各観測地点ごとの塩分，海水密度，海水温の鉛直構造がそれぞれfiguresディレクトリにpng形式で出力されるようになっています．
<br><br>
![image](https://github.com/user-attachments/assets/656f74ef-b779-4ee7-adc7-66a92cd8f8ab)
<br><br>
(例図)2336航海でのSt.1で計測した塩分と深さのグラフ<br>

## Dependencies
+ seabird
+ matplotlib.pyplot
<br><br>

## Usage

### 1. データファイルの作成
各観測点のデータが入ったcnvファイルを入手，または作成する．
<br>

### 2. CTD_figure.pyを編集


```
#航海番号？と最大St名を入力
#Userが操作するのはここ↓
Vo_No=2336
max_St_No=3
```

### 3. run CTD_figure.py
<br>

## Auther
Kentaro Eikawa


