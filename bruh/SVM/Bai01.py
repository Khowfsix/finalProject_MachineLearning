from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.svm import LinearSVC
from sklearn.inspection import DecisionBoundaryDisplay

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import os
from PIL import Image

np.random.seed(100)
N = 150


def executeThisFunction():
    centers = [[2, 2], [7, 7]]
    n_classes = len(centers)
    data, labels = make_blobs(n_samples=N,
                              centers=np.array(centers),
                              random_state=1)

    nhom_0 = []
    nhom_1 = []

    for i in range(0, N):
        if labels[i] == 0:
            nhom_0.append([data[i, 0], data[i, 1]])
        elif labels[i] == 1:
            nhom_1.append([data[i, 0], data[i, 1]])

    nhom_0 = np.array(nhom_0)
    nhom_1 = np.array(nhom_1)

    res = train_test_split(data, labels,
                           train_size=0.8,
                           test_size=0.2,
                           random_state=1)

    train_data, test_data, train_labels, test_labels = res

    nhom_0 = []
    nhom_1 = []

    # noinspection PyPep8Naming
    SIZE = train_data.shape[0]
    for i in range(0, SIZE):
        if train_labels[i] == 0:
            nhom_0.append([train_data[i, 0], train_data[i, 1]])
        elif train_labels[i] == 1:
            nhom_1.append([train_data[i, 0], train_data[i, 1]])

    nhom_0 = np.array(nhom_0)
    nhom_1 = np.array(nhom_1)

    svc = LinearSVC(C=100, loss="hinge", random_state=42, max_iter=100000)

    svc.fit(train_data, train_labels)

    he_so = svc.coef_
    intercept = svc.intercept_

    predicted = svc.predict(test_data)
    sai_so = accuracy_score(test_labels, predicted)
    print('sai so:', sai_so)

    my_test = np.array([[2.5, 4.0]])
    ket_qua = svc.predict(my_test)

    print('Ket qua nhan dang la nhom:', ket_qua[0])

    plt.plot(nhom_0[:, 0], nhom_0[:, 1], 'og', markersize=2)
    plt.plot(nhom_1[:, 0], nhom_1[:, 1], 'or', markersize=2)

    w = he_so[0]
    a = -w[0] / w[1]
    xx = np.linspace(2, 7, 100)
    yy = a * xx - intercept[0] / w[1]

    plt.plot(xx, yy, 'b')

    decision_function = svc.decision_function(train_data)
    support_vector_indices = np.where(np.abs(decision_function) <= 1 + 1e-15)[0]
    support_vectors = train_data[support_vector_indices]
    support_vectors_x = support_vectors[:, 0]
    support_vectors_y = support_vectors[:, 1]

    ax = plt.gca()

    # noinspection PyTypeChecker
    DecisionBoundaryDisplay.from_estimator(
        svc,
        train_data,
        ax=ax,
        grid_resolution=50,
        plot_method="contour",
        colors="k",
        levels=[-1, 0, 1],
        alpha=0.5,
        linestyles=["--", "-", "--"],
    )
    plt.scatter(
        support_vectors[:, 0],
        support_vectors[:, 1],
        s=100,
        linewidth=1,
        facecolors="none",
        edgecolors="k",
    )

    plt.legend(['Nhom 0', 'Nhom 1'])

    # plt.show()
    st.pyplot(plt)
    code = '''centers = [[2, 2], [7, 7]]
    n_classes = len(centers)
    data, labels = make_blobs(n_samples=N, 
                            centers=np.array(centers),
                            random_state=1)'''
    st.code(code, language="python")
    st.write(
        "S??? d???ng make_blobs ????? t???o c??c ?????m m??u v???i ph??n ph???i Gaussian. B???n c?? th??? ki???m so??t s??? l?????ng ?????m m??u s??? t???o v?? s??? l?????ng m???u s??? t???o, c??ng nh?? m???t lo???t c??c thu???c t??nh kh??c.")

    code = '''    for i in range(0, N):
        if labels[i] == 0:
            nhom_0.append([data[i,0], data[i,1]])
        elif labels[i] == 1:
            nhom_1.append([data[i,0], data[i,1]])'''
    st.code(code, language="python")
    st.write("Th??m ph???n t??? cho 2 m???ng nhom_0 v?? nhom_1")

    code = '''svc = LinearSVC(C = 100, loss="hinge", random_state=42, max_iter = 100000)'''
    st.code(code, language="python")
    st.write(
        "LinearSVC l?? m???t thu???t to??n c??? g???ng t??m m???t si??u ph???ng ????? t???i ??a h??a kho???ng c??ch gi???a c??c m???u ???????c ph??n lo???i.")

    code = '''predicted = svc.predict(test_data)
    sai_so = accuracy_score(test_labels, predicted)
    print('sai so:', sai_so)'''
    st.code(code, language="python")
    st.write("D??ng svc.predict() ????? d??? ??o??n d li???u v?? t??nh ???????c sai s??? b???ng c??ch s??i h??m accuracy_score")
    code = '''w = he_so[0]
    a = -w[0] / w[1]
    xx = np.linspace(2, 7, 100)
    yy = a * xx - intercept[0] / w[1]

    plt.plot(xx, yy, 'b')'''
    st.code(code, language="python")
    st.write("V??? ????? th??? b???ng c??ch d??? li???u t??? a, xx, yy")

    code = '''decision_function = svc.decision_function(train_data)
    support_vector_indices = np.where(np.abs(decision_function) <= 1 + 1e-15)[0]
    support_vectors = train_data[support_vector_indices]
    support_vectors_x = support_vectors[:,0]
    support_vectors_y = support_vectors[:,1]'''
    st.code(code, language="python")
    st.write(
        "Output c???a svc.decision_function l?? 1 h??m decision cho th???y ???????c ch??ng ta ??ang ??? g???n ???????ng boundary nh?? th??? n??o. C??ng g???n th?? ????? tin c???y c??ng th???p")

# if __name__ == '__main__':
#     executeThisFunction()
