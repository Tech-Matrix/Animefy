import cv2
import numpy as np

'''def read_file(filename):
  img = cv2.imread(filename)
  cv2_imshow(img)
  return img'''
def color_quantization(img, k):
# Transform the image
  data = np.float32(img).reshape((-1, 3))

# Determine criteria
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

# Implementing K-Means
  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result

def edge_mask(img, line_size, blur_value):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_blur = cv2.medianBlur(gray, blur_value)
  edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
  return edges

#uploaded = files.upload()

#filename = next(iter(uploaded))

def filter_func(filename) :
    img = cv2.imread(filename)
    line_size = 5
    blur_value = 7

    edges = edge_mask(img, line_size, blur_value)
    #cv2.imshow("newolf",edges)
    cv2.imwrite("blackwhite.jpg",edges)
    blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200,sigmaSpace=200)
    #cv2_imshow("newolf",blurred)
    #cv2.imwrite("blackwhite.jpg",blurred)

    total_color = 9

    blurred = color_quantization(blurred, total_color)
    #cv2_imshow("newolf",blurred)

    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
    #cv2.imshow("newolf",cartoon)
    cv2.imwrite("toonify.jpg",cartoon)
