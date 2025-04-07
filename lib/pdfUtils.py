from PIL import Image, ImageFont, ImageDraw  # requires python -m pip install Pillow

font_name = "cour"
font_size = 10

pdf_bg = 255
pdf_mode = "L"
pdf_scale = 4
pdf_width = 1100 * pdf_scale
pdf_height = 850 * pdf_scale
pdf_text_size = font_size * pdf_scale
pdf_pos_x = pdf_text_size
pdf_pos_start_y = pdf_text_size
pdf_pos_y = pdf_pos_start_y
pdf_file_name = "output.pdf"
pdf_format = "PDF"
pdf_res = 72

img = None
imgFont = None
draw = None

def setup_pdf():
    global img
    global imgFont
    global draw

    img = Image.new(mode=pdf_mode, size=(pdf_width, pdf_height), color=pdf_bg)
    imgFont = ImageFont.truetype(font_name, pdf_text_size)
    draw = ImageDraw.Draw(im=img)


def add_to_pdf(input):
    global imgFont
    global draw
    global pdf_pos_y

    draw.text(xy=(pdf_pos_x, pdf_pos_y), font=imgFont, text=input, fill=0)
    pdf_pos_y = pdf_pos_y + pdf_text_size


def write_pdf():
    global img

    img.save(fp=pdf_file_name, format=pdf_format, resolution=pdf_res, save_all=True)
