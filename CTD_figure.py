import seabird
from seabird.cnv import fCNV
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Noto Sans CJK JP'
plt.rcParams["font.size"]=14

#Userが操作するのはここ↓
#航海番号？と最大St名を入力
Vo_No=2336
max_St_No=3

#辞書型にするために空の辞書を作成
CTD_DATA={}

for St_No in range(1,max_St_No+1):
    name=f"{Vo_No}_st{St_No}"

    #fCNVライブラリを使ってcnvファイルの読み取り
    CTD_DATA[St_No]=fCNV(f"./data/{name}.cnv")

    #塩分と深さの図
    fig, ax=plt.subplots()
    #ax?の形にして図をいじりやすくした
    fig, ax = plt.subplots()
    ax.plot(CTD_DATA[St_No]["PSAL"],CTD_DATA[St_No]["DEPTH"])
    #軸の方向を逆向きに
    ax.invert_yaxis()
    ax.set_xlabel("PSAL(塩分)[PSU]",labelpad=10)
    ax.set_ylabel("DEPTH(深さ)[m]",labelpad=10)
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
    plt.savefig(f"./figures/St{St_No}_Depth_salt.png")
    plt.close()

    #海水密度と深さの図
    fig2, ax2=plt.subplots()
    ax2.plot(CTD_DATA[St_No]["sigma_t"],CTD_DATA[St_No]["DEPTH"])
    #軸の方向を逆向きに
    ax2.invert_yaxis()
    ax2.set_xlabel("sigma-t(海水密度)[kg/m³]",labelpad=10)
    ax2.set_ylabel("DEPTH(深さ)[m]",labelpad=10)
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
    plt.savefig(f"./figures/St{St_No}_Depth_sigma-t.png")
    plt.close()

    #海水温と深さの図
    fig3, ax3=plt.subplots()
    ax3.plot(CTD_DATA[St_No]["TEMP"],CTD_DATA[St_No]["DEPTH"])
    #軸の方向を逆向きに
    ax3.invert_yaxis()
    ax3.set_xlabel("TEMP(水温)[℃]",labelpad=10)
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
    plt.savefig(f"./figures/St{St_No}_Depth_TEMP.png")
    plt.close()
