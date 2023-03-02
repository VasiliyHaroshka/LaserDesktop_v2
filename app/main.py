import tkinter as tk
from math import cos, pi, sqrt, radians


# Формулы
# **********************************Верификация входных данных**********************************
def common_verify(value, entry) -> bool:
    """Общая верификафия"""
    try:
        float(value)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, f"ОШИБКА!!! Вводить можно только цифры и точку")
        crash()
        return False
    else:
        return True


def lambda_verify() -> bool:
    """Верификафия длины волны"""
    length_of_wave = laser_lambda.get()
    common_verify(length_of_wave, laser_lambda)
    if float(length_of_wave) < 0.405 or float(length_of_wave) > 100:
        laser_lambda.delete(0, tk.END)
        laser_lambda.insert(0, f"ОШИБКА!!! Длина волны в диапазоне 0.405 - 100 мкм")
        return False
    return True


def time_verify() -> bool:
    """Верификафия времени работы"""
    work_time = laser_t.get()
    common_verify(work_time, laser_t)
    if int(work_time) <= 0:
        laser_t.delete(0, tk.END)
        laser_t.insert(0, f"ОШИБКА!!! Время работы не может быть 0 или меньше")
        return False
    return True


def diameter_verify() -> bool:
    """Верификафия диаметра пятна"""
    diameter_of_spot = laser_d.get()
    common_verify(diameter_of_spot, laser_d)
    if float(diameter_of_spot) <= 0:
        laser_d.delete(0, tk.END)
        laser_d.insert(0, f"ОШИБКА!!! Диаметр пятна не может быть 0 или меньше")
        return False
    return True


def impulse_duration_verify() -> bool:
    """Верификафия длительности импульса"""
    impulse_duration = laser_tay.get()
    common_verify(impulse_duration, laser_tay)
    if float(impulse_duration) <= 0:
        laser_tay.delete(0, tk.END)
        laser_tay.insert(0, f"ОШИБКА!!! Длительность импульса не может быть 0 или меньше")
        return False
    return True


def frequency_verify() -> bool:
    """Верификафия частоты"""
    frequency = laser_f.get()
    common_verify(frequency, laser_f)
    if float(frequency) <= 0:
        laser_f.delete(0, tk.END)
        laser_f.insert(0, f"ОШИБКА!!! Частота не может быть 0 или меньше")
        return False
    return True


def long_wave_verify() -> bool:
    length_of_wave = laser_lambda.get()
    if float(length_of_wave) < 1.4:
        laser_lambda.delete(0, tk.END)
        laser_lambda.insert(0, "ОШИБКА!!! ПЕРЕКЛЮЧИТЕ УКАЗАТЕЛЬ БОЛЕЕ 1,4 мкм")
        crash()
        return False
    return True


# **********************************Очистка полей**********************************
def clear_all() -> None:
    """Очистить все поля ввода"""
    laser_lambda.delete(0, tk.END)
    laser_t.delete(0, tk.END)
    laser_d.delete(0, tk.END)
    laser_tay.delete(0, tk.END)
    laser_f.delete(0, tk.END)
    skin.delete(0, tk.END)
    eyes.delete(0, tk.END)


# **********************************Error**********************************
def crash() -> None:
    """Заполняет поля ПДУ для глаз и кожи сообщением о ошибке"""
    skin.delete(0, tk.END)
    eyes.delete(0, tk.END)
    skin.insert(0, "Невозможно рассчитать ПДУ для кожи!!!")
    eyes.insert(0, "Невозможно рассчитать ПДУ для глаз!!!")


# ********************************** Вычисление специальных коэффициентов **********************************


def S0_calculation() -> float | int:
    """Вычисление коэффициента S0"""
    diameter_of_spot = float(laser_d.get())
    print(f" S0 = {pi * diameter_of_spot ** 2 / 4}")
    return pi * diameter_of_spot ** 2 / 4


def alpha_calculation(angel=45) -> float | int:
    """Вычисление предельного угла (alpha) для 45 градусав по умолчанию"""
    alpha = 0.04 * sqrt(S0_calculation() * cos(radians(angel)) / pi)
    print(f"alpha = {alpha}")
    return alpha


