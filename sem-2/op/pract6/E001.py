import tkinter as tk
import tkinter.ttk as ttk
import datetime
import urllib.request
import xml.etree.ElementTree as ET
from tkinter import messagebox
import calendar
import locale
import matplotlib.pyplot as plt
from datetime import timedelta
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib


def convert():
    try:
        name_a = val_a.get()
        name_b = val_b.get()
        mod = float(ent_mod.get())
        kurs_a = 0
        kurs_b = 0
        for i in range(len(Name)):
            if Name[i] == name_a:
                kurs_a = Value[i]
            if Name[i] == name_b:
                kurs_b = Value[i]
            if kurs_a != 0 and kurs_b != 0:
                break
        conv_kurs = round(((1 / kurs_b) * kurs_a) * mod, 10)
        conv_val.configure(text=conv_kurs)
    except:
        messagebox.showwarning("Ошибка", "Выберете валюты и их количество")


def hide_comboboxes():
    comb1.grid_forget()
    comb1.set('')
    comb2.grid_forget()
    comb2.set('')
    comb3.grid_forget()
    comb3.set('')
    comb4.grid_forget()
    comb4.set('')

def show_combobox1():
    hide_comboboxes()
    comb1.grid(column=2, row=2)

def show_combobox2():
    hide_comboboxes()
    comb2.grid(column=2, row=3)

def show_combobox3():
    hide_comboboxes()
    comb3.grid(column=2, row=4)

def show_combobox4():
    hide_comboboxes()
    comb4.grid(column=2, row=5)


def get_currency_rate(currency_code, date):
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"
    with urllib.request.urlopen(url) as url:
        xml = url.read()
    root = ET.fromstring(xml)
    for valute in root.findall("Valute"):
        if valute.find("CharCode").text == currency_code:
            return float(valute.find("Value").text.replace(",", ".")) / float(valute.find("Nominal").text)

def graf_create():
    try:
        for i in range(len(Name)):
            if val_c.get() == Name[i]:
                currency_code = CharCode[i]
        dates = []
        rates = []
        if comb1.get() != "":
            period = comb1.get()
            start_date, end_date = period.split(" - ")
            start_date = datetime.datetime.strptime(start_date, "%d.%m.%Y").date()
            end_date = datetime.datetime.strptime(end_date, "%d.%m.%Y").date()
        elif comb2.get() != "":
            month, year = comb2.get().split(", ")
            month_number = list(calendar.month_name).index(month)
            start_date = datetime.date(int(year), month_number, 1)
            end_date = datetime.date(int(year), month_number, calendar.monthrange(int(year), month_number)[1])
        elif comb3.get() != "":
            quarter, year = comb3.get().split(", год ")
            quarter_number = int(quarter.split()[1])
            start_date = datetime.date(int(year), 3 * (quarter_number - 1) + 1, 1)
            end_date = datetime.date(int(year), 3 * quarter_number, calendar.monthrange(int(year), 3 * quarter_number)[1])
        elif comb4.get() != "":
            year = int(comb4.get())
            start_date = datetime.date(year, 1, 1)
            end_date = datetime.date(year, 12, 31)
        date = start_date
        while date <= end_date:
            rate = get_currency_rate(currency_code, date.strftime("%d/%m/%Y"))
            dates.append(date)
            rates.append(rate)
            print(date)
            if date == datetime.datetime.today().date():
                end_date = datetime.date(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day)
                break
            date += timedelta(days=1)
        matplotlib.use('TkAgg')
        fig = plt.figure(figsize=(11, 4))
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=tab2)
        plot_widget = canvas.get_tk_widget()
        fig.clear()
        plt.plot(dates, rates)
        plt.grid()
        plot_widget.grid(row=7, column=0)
    except:
        messagebox.showwarning("Ошибка", "Выберете валюту и диапазон")



day = str(datetime.datetime.today().day)
month = str(datetime.datetime.today().month)
year = str(datetime.datetime.today().year)
if len(day) == 1:
    day = "0" + day
if len(month) == 1:
    month = "0" + month
url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}"
response = urllib.request.urlopen(url)
xml = response.read()
root = ET.fromstring(xml)
Kurs_date = root.get('Date')
CharCode = ["RU"]
Nominal = ["1"]
Name = ["Российский рубль"]
Value = ["1"]
for valute in root.findall("Valute"):
    CharCode.append(valute.find("CharCode").text)
    Nominal.append(valute.find("Nominal").text)
    Name.append(valute.find("Name").text)
    Value.append(valute.find("Value").text)

