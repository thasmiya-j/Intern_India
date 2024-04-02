import qrcode

# Data to encode
data = "https://www.example.com"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("example_qrcode.png")

print("QR code generated successfully!")

#T0 RETRIEVE THE SAVED IMAGE

from PIL import Image

# Open the saved image
img = Image.open("example_qrcode.png")

# Show the image
img.show()

