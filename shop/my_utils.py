from PIL import Image, ImageDraw, ImageFilter




def password_check(password, username):

    special_chars = "#$%^&*()-+?!_=,<>/"
    s1 = "too short"
    s2 = "username similar to password"
    s3 = "no digit used"
    s4 = "at least one upper letter"
    s5 = "at least one lower letter"
    s6 = "use at least one valid character: #$%^&*()-+?!_=,<>/"
    s7 = "ok"

    if len(password) >= 6:
        pass
    else:
        return s1
    if username not in password:
        pass
    else:
        return s2
    if any(char.isdigit() for char in password):
        pass
    else:
        return s3
    if any(char.isupper() for char in password):
        pass
    else:
        return s4
    if any(char.islower() for char in password):
        pass
    else:
        return s5
    if any(char in special_chars for char in password):
        return s7
    else:
        return s6

def generate_thumbnail(img, tmbsize):
    img_width, img_height = img.size
    img_cropped =  img.crop(((img_width - min(img.size)) // 2,(img_height - min(img.size)) // 2,(img_width + min(img.size)) // 2,(img_height + min(img.size)) // 2))
    return img_cropped.resize((tmbsize, tmbsize), Image.LANCZOS)

# def resize_fixed_width(img, width):
#     img_width, img_height = img.size
#     ratio = img_width/