from PIL import Image, ImageDraw, ImageFilter




def password_check(password):
    # has_num = False
    # has_6_chars = False
    # has_upper = False
    # has_lower = False
    # has_symbol = False
    special_chars = "#$%^&*()-+?!_=,<>/"
    if len(password) >= 6:
        print("has_6_chars")
        # has_6_chars = True
    else:
        return False
    if any(char.isdigit() for char in password):
        print("has_num")
        # has_num = True
    else:
        return False
    if any(char.isupper() for char in password):
        print("has_upper")
        # has_upper = True
    else:
        return False
    if any(char.islower() for char in password):
        print("has_lower")
        # has_lower = True
    else:
        return False
    if any(char in special_chars for char in password):
        # has_symbol = True
        print("has_symbol")
        print("password OK")
        return True

def generate_thumbnail(img, tmbsize):
    img_width, img_height = img.size
    img_cropped =  img.crop(((img_width - min(img.size)) // 2,(img_height - min(img.size)) // 2,(img_width + min(img.size)) // 2,(img_height + min(img.size)) // 2))
    return img_cropped.resize((tmbsize, tmbsize), Image.LANCZOS)

# def resize_fixed_width(img, width):
#     img_width, img_height = img.size
#     ratio = img_width/