def w_calculation(f: int | float, t: int | float) -> float | int:
    print(f"w = {f * t + 1}")
    return f * t + 1


# ********************************** Таблицы **********************************

def table_3(len_w, tay) -> float:
    """ТАБЛИЦА 3"""
    if 0.38 < len_w <= 0.6:
        if tay <= 2.3e-11:
            return (tay ** 2) ** (1 / 3)
        elif 2.3e-11 < tay <= 5e-5:
            return 8e-8
        elif 5e-5 < tay <= 1:
            return 5.9e-5 * ((tay ** 2) ** (1 / 3))

    elif 0.6 < len_w <= 0.75:
        if tay <= 6.5e-11:
            return (tay ** 2) ** (1 / 3)
        elif 6.5e-11 < tay <= 5e-5:
            return 1.6e-7
        elif 5e-5 < tay <= 1:
            return 1.2e-4 * ((tay ** 2) ** (1 / 3))

    elif 0.75 < len_w <= 1:
        if tay <= 2.5e-10:
            return (tay ** 2) ** (1 / 3)
        elif 2.5e-11 < tay <= 5e-5:
            return 4e-7
        elif 5e-5 < tay <= 1:
            return 3e-4 * ((tay ** 2) ** (1 / 3))

    elif 1 < len_w <= 1.4:
        if tay <= 1e-9:
            return (tay ** 2) ** (1 / 3)
        elif 1e-9 < tay <= 5e-5:
            return 1e-6
        elif 5e-5 < tay <= 1:
            return 7.4e-4 * ((tay ** 2) ** (1 / 3))

    else:
        crash()


def table_4(len_w: float, t: float) -> float:
    """ТАБЛИЦА 4"""
    if 0.38 < len_w <= 0.5:
        if 1 < t <= 500:
            return 6.9e-5 / t ** (1 / 3)
        elif 500 < t <= 1e4:
            return 3.7e-3 / t
        elif t > 1e4:
            return 3.7e-7

    elif 0.5 < len_w <= 0.6:
        if 1 < t <= 2.2e3:
            return 5.9e-5 / t ** (1 / 3)
        elif 2.2e3 < t <= 1e4:
            return 0.01 / t
        elif t > 1e4:
            return 1e-6

    elif 0.6 < len_w <= 0.7:
        if 1 < t <= 2.2e3:
            return 1.2e-4 / t ** (1 / 3)
        elif 2.2e3 < t <= 1e4:
            return 2e-2 / t
        elif t > 1e4:
            return 2e-6

    elif 0.7 < len_w <= 0.75:
        if 1 < t <= 1e4:
            return 1.2e-4 / t ** (1 / 3)
        elif t > 1e4:
            return 5.5e-6

    elif 0.75 < len_w <= 1:
        if 1 < t <= 1e4:
            return 3e-4 / t ** (1 / 3)
        elif t > 1e4:
            return 1.4e-5

    elif 1 < len_w <= 1.4:
        if 1 < t <= 1e4:
            return 7.4e-4 / t ** (1 / 3)
        elif t > 1e4:
            return 3.5e-5
    else:
        crash()


def table_5(t: float | int, alpha: float) -> float | int:
    """ТАБЛИЦА 5"""
    if t <= 1e-9:
        alpha_pred = 1e-2
    elif 1e-9 < t <= 1e-7:
        alpha_pred = 6e-3
    elif 1e-7 < t <= 1e-5:
        alpha_pred = 3.5e-3
    elif 1e-5 < t <= 1e-4:
        alpha_pred = 2e-3
    elif 1e-4 < t <= 1e-2:
        alpha_pred = 3.5e-3
    elif 1e-2 < t <= 1:
        alpha_pred = 6e-3
    elif t > 1:
        alpha_pred = 1e-2
    else:
        alpha_pred = 0
        print("!!!Ошибка в табл 5!!!")
        crash()

    if alpha > alpha_pred:
        if t <= 1e-9:
            return 1e3 * alpha ** 2 + 1
        elif 1e-9 < t <= 1e-7:
            return 2.8e3 * alpha ** 2 + 1
        elif 1e-7 < t <= 1e-5:
            return 8.2e3 * alpha ** 2 + 1
        elif 1e-5 < t <= 1e-4:
            return 2.5e3 * alpha ** 2 + 1
        elif 1e-4 < t <= 1e-2:
            return 8.2e3 * alpha ** 2 + 1
        elif 1e-2 < t <= 1:
            return 2.8e3 * alpha ** 2 + 1
        elif t > 1:
            return 1e3 * alpha ** 2 + 1
    else:
        return 1