for i in range(len(Name)):
    Name[i] = f"({CharCode[i]})" + Name[i]
    if Nominal[i] != 1:
        Value[i] = round(float(Value[i].replace(',', '.'))/float(Nominal[i]), 10)


window = tk.Tk()
window.title("Конвертор/динамика валют")
window.geometry("1350x600+327+225")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Конвертор")
tab_control.add(tab2, text="Динамика")

val_a = ttk.Combobox(tab1, width=60)
val_a["values"] = Name
val_a.set(Name[14])
val_a.grid(column=0, row=3)
val_b = ttk.Combobox(tab1, width=60)
val_b["values"] = Name
val_b.set(Name[0])
val_b.grid(column=0, row=6)


ent_mod = tk.Entry(tab1)
ent_mod.insert(0, "1")
ent_mod.grid(column=10, row=3)
conv = tk.Button(tab1, text="Конвертировать", command=convert)
conv.grid(column=15, row=3)
date_kur = tk.Label(tab1, text=f"Дата курса: {Kurs_date}")
date_kur.grid(column=15, row=0)
conv_val = tk.Label(tab1, text=0)
conv_val.grid(column=10, row=6)

text_a = tk.Label(tab2, text="Валюта")
text_a.grid(column=0, row=0)
val_c = ttk.Combobox(tab2, width=60)
val_c["values"] = Name[1:]
val_c.set(Name[14])
val_c.grid(column=0, row=2)
graf = tk.Button(tab2, text="Построить график", command=graf_create)
graf.grid(column=0, row=5)
text_b = tk.Label(tab2, text="Период")
text_b.grid(column=1, row=0)

var = tk.StringVar()
but_a = tk.Radiobutton(tab2, text="Неделя", variable=var, value="1", command=show_combobox1)
but_a.grid(column=1, row=2)
but_b = tk.Radiobutton(tab2, text="Месяц", variable=var, value="1", command=show_combobox2)
but_b.grid(column=1, row=3)
but_c = tk.Radiobutton(tab2, text="Квартал", variable=var, value="1", command=show_combobox3)
but_c.grid(column=1, row=4)
but_d = tk.Radiobutton(tab2, text="Год", variable=var, value="1", command=show_combobox4)
but_d.grid(column=1, row=5)

today = datetime.datetime.today().date()
week_ago = today - datetime.timedelta(days=7)
tw_weeks_ago = week_ago - datetime.timedelta(days=7)
th_weeks_ago = tw_weeks_ago - datetime.timedelta(days=7)
f_weeks_ago = th_weeks_ago - datetime.timedelta(days=7)
today_str = today.strftime("%d.%m.%Y")
week_ago_str = week_ago.strftime("%d.%m.%Y")
tw_week_ago_str = tw_weeks_ago.strftime("%d.%m.%Y")
th_week_ago_str = th_weeks_ago.strftime("%d.%m.%Y")
f_week_ago_str = f_weeks_ago.strftime("%d.%m.%Y")
comb1_val = [f"{week_ago_str} - {today_str}", f"{tw_week_ago_str} - {week_ago_str}", f"{th_week_ago_str} - {tw_week_ago_str}",
             f"{f_week_ago_str} - {th_week_ago_str}"]
comb1 = ttk.Combobox(tab2, state="readonly", values=comb1_val)

locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
calendar.different_locale('ru_RU.utf8')
today = datetime.datetime.today()
comb2_val = []
for i in range(4):
    year = today.year if i == 0 else today.year if today.month > 1 else today.year - 1
    month = today.month - i if today.month > i else today.month - i + 12
    month_name = calendar.month_name[month]
    comb2_val.append(f"{month_name}, {year}")
comb2 = ttk.Combobox(tab2, state="readonly", values=comb2_val)


comb3_val = []
for i in range(4):
    quarter = f"Квартал {(today.month-1)//3 + 1}, год {today.year}"
    comb3_val.append(quarter)
    today -= datetime.timedelta(days=90)
comb3 = ttk.Combobox(tab2, state="readonly", values=comb3_val)

comb4_val = [year, int(year)-1, int(year)-2, int(year)-3]
comb4 = ttk.Combobox(tab2, state="readonly", values=comb4_val)


tab_control.pack(expand=3, fill='both')
window.mainloop()