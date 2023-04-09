import cv2

# image resizer
print("--Image resizer using opencv.")

# takes path of image from user. 
image_path = input("Enter Path ot Image Resize : ")


image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
# just show image
# cv2.imshow("title", src)

# scale down the image
_scaledown = int(input("Enter the size to scale down the image by % : "))
scale_percent = _scaledown

# calculate the scale percent of the original dimensions
new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(image, (new_width, new_height))

# saves output as new file 
new_file = input("Enter new file name : ")
ext = input("Enter extension [ jpg / jpeg / png ] : ")
cv2.imwrite(f"{new_file}.{ext}", output)
cv2.waitKey(0)
