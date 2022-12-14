from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from sklearn import datasets
from skimage import exposure
import numpy as np

import sklearn
import streamlit as st
import os
from PIL import Image
def executeThisFunction():
    # take the MNIST Data and construct the training and testing split, using 75% of the
    # Data for training and 25% for testing
    currentDir = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(currentDir, "../assets/images/KNN/digit.jpg")
    image = Image.open(filepath)
    st.image(image, caption='', use_column_width=True)
    mnist = datasets.load_digits()
    (trainData, testData, trainLabels, testLabels) = train_test_split(np.array(mnist.data),
                                                                      mnist.target, test_size=0.25, random_state=42)

    # now, let's take 10% of the training Data and use that for validation
    (trainData, valData, trainLabels, valLabels) = train_test_split(trainData, trainLabels,
                                                                    test_size=0.1, random_state=84)

    print("training Data points: ", len(trainLabels))
    print("validation Data points: ", len(valLabels))
    print("testing Data points: ", len(testLabels))
    st.write("testing Data points: ", len(testLabels))
    st.write("training Data points: ", len(trainLabels))
    st.write("validation Data points: ", len(valLabels))
    model = KNeighborsClassifier()
    model.fit(trainData, trainLabels)
    # evaluate the model and update the accuracies list
    score = model.score(valData, valLabels)
    print("accuracy = %.2f%%" % (score * 100))
    st.write("accuracy = %.2f%%" % (score * 100))

    # loop over a few random digits
    for i in list(map(int, np.random.randint(0, high=len(testLabels), size=(5,)))):
        # grab the image and classify it
        image = testData[i]
        prediction = model.predict(image.reshape(1, -1))[0]

        # convert the image for a 64-dim array to an 8 x 8 image compatible with OpenCV,
        # then resize it to 32 x 32 pixels so we can see it better
        image = image.reshape((8, 8)).astype("uint8")

        image = exposure.rescale_intensity(image, out_range=(0, 255))
        # image = imutils.resize(image, width=32, inter=cv2.INTER_CUBIC)

        # show the prediction
        print("I think that digit is: {}".format(prediction))
        st.write("I think that digit is: {}".format(prediction))
        # cv2.imshow("Image", image)
        # img_array = np.array(image)
        # cv2.imwrite('digitOut.jpg', cv2.cvtColor(img_array, cv2.IMREAD_GRAYSCALE))
        # image = Image.open('digitOut.jpg')
        # st.image(image, caption='Output', use_column_width=True)
        # st.pyplot(image)


    code = '''mnist = datasets.load_digits()'''
    st.code(code, language ="python")
    st.write("H??m load_digits() gi??p t???i v?? tr??? v??? t???p d??? li???u ch??? s???. Ph??n lo???i n??y ch???a c??c ??i???m d??? li???u, trong ???? m???i ??i???m d??? li???u l?? m???t h??nh ???nh 8X8 c???a m???t ch??? s???")

    code = '''(trainData, testData, trainLabels, testLabels) = train_test_split(np.array(mnist.data),
                                                            mnist.target, test_size=0.25, random_state=42)'''
    st.code(code, language="python")
    st.write("train_test_split l?? m???t ch???c n??ng trong l???a ch???n m?? h??nh Sklearn ????? chia m???ng d??? li???u th??nh hai t???p h???p con: d??nh cho d??? li???u hu???n luy???n v?? d??? li???u th??? nghi???m. V???i ch???c n??ng n??y, b???n kh??ng c???n ph???i chia t???p d??? li???u theo c??ch th??? c??ng.")

    code = '''score = model.score(valData, valLabels)'''
    st.code(code, language="python")
    st.write("??i???m m?? h??nh l?? m???t to??n t??? AI Studio l??u tr??? gi?? tr??? ???????c d??? ??o??n b???i m?? h??nh h???c t???p c?? gi??m s??t cho tr?????ng m???c ti??u.")


