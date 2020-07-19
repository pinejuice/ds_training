import numpy as np

def create1DArray():
    # 1次元配列の作成
    a = np.array([1, 2, 3])
    print(a)
    # [1 2 3]
    print(type(a))
    # numpy.ndarray
    print(a.shape)
    # (3,) 1次元配列で要素が3

def create2DArray():
    # 2次元配列の作成
    b = np.array([[1, 2, 3], [4, 5, 6]])
    print(b)
    # [[1 2 3]
    #  [4 5 6]]
    print(b.shape)
    # (2, 3) 2×3行列だと判明

def arrayReshape():
    # 配列の変形(reshape)
    c1 = np.array([0, 1, 2, 3, 4, 5])
    print(c1)
    # [0 1 2 3 4 5]
    c2 = c1.reshape((2, 3))
    # 2×3行列に変換
    print(c2)
    # [[0 1 2]
    #  [3 4 5]]
    try:
        # 3×4行列に変換しようとしたが、要素数が足りず変換できない
        c1.reshape((3, 4))
    except Exception as e:
        print(e)
        # cannot reshape array of size 6 into shape (3,4)
    # 2×3行列を1次元配列に変換する
    # 返り値は参照値
    c3 = c2.ravel()
    print(c3)
    # [0 1 2 3 4 5]
    # 2×3行列を1次元配列に変換する
    # 返り値はコピー値
    c4 = c2.flatten()
    print(c4)
    # [0 1 2 3 4 5]

def indexAndSlice():
    a = np.array([1, 2, 3])
    # index
    print(a[0])
    # 1
    # slice
    print(a[1:])
    # [2 3]
    b = np.array([[1, 2, 3], [4, 5, 6]])
    print(b[0])
    # [1 2 3]
    print(b[1][1])
    # 5
    print(b[1, 1])
    # 5 b[2行目, 2列目]
    print(b[:, 2])
    # [3 6] b[:(行方向はすべて), 2(列方向は3行目)]
    print(b[1, :])
    # [4 5 6] b[2行目, すべて]
    print(b[0, 1:])
    # [2 3]

def dataResubstitution():
    a = np.array([1, 2, 3])
    a[2] = 4
    print(a)
    # [1 2 4]
    b = np.array([[1, 2, 3], [4, 5, 6]])
    b[1, 2] = 7
    print(b)
    # [[1 2 3]
    #  [4 5 7]]
    b[:, 2] = 8
    print(b)
    # [[1 2 8]
    #  [4 5 8]]

def deepCopy():
    a = np.array([1, 2, 3])
    a1 = a
    print(a1)
    # [1 2 3]
    a1[2] = 5
    print(a1)
    # [1 2 5]
    print(a)
    # [1 2 5]
    # a1とaは互いに参照しあっている
    a2 = a.copy()
    print(a2)
    # [1 2 5]
    a2[0] = 6
    print(a2)
    # [6 2 5]
    print(a)
    # [1 2 5]
    # a2とaは別々の配列とみなされている。
    # ravelメソッドは参照
    # flattenメソッドはコピー
    np_array1 = np.array([0, 1])
    np_array2 = np_array1[:]
    print(np_array1)
    print(np_array2)
    # どちらも[0 1]
    np_array2[0] = 2
    print(np_array1)
    print(np_array2)
    # どちらも[2 1]
    # スライスの結果は参照になる

def returnArange():
    print(np.arange(10))
    # [0 1 2 3 4 5 6 7 8 9]
    print(np.arange(1, 11))
    # [1 2 3 4 5 6 7 8 9 10]
    print(np.arange(1, 11, 2))
    # [1 3 5 7 9]


if __name__ == "__main__":
    create1DArray()
    create2DArray()
    arrayReshape()
    indexAndSlice()
    dataResubstitution()
    deepCopy()
    returnArange()
