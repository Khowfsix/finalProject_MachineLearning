from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

N = 1500
np.random.seed(100)


def main():
    centers = [[2, 3], [5, 5], [1, 8]]
    n_classes = len(centers)
    data, labels = make_blobs(n_samples=N,
                              centers=np.array(centers),
                              random_state=1)
    nhom_0 = []
    nhom_1 = []
    nhom_2 = []

    for i in range(N):
        if labels[i] == 0:
            nhom_0.append([data[i, 0], data[i, 1]])
        elif labels[i] == 1:
            nhom_1.append([data[i, 0], data[i, 1]])
        else:
            nhom_2.append([data[i, 0], data[i, 1]])


    nhom_0 = np.array(nhom_0)
    nhom_1 = np.array(nhom_1)
    nhom_2 = np.array(nhom_2)

    plt.plot(nhom_0[:, 0], nhom_0[:, 1], 'og', markersize=2)
    plt.plot(nhom_1[:, 0], nhom_1[:, 1], 'or', markersize=2)
    plt.plot(nhom_2[:, 0], nhom_2[:, 1], 'ob', markersize=2)

    res = train_test_split(data, labels,
                           train_size=0.8,
                           test_size=0.2,
                           random_state=1)

    train_data, test_data, train_labels, test_labels = res

    # default = 5
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(train_data, train_labels)
    predicted = knn.predict(test_data)

    sai_so = accuracy_score(test_labels, predicted)
    print("Sai so: ", sai_so)

    predicted = knn.predict([[100, 100]])
    print("Predictions from the classifier:")
    print(predicted)

    plt.show()


if __name__ == "__main__":
    main()

