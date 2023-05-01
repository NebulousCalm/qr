url = "https://www.google.com" # sample, testing URL

import qrcode # module import

qr = qrcode.QRCode(
  version = 1, # 1-40, controls size
  error_correction = qrcode.constants.ERROR_CORRECT_H, # corrects ~30% of errors
  box_size = 10, # How many pixels in each "box"
  border = 4, # How many boxes thick the border should be (default of 4)
)

qr.add_data(url) # populate with URL
qr.make(fit=True) # create

img = qr.make_image(fill_color="white", back_color="black") # choose colors (fill color is bg despite wording)
img.save("qrcode.png") # save as an image in file system

# created by Zachary Richman