def table_6(len_w: float, t: float) -> float | int:
    """ТАБЛИЦА 6"""
    if 0.38 < len_w <= 0.5:
        if 1e-10 < t <= 0.1:
            return 2.5e3 * t ** (1 / 5)
        elif 0.1 < t <= 1:
            return 5e3 * t ** (1 / 2)
        elif 1 < t <= 100:
            return 5e3 / t ** (1 / 2)
        elif t > 100:
            return 5e2
    elif 0.5 < len_w <= 0.9:
        if 1e-10 < t <= 3:
            return 7e3 * t ** (1 / 5)
        elif 3 < t <= 100:
            return 5e3 / t ** (1 / 2)
        elif t > 100:
            return 5e2
    elif 0.9 < len_w <= 1.4:
        if 1e-10 < t <= 1:
            return 2e4 * t ** (1 / 5)
        elif 1 < t <= 100:
            return 2e4 / (t ** 4) ** (1 / 5)
        elif t > 100:
            return 5e2

    if 1.4 < len_w <= 1.8:
        if 1e-10 < t <= 1:
            return 2e4 * t ** (1 / 5)
        elif 1 < t <= 100:
            return 2e4 / (t ** 4) ** (1 / 5)
        elif t > 100:
            return 5e2

    elif 1.8 < len_w <= 2.5:
        if 1e-10 < t <= 3:
            return 7e3 * t ** (1 / 5)
        elif 3 < t <= 100:
            return 5e3 / t ** (1 / 2)
        elif t > 100:
            return 5e2

    elif 2.5 < len_w <= 1e5:
        if 1e-10 < t <= 0.1:
            return 2.5e3 * t ** (1 / 5)
        elif 0.1 < t <= 1:
            return 5e3 / t ** (1 / 2)
        elif 1 < t <= 100:
            return 5e3 / t ** (1 / 2)
        elif t > 100:
            return 5e2
    else:
        crash()


# ********************************** НЕПРЕРЫВНЫЙ **********************************

# ********************************** Кожа

def continuous_calculation_skin() -> None:
    """Расчитывает ПДУ для кожи непрерывного лазера и заполняет виджет ответа ПДУ для кожи"""
    length_of_wave = float(laser_lambda.get())
    work_time = float(laser_t.get())
    pdu_skin: float = table_6(length_of_wave, work_time) / 10 * 1e-4 * work_time
    print(f"ПДУ для кожи непр лазера = {pdu_skin}")
    skin.insert(0, str(pdu_skin))


# ********************************** Глаза

def continuous_calculation_eyes() -> None:
    """Расчитывает ПДУ для глаз непрерывного лазера и заполняет виджет ответа ПДУ для глаз"""
    length_of_wave = float(laser_lambda.get())
    work_time = float(laser_t.get())
    pdu_eyes: float = table_4(length_of_wave, work_time) / 10 * table_5(work_time,
                                                                        alpha_calculation()) / 0.4 * work_time
    print(f"B для непр {table_5(work_time, alpha_calculation())}")
    print(f"ПДУ для глаз непр лазера = {pdu_eyes}")
    eyes.insert(0, str(pdu_eyes))


# ********************************** ИМПУЛЬСНЫЙ **********************************

# ********************************** Кожа


def serial_impulse_skin() -> float:
    """Расчет ПДУ для кожи имп лазера для серии импульсов"""
    length_of_wave = float(laser_lambda.get())
    work_time = float(laser_t.get())
    h1 = table_6(length_of_wave, work_time) / 10 * 1e-4 * work_time
    print(f"H1 = {h1}")
    return h1


def single_impulse_skin() -> float:
    """Расчет ПДУ для кожи имп лазера для одиночного импульса"""
    length_of_wave = float(laser_lambda.get())
    impulse_duration = float(laser_tay.get())
    frequency = float(laser_f.get())
    work_time = float(laser_t.get())
    h2: float = table_6(length_of_wave, impulse_duration) * 1e-4 * sqrt(w_calculation(frequency, work_time))
    print(f"H2 = {h2}")
    return h2


