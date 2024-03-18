import tkinter as tk
from tkinter import filedialog
from tkinter import *

import numpy as np
from PIL import ImageTk, Image
from keras.models import Sequential

import numpy
# Tải data đã train
from tensorflow.keras.models import load_model


model = load_model('my_model.h5')

# Các nhãn
classes = {0: 'Tốc độ tối đa (20km/h)',
           1: 'Tốc độ tối đa (30km/h)',
           2: 'Tốc độ tối đa (50km/h)',
           3: 'Tốc độ tối đa (60km/h)',
           4: 'Tốc độ tối đa (70km/h)',
           5: 'Tốc độ tối đa (80km/h)',
           6: 'Cấm xe tải vượt',
           7: 'Giao nhau với đường không ưu tiên',
           8: 'Đường ưu tiên',
           9: 'Giao nhau với đường ưu tiên',
           10: 'Dừng lại',
           11: 'Cấm',
           12: 'Cấm xe > 3.5T',
           13: 'Cấm đi ngược chiều',
           14: 'Nguy hiểm khác',
           15: 'Chỗ ngoặt bên trái',
           16: 'Chỗ ngoặt bên phải',
           17: 'Nhiều chỗ ngoặt liên tiếp',
           18: 'Đường gập ghềnh',
           19: 'Đường trơn trượt',
           20: 'Đường hẹp bên phải',
           21: 'Đường đang thi công',
           22: 'Biển báo giao thông',
           23: 'Người đi bộ cắt ngang',
           24: 'Trẻ em qua đường',
           25: 'Người đi xe đạp cắt ngang',
           26: 'Động vật qua đường',
           27: 'Hết tất cả lệnh cấm',
           28: 'Rẽ phải ở phía trước',
           29: 'Rẽ trái ở phía trước',
           30: 'Đi thẳng',
           31: 'Đi thẳng hoặc rẽ phải',
           32: 'Đi thẳng hoặc rẽ trái',
           33: 'Hướng đi vòng chướng ngại vật sang phải',
           34: 'Hướng đi vòng chướng ngại vật sang trái',
           35: 'Vòng xuyến',
           36: 'Hết lệnh cấm vượt',
           37: 'Hết lệnh cấm xe tải vượt',
           }

# Tạo giao diện
top = tk.Tk()
top.geometry('800x600')
top.title('Nhận diện biển báo GT')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    #pred = model.predict_classes([image])[0]
    pred = np.argmax(model.predict([image])[0], axis=-1)
    sign = classes[pred]
    print(sign)
    label.configure(foreground='#011638', text=sign)


def show_classify_button(file_path):
    classify_b = Button(top, text="Nhận diện", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.85)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


upload = Button(top, text="Tải ảnh lên", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))

upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Nhận dạng biển báo giao thông", pady=20, font=('arial', 20, 'bold'))

heading.configure(background='#CDCDCD', foreground='#364170')
heading.pack()
top.mainloop()
