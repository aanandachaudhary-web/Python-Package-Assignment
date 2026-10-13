import qrcode

# Generate a QR code for a personal message
message = input("Enter your name or a short message: ")

img = qrcode.make(message)
img.save("personal_qrcode.png")

print("Personal QR code saved as personal_qrcode.png")

# Generate another QR code for a website
website = input("Enter your favourite website URL: ")

img = qrcode.make(website)
img.save("website_qrcode.png")

print("Website QR code saved as website_qrcode.png")