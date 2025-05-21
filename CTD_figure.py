import numpy as np
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Noto Sans CJK JP'
plt.rcParams["font.size"]=14

#航海番号？と最大St名を入力
#Userが操作するのはここ↓
Vo_No=2336
max_St_No=3

#辞書型にするために空の辞書を作成
CTD_DATA={}

for St_No in range(1,max_St_No+1):
    name=f"{Vo_No}_st{St_No}"
    
    #python/Reserchディレクトリにいる前提
    #pandasでascファイルの読み取り，sep=r'\s+'は空白区切りのコード
    #ディレクトリ構造についてはデータ見てから書き換える
    pd_ctd_data=pd.read_csv(f"./data/{name}.asc",sep=r'\s+')
    
    #pandasで出したデータをxarrayに変換，PrSMの列を探している．
    #ついでに辞書型にしてSt毎のデータの区別
    CTD_DATA[St_No]=pd_ctd_data.set_index("PrSM").to_xarray()
    print(f"--------------------\nCTD_DATA_St.{St_No}\n--------------------")
    print(CTD_DATA[St_No])


    #塩分と深さの図
    fig, ax=plt.subplots()
    #ax?の形にして図をいじりやすくした
    fig, ax = plt.subplots()
    ax.plot(CTD_DATA[St_No].Sal00,CTD_DATA[St_No].DepSM)
    #軸の方向を逆向きに
    ax.invert_yaxis()
    ax.set_xlabel("sal00(塩分)[PSU]",labelpad=10)
    ax.set_ylabel("Depth(深さ)[m]",labelpad=10)
    ax.set_ylim(top=0)
    #titleはlabelじゃないのでpadで距離感を調整
    ax.set_title(f"CTD塩分(ST.{St_No})",pad=15)
    #x軸メモリ，ラベルを上側に
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")
    #背景にグリッドを設定
    ax.grid(True)
    ##枠線を消す（やっぱ要る）
    #for spine in ax.spines.values():
    #    spine.set_visible(False)
    #目盛り線を消す
    ax.tick_params(axis="both",which="both",length=0)
    #図の大きさ補正
    plt.tight_layout()
    #該当ディレクトリに保存
    plt.savefig(f"./figures/St{St_No}_DepSM_salt.png")
    plt.close()

    #海水密度と深さの図
    fig2, ax2=plt.subplots()
    ax2.plot(CTD_DATA[St_No]["Sigma-t00"],CTD_DATA[St_No].DepSM)
    #軸の方向を逆向きに
    ax2.invert_yaxis()
    ax2.set_xlabel("Sigma-t00(海水密度)[kg/m³]",labelpad=10)
    ax2.set_ylabel("Depth(深さ)[m]",labelpad=10)
    ax2.set_ylim(top=0)
    ax2.set_title(f"CTD海水密度(St.{St_No})",pad=15)
    #x軸メモリ，ラベルを上側に
    ax2.xaxis.set_ticks_position("top")
    ax2.xaxis.set_label_position("top")
    #背景にグリッドを設定
    ax2.grid(True)
    #目盛り線を消す
    ax2.tick_params(axis="both",which="both",length=0)
    #図の大きさ補正
    plt.tight_layout()
    #該当ディレクトリに保存
    plt.savefig(f"./figures/St{St_No}_DepSM_Sigma-t00.png")
    plt.close()

    #海水温と深さの図
    fig3, ax3=plt.subplots()
    ax3.plot(CTD_DATA[St_No].T090C,CTD_DATA[St_No].DepSM)
    #軸の方向を逆向きに
    ax3.invert_yaxis()
    ax3.set_xlabel("T090C(水温)[℃]",labelpad=10)
    ax3.set_ylabel("Depth(深さ)[m]",labelpad=10)
    ax3.set_ylim(top=0)
    ax3.set_title(f"CTD水温(St.{St_No})",pad=15)
    #x軸メモリ，ラベルを上側に
    ax3.xaxis.set_ticks_position("top")
    ax3.xaxis.set_label_position("top")
    #背景にグリッドを設定
    ax3.grid(True)
    #目盛り線を消す
    ax3.tick_params(axis="both",which="both",length=0)
    #図の大きさ補正
    plt.tight_layout()
    #該当ディレクトリに保存
    plt.savefig(f"./figures/St{St_No}_DepSM_T090C.png")
    plt.close()
