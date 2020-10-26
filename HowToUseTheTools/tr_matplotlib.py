import matplotlib.pyplot as plt
import matplotlib.style

# ggplotスタイルの指定
matplotlib.style.use('ggplot')

# データの用意
x = [1, 2, 3]
y = [1, 4, 9]

# 折れ線グラフの描画
plt.plot(x, y)
# グラフのタイトルの指定
plt.title('title')

# グラフの表示
plt.show()
