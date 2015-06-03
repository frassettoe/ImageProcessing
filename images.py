# from PIL import Image  # To import an image.
import matplotlib.pyplot as plt  # To display an image
import numpy  # To manipulate matrices
from scipy import misc  # To load an image
from copy import deepcopy
#This is just a test
#How do you use github?  Who knows.
#still a test

def display(image):
    plt.imshow(image)
    plt.show()


def edge_detection(image, threshold):
    edges = deepcopy(image)
    # Create white edge image.
    for i in range(len(image)):
        for j in range(len(image[0])):
            edges[i][j] = [255, 255, 255]

    for i in range(1, len(image) - 1):
        for j in range(1, len(image[0]) - 1):
            for k in [0]:

                diffs = []
                diffs.append(abs(image[i][j][k] - image[i - 1][j - 1][k]))
                diffs.append(abs(image[i][j][k] - image[i][j - 1][k]))
                diffs.append(abs(image[i][j][k] - image[i + 1][j - 1][k]))
                # diffs.append(abs(image[i][j][k] - image[i - 1][j - 1][k]))
                # diffs.append(abs(image[i][j][k] - image[i - 1][j][k]))

                add_edge = 0
                for diff in diffs:
                    if diff > threshold:
                        add_edge += 1

                # if add_edge == len(diffs):
                if abs(sum(diffs)) / len(diffs) > threshold:
                    edges[i][j] = [0, 0, 0]
    display(image)
    display(edges)


def image_inverse(image):
    new_image = deepcopy(image)
    for i in range(len(image)):
        for j in range(len(image[0])):
            for k in range(3):
                new_image[i][j][k] = 255 - new_image[i][j][k]

    display(image)
    display(new_image)


def linear_combination(image1, image2, a=0.5):
    image1 *= a
    image2 *= (1 - a)
    comp = numpy.add(image1, image2)
    display(comp)


def composite(overlay, backgound):
    new_image = deepcopy(overlay)

    for i in range(len(overlay)):
        for j in range(len(overlay[0])):
            for k in range(3):
                if overlay[i][j][k] < 180:
                    new_image[i][j][k] = overlay[i][j][k]
                else:
                    new_image[i][j][k] = backgound[i][j][k]

    display(new_image)

# Read in images.
toad = misc.imread("toad.jpg")
ripon = misc.imread("ripon.jpg")
lamb = misc.imread("lamb.jpg")
tin = misc.imread("tin.jpg")
hair = misc.imread("hair.jpg")
dorothy = misc.imread("dorothy.png")


# Do edge detection
edge_detection(ripon, 100)
# edge_detection(tin, 250)

# image_inverse(dorothy)

#composite(hair, lamb)

#linear_combination(lamb, hair, a=0.4)
#display(hair)