def impulse_calculation_skin() -> None:
    """Сравнивает ПДУ имп лазера для серии импульсов и одиночного импульса и выбирает наимельший
    Заполняет ПДУ для коди импульсного лазера"""
    print(f"ПДУ для кожи имп лазера = {min(serial_impulse_skin(), single_impulse_skin())}")
    skin.insert(0, str(min(serial_impulse_skin(), single_impulse_skin())))


# ********************************** Глаза

def serial_impulse_eyes() -> float:
    """Расчет ПДУ для глаз имп лазера для серии импульсов"""
    length_of_wave = float(laser_lambda.get())
    work_time = float(laser_t.get())
    impulse_duration = float(laser_tay.get())
    w1: float = table_4(length_of_wave, work_time) / 10 * work_time
    print(f"B для имп серии = {table_5(work_time, alpha_calculation())}")
    if table_5(work_time, alpha_calculation()) != 1:
        w1 *= impulse_duration
    print(f"w1 = {w1}")
    return w1


def single_impulse_eyes() -> float:
    """Расчет ПДУ для глаз имп лазера для одиночного импульса"""
    length_of_wave = float(laser_lambda.get())
    impulse_duration = float(laser_tay.get())
    frequency = float(laser_f.get())
    work_time = float(laser_t.get())
    w2: float = table_3(length_of_wave, impulse_duration)
    print(f"B для имп одиноч {table_5(impulse_duration, alpha_calculation())}")
    if table_5(impulse_duration, alpha_calculation()) != 1:
        w2 *= impulse_duration
    print(f"W2 = {w2 * w_calculation(frequency, work_time) ** (2 / 3)}")
    return w2 * w_calculation(frequency, work_time) ** (2 / 3)


def impulse_calculation_eyes():
    """Сравнивает ПДУ имп лазера для серии импульсов и одиночного импульса и выбирает наимельший и делит его на 0.4.
       Заполняет ПДУ для глаз импульсного лазера"""
    eyes.insert(0, str(min(serial_impulse_eyes(), single_impulse_eyes()) / 0.4))


# ********************************** МОНОИМПУЛЬСНЫЙ **********************************

# ********************************** Кожа
def monoimpulse_skin() -> None:
    """Расчет ПДУ для кожи моноимп лазера и заполнение виджета ПДУ для кожи"""
    length_of_wave = float(laser_lambda.get())
    impulse_duration = float(laser_tay.get())
    pdu_skin: float = table_6(length_of_wave, impulse_duration) / 10 * 1e-4
    print(f"ПДУ для кожи моноимп = {pdu_skin}")
    skin.insert(0, str(pdu_skin))


# ********************************** Глаза

def monoimpulse_eyes() -> None:
    """Расчет ПДУ для глаз моноимп лазера и заполнение виджета ПДУ для глаз"""
    length_of_wave = float(laser_lambda.get())
    impulse_duration = float(laser_tay.get())
    pdu_eyes: float = table_3(length_of_wave, impulse_duration)
    print(f"B для глаз моноимп = {table_5(impulse_duration, alpha_calculation())}")
    if table_5(impulse_duration, alpha_calculation()) != 1:
        pdu_eyes *= impulse_duration
    print(f"ПДУ для глаз моноимп = {pdu_eyes / 0.4}")
    eyes.insert(0, str(pdu_eyes / 0.4))


# ********************************** БОЛЕЕ 1,4 НЕПРЕРЫВНЫЙ **********************************

def long_wave_continuous_calculation() -> None:
    """Расчитывает ПДУ для глаз и кожи непрерывного лазера большой длины волны и заполняет виджеты ответа ПДУ"""
    length_of_wave = float(laser_lambda.get())
    work_time = float(laser_t.get())
    pdu: float = table_6(length_of_wave, work_time) / 5 * 1e-4 * work_time
    print(f"ПДУ для глаз и кожи непр лазера большой длины волны = {pdu}")
    skin.insert(0, str(pdu))
    eyes.insert(0, str(pdu))


