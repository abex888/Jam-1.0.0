import tkinter as tk
from tkinter import font
import time
import calendar

class TimeHandler:
    def __init__(self):
        self.sundanese_time_names = {
            0: "tengah peuting",
            1: "tumorek",
            2: "Janari Leutik",
            3: "Janari Gede",
            4: "Kongkorongok Hayam",
            5: "Balebat",
            6: "Carangcang Tihang",
            7: "Meletek Panon Poe",
            8: "Ngaluluh Taneuh",
            9: "Haneut Moyan",
            10: "Rumangsang",
            11: "Pecat Sawed",
            12: "Tangage",
            13: "Lingsir",
            14: "Kalangkang Satangtung",
            15: "Mengok",
            16: "Tunggang Gunung",
            17: "Sariak Layung",
            18: "Sareupna",
            19: "Harieum Beungeut",
            20: "Sareureuh Budak",
            21: "Tumoke",
            22: "Sareureuh Kolot",
            23: "Indung Peuting"
        }

        self.sundanese_day_names = {
            0: "Senén",
            1: "Salasa",
            2: "Rebo",
            3: "Kamis",
            4: "Jumat",
            5: "Saptu",
            6: "Minggu"
        }

    def get_current_time(self):
        current_time = time.strftime("%H:%M:%S")
        weekday_index = time.localtime().tm_wday
        weekday_eng = calendar.day_name[weekday_index]
        weekday_sun = self.sundanese_day_names[weekday_index]
        day = time.strftime("%d")
        month = time.strftime("%m")
        year = time.strftime("%Y")
        hour = int(current_time[:2])
        sundanese_time_name = self.sundanese_time_names[hour]

        current_date = f"{weekday_eng}, {day}, {month}, {year}"
        sundanese_date = f"{weekday_sun}, {day}/{month}/{year}"

        return current_time, sundanese_time_name, current_date, sundanese_date

class ClockGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Clock")
        self.root.geometry("300x150")
        self.root.resizable(False, False)

        self.custom_font = font.Font(family="Helvetica", size=48, weight="bold")

        self.time_handler = TimeHandler()

        self.time_label = tk.Label(self.root, font=self.custom_font, text="", fg="black")
        self.time_label.pack()

        self.sundanese_time_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.sundanese_time_label.pack()

        self.sundanese_day_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.sundanese_day_label.pack()

        self.update_time()

    def update_time(self):
        current_time, sundanese_time_name, _, sundanese_date = self.time_handler.get_current_time()
        self.time_label.config(text=current_time)
        self.sundanese_time_label.config(text=f"Kiwari wanci {sundanese_time_name}")
        self.sundanese_day_label.config(text=sundanese_date)
        self.root.after(1000, self.update_time)

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    clock_gui = ClockGUI()
    clock_gui.start()
