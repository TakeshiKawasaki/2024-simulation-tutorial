import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
#図の解像度が上がる
%config InlineBackend.figure_format = 'retina'
import numpy as np

#Tex フォント（任意）:使いたい人は以下のコメントアウトを開放 
#plt.rcParams["text.usetex"] =True 
plt.rcParams['font.family'] = 'Arial' #使用するフォント名
plt.rcParams["font.size"] = 25

#図全体のサイズやアスペクト比を変える
fig = plt.figure(figsize=(18,12))
#複数の図を並べる時ここを変える

 ###########################
ax = fig.add_subplot(221)
#各自ファイルのパスを変えること
i, pi,error  = np.loadtxt("./Lecture2/pi-error.dat", comments='#', unpack=True)
plt.plot(i, pi, "o-",markersize=10,color="b",label=r"rand()")
plt.xscale('log')
###Drawing a line ######
x= np.linspace(1e4, 1e8, 100) 
y= np.pi+0*x
plt.plot(x, y, "--",markersize=3,linewidth = 2.0, color="k",label=r"$\pi$")
#########
#図の書式設定
plt.tick_params(which='major',width = 1, length = 10)
plt.tick_params(which='minor',width = 1, length = 5)
plt.minorticks_on()
ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.xlabel(r"$n$",color='k', size=30)
plt.ylabel(r"$\pi(n)$",color='k', size=30)

#図の凡例の有無や位置，サイズを調整
plt.legend(ncol=1, loc=4, borderaxespad=0, fontsize=25,frameon=False)
#各グラフのアスペクト比を1:1にする
#################################

 ###########################
ax = fig.add_subplot(222)
#各自ファイルのパスを変えること
i, pi,error  = np.loadtxt("./Lecture2/pi-error.dat", comments='#', unpack=True)
plt.plot(i, error, "x-",markersize=10,color="r",label=r"rand()")
plt.xscale('log')
plt.yscale('log')

###Drawing a line ######
x= np.linspace(1e4, 1e8, 100) 
y=1/x**0.5
plt.plot(x, y, "--",markersize=3,linewidth = 2.0, color="k",label=r"$\propto 1/\sqrt{n}$")
#########


#図の書式設定
plt.tick_params(which='major',width = 1, length = 10)
plt.tick_params(which='minor',width = 1, length = 5)
plt.minorticks_on()
ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.xlabel(r"$n$",color='k', size=30)
plt.ylabel(r"$\delta(n)$",color='k', size=30)

#図の凡例の有無や位置，サイズを調整
plt.legend(ncol=1, loc=1, borderaxespad=0, fontsize=25,frameon=False)
#################################

 ###########################

ax = fig.add_subplot(223)
#各自ファイルのパスを変えること
i, pi,error  = np.loadtxt("./Lecture2/pi-error-MT.dat", comments='#', unpack=True)
plt.plot(i, pi, "D-",markersize=10,color="g",label=r"MT")
plt.xscale('log')
###Drawing a line ######
x= np.linspace(1e4, 1e8, 100) 
y= np.pi+0*x
plt.plot(x, y, "--",markersize=3,linewidth = 2.0, color="k",label=r"$\pi$")
#########

#図の書式設定
plt.tick_params(which='major',width = 1, length = 10)
plt.tick_params(which='minor',width = 1, length = 5)
plt.minorticks_on()
ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.xlabel(r"$n$",color='k', size=30)
plt.ylabel(r"$\pi(n)$",color='k', size=30)

#図の凡例の有無や位置，サイズを調整
plt.legend(ncol=1, loc=4, borderaxespad=0, fontsize=25,frameon=False)
#################################

###########################

ax = fig.add_subplot(224)
#各自ファイルのパスを変えること
i, pi,error  = np.loadtxt("./Lecture2/pi-error-MT.dat", comments='#', unpack=True)
plt.plot(i, error, "s-",markersize=10,color="m",label=r"MT")

###Drawing a line ######
x= np.linspace(1e4, 1e8, 100) 
y=1/x**0.5
plt.plot(x, y, "--",markersize=3,linewidth = 2.0, color="k",label=r"$\propto 1/\sqrt{n}$")
#########
plt.xscale('log')
plt.yscale('log')
#図の書式設定
plt.tick_params(which='major',width = 1, length = 10)
plt.tick_params(which='minor',width = 1, length = 5)
plt.minorticks_on()
ax.spines['top'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['left'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)
plt.xlabel(r"$n$",color='k', size=30)
plt.ylabel(r"$\delta(n)$",color='k', size=30)

#図の凡例の有無や位置，サイズを調整
plt.legend(ncol=1, loc=1, borderaxespad=0, fontsize=25,frameon=False)
#################################

#図のマージン設定
plt.subplots_adjust(wspace=0.3, hspace=0.3)

#各自ファイルのパスを変えること．
plt.savefig('./Lecture2/pi-error.png')
plt.savefig('./Lecture2/pi-error.pdf')