# ********************************** БОЛЕЕ 1,4 ИМПУЛЬСНЫЙ **********************************
def long_wave_serial_impulse():
    """Расчет ПДУ имп лазера большой длины для серии импульсов"""
    length_of_wave = float(laser_lambda.get())
    work_time = float(laser_t.get())
    h1: float = table_6(length_of_wave, work_time) / 5 * 1e-4 * work_time
    print(f"H1 для глаз и кожи непр лазера большой длины волны = {h1}")
    return h1


def long_wave_single_impulse():
    """Расчет ПДУ имп лазера большой длины для одиночного импульса"""
    length_of_wave = float(laser_lambda.get())
    impulse_duration = float(laser_tay.get())
    frequency = float(laser_f.get())
    work_time = float(laser_t.get())
    h2: float = table_6(length_of_wave, impulse_duration) / 5 * 1e-4 * sqrt(w_calculation(frequency, work_time))
    print(f"H2 для глаз и кожи непр лазера большой длины волны = {h2}")
    return h2


def long_wave_impulse_calculation():
    """Расчитывает ПДУ для глаз и кожи непрерывного лазера большой длины волны и заполняет виджеты ответа ПДУ"""
    skin.insert(0, str(min(long_wave_serial_impulse(), long_wave_single_impulse())))
    eyes.insert(0, str(min(long_wave_serial_impulse(), long_wave_single_impulse())))


# ********************************** БОЛЕЕ 1,4 МОНОИМПУЛЬСНЫЙ **********************************

def long_wave_monoimpulse_calculation() -> None:
    length_of_wave = float(laser_lambda.get())
    impulse_duration = float(laser_tay.get())
    pdu: float = table_6(length_of_wave, impulse_duration) / 5 * 1e-4
    print(f"ПДУ для кожи и глаз мноимп лазера большой длины волны = {pdu}")
    skin.insert(0, str(pdu))
    eyes.insert(0, str(pdu))


# ********************************** MAIN **********************************
def go():
    skin.delete(0, tk.END)
    eyes.delete(0, tk.END)
    work_mode: int = mode.get()
    long_wave_laser: bool = is_long_lambda.get()
    if work_mode == 1 and not long_wave_laser:
        if all([lambda_verify(), time_verify(), diameter_verify()]):
            continuous_calculation_skin()
            continuous_calculation_eyes()
        else:
            crash()
    elif work_mode == 2 and not long_wave_laser:
        if all([lambda_verify(), time_verify(), diameter_verify(), impulse_duration_verify(), frequency_verify()]):
            impulse_calculation_skin()
            impulse_calculation_eyes()
        else:
            crash()
    elif work_mode == 3 and not long_wave_laser:
        if all([lambda_verify(), diameter_verify(), impulse_duration_verify()]):
            monoimpulse_skin()
            monoimpulse_eyes()
        else:
            crash()
    elif work_mode == 1 and long_wave_laser:
        if all([lambda_verify(), time_verify(), diameter_verify(), long_wave_verify()]):
            long_wave_continuous_calculation()
        else:
            crash()
    elif work_mode == 2 and long_wave_laser:
        if all([lambda_verify(), time_verify(), diameter_verify(), impulse_duration_verify(), frequency_verify(),
                long_wave_verify()]):
            long_wave_impulse_calculation()
        else:
            crash()
    elif work_mode == 3 and long_wave_laser:
        if all([lambda_verify(), diameter_verify(), impulse_duration_verify(), long_wave_verify()]):
            long_wave_monoimpulse_calculation()
        else:
            crash()


# Функции выбора режима работы
def constant():
    clear_all()
    laser_tay.insert(0, "---")
    laser_f.insert(0, "---")


def impulse():
    clear_all()


def monoimpulse():
    clear_all()
    laser_t.insert(0, "---")
    laser_f.insert(0, "---")


# Окно
win = tk.Tk()
win.geometry("900x700+400+70")
win.resizable(False, False)
win.title("Laser Desktop")

image = tk.PhotoImage(file='icon.png')
win.iconphoto(False, image)

tk.Label(win, text="Программа для расчета ПДУ отраженного лазерного излучения",
         font=("Times New Roman", 16, 'bold'),
         justify=tk.CENTER,
         padx=55) \
    .grid(row=0, column=0, columnspan=2, sticky="we")

win.grid_rowconfigure(0, minsize=70)

