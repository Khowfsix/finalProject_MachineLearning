from matplotlib import pyplot as plt
import numpy as np
import streamlit as st
import os
from PIL import Image


def grad(x):
    return 2 * x + 5 * np.cos(x)


def cost(x):
    return x ** 2 + 5 * np.sin(x)


def myGD1(x0, eta):
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta * grad(x[-1])
        if abs(grad(x_new)) < 1e-3:  # just a small number
            break
        x.append(x_new)
    return (x, it)


def returnBieuDo(self):
    return self.plt


def executeThisFunction():
    x0 = -5
    eta = 0.1
    (x, it) = myGD1(x0, eta)
    x = np.array(x)
    y = cost(x)

    n = 101
    xx = np.linspace(-6, 6, n)
    yy = xx ** 2 + 5 * np.sin(xx)

    currentDir = os.path.abspath(os.path.dirname(__file__))




    plt.subplot(2, 4, 1)
    plt.plot(xx, yy)
    index = 0
    plt.plot(x[index], y[index], 'ro')
    s = ' iter%d/%d, grad=%.3f ' % (index, it, grad(x[index]))
    plt.xlabel(s, fontsize=8)
    plt.axis([-7, 7, -10, 50])

    plt.subplot(2, 4, 2)
    plt.plot(xx, yy)
    index = 1
    plt.plot(x[index], y[index], 'ro')
    s = ' iter%d/%d, grad=%.3f ' % (index, it, grad(x[index]))
    plt.xlabel(s, fontsize=8)
    plt.axis([-7, 7, -10, 50])

    plt.subplot(2, 4, 3)
    plt.plot(xx, yy)
    index = 2
    plt.plot(x[index], y[index], 'ro')
    s = ' iter%d/%d, grad=%.3f ' % (index, it, grad(x[index]))
    plt.xlabel(s, fontsize=8)
    plt.axis([-7, 7, -10, 50])

    plt.subplot(2, 4, 4)
    plt.plot(xx, yy)
    index = 3
    plt.plot(x[index], y[index], 'ro')
    s = ' iter%d/%d, grad=%.3f ' % (index, it, grad(x[index]))
    plt.xlabel(s, fontsize=8)
    plt.axis([-7, 7, -10, 50])

    plt.subplot(2, 4, 5)
    plt.plot(xx, yy)
    index = 4
    plt.plot(x[index], y[index], 'ro')
    s = ' iter%d/%d, grad=%.3f ' % (index, it, grad(x[index]))
    plt.xlabel(s, fontsize=8)
    plt.axis([-7, 7, -10, 50])

    plt.subplot(2, 4, 6)
    plt.plot(xx, yy)
    index = 5
    plt.plot(x[index], y[index], 'ro')
    s = ' iter%d/%d, grad=%.3f ' % (index, it, grad(x[index]))
    plt.xlabel(s, fontsize=8)
    plt.axis([-7, 7, -10, 50])

    plt.subplot(2, 4, 7)
    plt.plot(xx, yy)
    index = 7
    plt.plot(x[index], y[index], 'ro')
    s = ' iter%d/%d, grad=%.3f ' % (index, it, grad(x[index]))
    plt.xlabel(s, fontsize=8)
    plt.axis([-7, 7, -10, 50])

    plt.subplot(2, 4, 8)
    plt.plot(xx, yy)
    index = 11
    plt.plot(x[index], y[index], 'ro')
    s = ' iter%d/%d, grad=%.3f ' % (index, it, grad(x[index]))
    plt.xlabel(s, fontsize=8)
    plt.axis([-7, 7, -10, 50])

    plt.tight_layout()
    # plt.show()
    st.pyplot(plt)

    code = '''yy = xx ** 2 + 5 * np.sin(xx)'''
    st.code(code, language='python')
    filepath = os.path.join(currentDir, "../assets/images/giamDanDaoHam/hamBai01GDDH.png")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)

    code = '''def cost(x):
        return x ** 2 + 5 * np.sin(x)'''
    st.code(code, language='python')
    st.write("H??m n??y d??ng ????? t??nh ?????o h??m")

    code =  '''def myGD1(x0, eta):
        x = [x0]
        for it in range(100):
            x_new = x[-1] - eta * grad(x[-1])
            if abs(grad(x_new)) < 1e-3:  # just a small number
                break
            x.append(x_new)
        return (x, it)'''
    st.code(code, language='python')
    st.write("Cost ????? t??nh gi?? tr??? c???a h??m s???. H??m n??y kh??ng s??? d???ng trong thu???t to??n nh??ng th?????ng ???????c d??ng ????? ki???m tra vi???c t??nh ?????o h??m c?? ????ng kh??ng ho???c ????? xem gi?? tr??? c???a h??m s??? c?? gi???m theo m???i v??ng l???p hay kh??ng.")

    st.subheader("??i???m xu???t ph??t kh??c nhau")
    st.write("Sau khi ???? c?? c??c h??m c???n thi???t, ch??ng ta th??? t??m nghi???m v???i c??c ??i???m kh???i t???o kh??c nhau l?? x0 = ???5 v?? x0 = 5, v???i c??ng learning rate ?? = 0.1.")
    code = '''(x1, it1) = myGD1(-5, .1)
(x2, it2) = myGD1(5, .1)
print(???Solution x1 = %f, cost = %f, after %d iterations???%(x1[-1], cost(x1[-1]), it1))
print(???Solution x2 = %f, cost = %f, after %d iterations???%(x2[-1], cost(x2[-1]), it2))
            '''
    st.code(code, language='python')

    st.write("K???t qu???:")
    code = '''Solution x1 = -1.110667, cost = -3.246394, after 11 iterations
Solution x2 = -1.110341, cost = -3.246394, after 29 iterations
'''
    st.code(code, language='python')
