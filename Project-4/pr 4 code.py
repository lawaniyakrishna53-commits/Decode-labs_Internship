import cv2
import pytesseract

# Set Tesseract path (change if different on your PC)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load image
image = cv2.imread('sample.jpg')

# Check if image is loaded
if image is None:
    print('Image not found!')
    exit()

# Step 1: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 2: Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 3: Apply Otsu Thresholding
_, thresh = cv2.threshold(blur, 0, 255,
                          cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Step 4: Extract text using OCR
text = pytesseract.image_to_string(thresh, config='--psm 6')

# Print extracted text
print('\n===== EXTRACTED TEXT =====\n')
print(text)

# Show images
cv2.imshow('Original Image', image)
cv2.imshow('Processed Image', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()