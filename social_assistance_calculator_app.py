# importing the necessary libraries for the project:
from tkinter import *
from tkinter import font as tkfont
from tkinter import ttk
import ttkbootstrap as ttk


class SocialAssistanceCalculatorApp:
    # here are the min and max thresholds ass class attributes:
    MIN_THRESHOLD = 710
    MAX_THRESHOLD = 810

    def __init__(self):
        self.window = ttk.Window(themename='cyborg')
        self.window.geometry("500x700")
        self.window.title("Social Assistance Calculator")
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.style = ttk.Style()
        self.font_bold = tkfont.Font(weight='bold')
        self.style.configure('TLabel', font=self.font_bold)
        self.program_name = ttk.Label(
            self.window,
            text="SOCIAL  ASSISTANCE  CALCULATOR",
            foreground='turquoise',
            font=("Cooper Black", 14)
        )
        self.program_name.pack(pady=6)
        # mother income features:
        self.style_1 = ttk.Style()
        self.style_1.configure('TEntry', bd=5)
        self.lbl1 = ttk.Label(
            self.window,
            text="Incomes of the mother:",
            foreground='white',
            font=("Forte", 12),
        )
        self.lbl1.pack(pady=15)
        self.mother_income_entry = ttk.Entry(self.window, width=25)
        self.mother_income_entry.pack()
        # father income features::
        self.style_2 = ttk.Style()
        self.style_2.configure('TEntry', bd=5)
        self.lbl2 = ttk.Label(
            self.window,
            text="Incomes of the father:",
            foreground='white',
            font=("Forte", 12),
        )
        self.lbl2.pack(pady=10)
        self.father_income_entry = ttk.Entry(self.window, width=25)
        self.father_income_entry.pack()
        # extra income features:
        self.style_3 = ttk.Style()
        self.style_3.configure('TEntry', bd=5)
        self.lbl3 = ttk.Label(
            self.window,
            text="Extra income:",
            foreground='white',
            font=("Forte", 12),
        )
        self.lbl3.pack(pady=10)
        self.extra_income_for_the_year = ttk.Entry(self.window, width=25)
        self.extra_income_for_the_year.pack()
        # family members features:
        self.style_4 = ttk.Style()
        self.style_4.configure('TEntry', bd=5)

        self.lbl4 = ttk.Label(
            self.window,
            text="Family members:",
            foreground='white',
            font=("Forte", 12),
        )
        self.lbl4.pack(pady=10)
        self.family_members = ttk.Entry(self.window, width=10)
        self.family_members.pack()
        # result label feature:
        self.result_label = ttk.Label(
            self.window,
            text="",
            font=("Lucida Calligraphy", 10),
            foreground="white",
        )
        self.result_label.place(x=70, y=500)

        self.style_6 = ttk.Style()
        self.style_6.configure(
            'TButton',
            font=("Bauhaus 93", 14),
            relief='flat'
        )
        self.btn = ttk.Button(
            self.window,
            text='Calculate',
            bootstyle='outline',
            command=self.calculation
        )
        self.btn.place(x=197, y=370)
        # info of the creator of the app:
        self.creator_info = Label(
            self.window,
            text="ZSZ Software, Ardino, All Rights Reserved 2024©",
            font=("Verdana", 8),
            fg="white",
        )
        self.creator_info.place(x=110, y=680)
        self.window.resizable(False, False)
        self.window.mainloop()

    def calculation(self):
        # getting user entry as float:
        mothers_income = self.mother_income_entry.get()
        fathers_income = self.father_income_entry.get()
        extra_income = self.extra_income_for_the_year.get()
        family_members_income = self.family_members.get()

        try:
            m = float(mothers_income)
            f = float(fathers_income)
            ex = float(extra_income)
            fm = float(family_members_income)

            # calculating the total income and income per family member:
            total_income = m + f + ex
            income_per_family_member = total_income / 12 / fm
            # have the right to receive social assistance case:
            if income_per_family_member <= self.MIN_THRESHOLD:
                # preparing the result by string formatting:
                res = f"- TOTAL INCOME (for year): {total_income:.2f} BGN\n" \
                      f"- MONTHLY INCOME PER MEMBER: {income_per_family_member:.2f} BGN\n" \
                      f">> You have the right to receive a social assistance\n" \
                      f"      fully!\n" \
                      f">> Your monthly income per member is less than\n" \
                      f"      the minimum {self.MIN_THRESHOLD} BGN."
                # replacing the result label text with the result from the calculation
                # to display it on the program frame
                self.result_label.config(text=res)
            # doesn't have the right to receive social assistance case:
            if income_per_family_member > self.MAX_THRESHOLD:
                res = f"- TOTAL INCOME (for year): {total_income:.2f} BGN\n" \
                      f"- MONTHLY INCOME PER MEMBER: {income_per_family_member:.2f} BGN\n" \
                      f">> You don't have the right to receive a social\n" \
                      f"       assistance!\n" \
                      f">> Your monthly income per member exceeds\n" \
                      f"       the maximum {self.MAX_THRESHOLD} BGN."
                self.result_label.config(text=res)
            # have the right to receive the %80 of the social assistance case:
            if self.MIN_THRESHOLD < income_per_family_member <= self.MAX_THRESHOLD:
                res = f"- TOTAL INCOME (for year): {total_income:.2f} BGN\n" \
                      f"- MONTHLY INCOME PER MEMBER: {income_per_family_member:.2f} BGN\n" \
                      f">> You have the right to receive the %80 of\n" \
                      f"       the social assistance.\n" \
                      f">> Your income per member is between the\n" \
                      f"    minimum {self.MIN_THRESHOLD} BGN and maximum {self.MAX_THRESHOLD} BGN."
                self.result_label.config(text=res)
        except ValueError:
            self.result_label.config(text="<< The entries cannot be empty or zero!!\n"
                                          "   Please fill them correctly\n"
                                          "   and try again. >>")


app = SocialAssistanceCalculatorApp()
