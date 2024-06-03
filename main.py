import cv2
import numpy as np

def main(image1, image2):

    # 转换为 RGB 颜色空间

    # 提取红色区域（示例：假设红色在 HSV 中的范围为 [0, 100, 100] 到 [10, 255, 255]）
    lower_red = np.array([0, 0, 200])
    upper_red = np.array([0, 0, 255])
    mask1 = cv2.inRange(image1, lower_red, upper_red)
    mask2 = cv2.inRange(image2, lower_red, upper_red)
    contours1, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_contour2 = max(contours2, key=cv2.contourArea)
    max_contour1 = max(contours1, key=cv2.contourArea)
    x1, y1, w1, h1 = cv2.boundingRect(max_contour1)
    x2, y2, w2, h2 = cv2.boundingRect(max_contour2)
    cv2.rectangle(image1, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
    cv2.rectangle(image2, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 2)
    cv2.imshow("Image 1", image1)
    cv2.imshow("Image 2", image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__=="__main__":
    img1 = cv2.imread('src.jpg')
    img2 = cv2.imread('dst2.jpg')

    similarity = main(img1, img2)
    