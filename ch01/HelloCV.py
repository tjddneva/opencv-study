import sys
import cv2

print('hello OpenCV', cv2.__version__)

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image Load failed!')
    sys.exit()

cv2.imwrite('cat_gray.png', img)

# 없어도 imshow 가 자동으로 창 만듬 but 무조건 WINDOW_AUTOSIZE 로 설정됨
cv2.namedWindow('image')

cv2.imshow('image', img)
# cv2.waitKey()
while True:
    if cv2.waitKey() == ord('q'):
        break

# cv2.destroyAllWindows()
cv2.destroyWindow('image')  # 없어도 window 가 자동으로 회수