# Выбор режима работы
mode = tk.IntVar()
is_long_lambda = tk.BooleanVar()

working_mode = tk.Label(win,
                        text="Выберите режим работы лазера:",
                        font=("Times New Roman", 15),
                        justify=tk.CENTER,
                        padx=50,
                        )
working_mode.grid(row=2, column=0, sticky="w")

working_mode = tk.Label(win,
                        text="Длина волны лазера более 1,4 мкм:",
                        font=("Times New Roman", 15),
                        justify=tk.CENTER,
                        padx=50,
                        )
working_mode.grid(row=2, column=1, sticky="w")

# RadioButtons
tk.Radiobutton(win, text="Непрерывный", variable=mode, command=constant, value=1).grid(row=3, column=0)
tk.Radiobutton(win, text="Импульсный", variable=mode, command=impulse, value=2).grid(row=4, column=0)
tk.Radiobutton(win, text="Моноимпульсный", variable=mode, command=monoimpulse, value=3).grid(row=5, column=0)

tk.Radiobutton(win, text="Да", variable=is_long_lambda, value=True).grid(row=3, column=1)
tk.Radiobutton(win, text="Нет", variable=is_long_lambda, value=False).grid(row=4, column=1)

# Поля ввода
# Длина волны
tk.Label(win,
         text="Введите длину волны (в мкм):",
         font=("Times New Roman", 15),
         justify=tk.CENTER,
         height=2,
         padx=50,
         anchor="s"
         ). \
    grid(row=6, column=0, sticky="w")

laser_lambda = tk.Entry(win)
laser_lambda.grid(row=7, column=0, sticky="wen", padx=50)

# Время работы
tk.Label(win,
         text="Введите время работы (в сек):",
         font=("Times New Roman", 15),
         justify=tk.CENTER,
         height=2,
         padx=50,
         anchor="s"). \
    grid(row=8, column=0, sticky="w")

laser_t = tk.Entry(win)
laser_t.grid(row=9, column=0, sticky="wen", padx=50)

# Диаметр пятна
tk.Label(win,
         text="Введите диаметр пятна (в см):",
         font=("Times New Roman", 15),
         justify=tk.CENTER,
         height=2,
         padx=50,
         anchor="s"). \
    grid(row=10, column=0, sticky="w")

laser_d = tk.Entry(win)
laser_d.grid(row=11, column=0, sticky="wen", padx=50)

# Длительность импульса
tk.Label(win,
         text="Введите длительность импулься (в сек):",
         font=("Times New Roman", 15),
         justify=tk.CENTER,
         height=2,
         padx=50,
         anchor="s"). \
    grid(row=12, column=0, sticky="w")

laser_tay = tk.Entry(win)
laser_tay.grid(row=13, column=0, sticky="wen", padx=50)

# Частота
tk.Label(win,
         text="Введите частоту (в Гц):",
         font=("Times New Roman", 15),
         justify=tk.CENTER,
         height=2,
         padx=50,
         anchor="s"). \
    grid(row=14, column=0, sticky="w")

laser_f = tk.Entry(win)
laser_f.grid(row=15, column=0, sticky="wen", padx=50)

# Кнопки внизу
start = tk.Button(win, text="Расчитать", command=go, width=15, bg="#00FF00")
start.grid(row=16, column=0, pady=20, padx=50, sticky="w")

reset = tk.Button(win, text="Сброс", command=clear_all, width=15, bg="red")
reset.grid(row=16, column=0, padx=50, sticky="e")

# Поля вывода
tk.Label(win,
         text="ПДУ для кожи (Дж/см2):",
         font=("Times New Roman", 15),
         justify=tk.CENTER,
         height=2,
         padx=50,
         anchor="s"). \
    grid(row=8, column=1, sticky="w")

skin = tk.Entry(win)
skin.grid(row=9, column=1, sticky="wen", padx=50)

tk.Label(win,
         text="ПДУ для глаз (Дж/см2):",
         font=("Times New Roman", 15),
         justify=tk.CENTER,
         height=2,
         padx=50,
         anchor="s"). \
    grid(row=10, column=1, sticky="w")

eyes = tk.Entry(win)
eyes.grid(row=11, column=1, sticky="wen", padx=50)

win.mainloop()
