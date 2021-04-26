from tkinter import *
from tkinter import messagebox
import csv
from Logistic_Regression import *


# constants
GREY = "#d8e3e7"
BLUE = "#9dbeb9"
morbidite_degeri = pred.astype(int)[0]


# ----------- FUNCTIONALITY SETUP -------------- #
def add_to_csv(csv_dict):
    fields = ["Morbidite", "Ameliyat", "Asa Skoru", "Age", "gender", "BMI"]
    with open('data.csv', mode='a', newline="") as data_file:
        csv_writer = csv.DictWriter(data_file, fieldnames=fields, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(csv_dict)
    return


def check_input():
    """
    All the type checks are here so that the rest of the program can work accurately.
    """
    ameliyat_tipi = at_val_inside.get()
    cinsiyet = gender_val_inside.get()
    if ameliyat_tipi == "Lüften seçiniz." or cinsiyet == "Lütfen seçiniz.":
        messagebox.showwarning("Seçilmemiş Değerler Var!",
                               "Lütfen ameliyat tipi ve cinsiyeti seçtiğinizden emin olun.")
    else:
        try:
            yas = int(yas_entry.get())
            bmi = float(bmi_entry.get())
            asa_skoru = as_val_inside.get()
        except ValueError:
            messagebox.showwarning("Geçersiz Datatipi", "Lütfen yaş bölgesine tam sayı,"
                                                        " BMI bölgesine rasyonel sayı yazınız.")
        except TclError:
            messagebox.showwarning(
                "Seçilmemiş Değerler Var!", "Lütfen asa skorunu seçtiğinizden emin olun.")
        else:
            # toCsv = (f"Ameliyat Tipi: {ameliyat_tipi}\nAsa skoru: {asa_skoru}\n"
            #          f"Yaş: {yas}\nCinsiyet: {cinsiyet}\nBMI: {bmi}")
            """
            Converting to gender and type to 1 or 0.
            """
            if ameliyat_tipi == "Kapalı":
                ameliyat_tipi = 1
            else:
                ameliyat_tipi = 2
            if cinsiyet == "Kadın":
                cinsiyet = 2
            else:
                cinsiyet = 1
            toCsv = {
                "Morbidite": morbidite_degeri,
                "Ameliyat": ameliyat_tipi,
                "Asa Skoru": asa_skoru,
                "Age": yas,
                "gender": cinsiyet,
                "BMI": bmi
            }
            add_to_csv(toCsv)


# ------------ UI SETUP ----------------- #
window = Tk()
window.title("Delapcare LogReg GUI")
window.minsize(width=600, height=300)
window.config(padx=50, pady=20, bg=GREY)

# ameliyat tipi
ameliyat_tipi_label = Label(text="Ameliyat Tipi: ",
                            bg=GREY, font=("Arial", 12))
ameliyat_tipi_label.grid(row=0, column=0, pady=10, sticky="w")

at_values = ["Kapalı", "Açık"]
at_val_inside = StringVar(window)
at_val_inside.set("Lütfen seçiniz.")
at_entry = OptionMenu(window, at_val_inside, *at_values)
at_entry.grid(column=0, row=1, pady=(0, 40), sticky="nw")

# asa skoru
asa_score_label = Label(text="Asa Skoru: ", bg=GREY, font=("Arial", 12))
asa_score_label.grid(row=0, column=1, sticky="w", pady=10)

as_values = ["   1   ", "   2   ", "   3  "]
as_val_inside = IntVar(window)
as_val_inside.set("Lütfen seçiniz.")
as_menu = OptionMenu(window, as_val_inside, *as_values)
as_menu.grid(column=1, row=1, pady=(0, 40), sticky="nw")

# yaş
yas_label = Label(text="Yaş: ", bg=GREY, font=("Arial", 12))
yas_label.grid(row=0, column=2, pady=10, sticky="w")

yas_entry = Entry(font=("Arial", 10))
yas_entry.grid(column=2, row=1, sticky="nw", pady=(0, 40))

# cinsiyet
gender_label = Label(text="Cinsiyet: ", bg=GREY, font=("Arial", 12))
gender_label.grid(row=0, column=3, pady=10, sticky="w")

gender_values = ["Kadın", "Erkek"]
gender_val_inside = StringVar(window)
gender_val_inside.set("Lütfen seçiniz.")
gender_entry = OptionMenu(window, gender_val_inside, *gender_values)
gender_entry.grid(column=3, row=1, sticky="nw", pady=(0, 40))

# bmi
bmi_label = Label(text="BMI: ", bg=GREY, font=("Arial", 12))
bmi_label.grid(row=0, column=4, pady=10, sticky="w")

bmi_entry = Entry(font=("Arial", 10))
bmi_entry.grid(column=4, row=1, pady=(0, 40), sticky="nw")

# morbidite
morbidite_label = Label(
    text=f"Morbidite: {morbidite_degeri}", bg=GREY, font=("Arial", 12))
morbidite_label.grid(row=3, column=1, sticky="w")

# diğer
warning_note = Label(text="Bu programın tutarlılık oranı %92'dir. Kesin bir sonuca varmadan önce medikal"
                          " profesyonellerden yardım alınız.", font=("Arial", 10), bg=GREY)
warning_note.grid(row=5, column=0, columnspan=4, sticky="w")

submit = Button(text="Hesapla", padx=10, pady=10, font=(
    "Arial", 12), bg=BLUE, command=check_input)
submit.grid(row=3, column=0, sticky="nw", pady=(0, 10))

window.mainloop()
