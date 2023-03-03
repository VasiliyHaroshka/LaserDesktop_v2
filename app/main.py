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
    if float(length_of_wave) < 0.38 or float(length_of_wave) > 100:
        laser_lambda.delete(0, tk.END)
        laser_lambda.insert(0, f"ОШИБКА!!! Длина волны в диапазоне 0.38 - 100 мкм")
        return False
    return True


def time_verify() -> bool:
    """Верификафия времени работы"""
    work_time = laser_time.get()
    common_verify(work_time, laser_time)
    if int(work_time) <= 0:
        laser_time.delete(0, tk.END)
        laser_time.insert(0, "ОШИБКА!!! Время работы не может быть 0 или меньше")
        return False
    return True


def diameter_verify() -> bool:
    """Верификафия диаметра пятна"""
    diameter_of_spot = laser_diameter.get()
    common_verify(diameter_of_spot, laser_diameter)
    if float(diameter_of_spot) <= 0:
        laser_diameter.delete(0, tk.END)
        laser_diameter.insert(0, "ОШИБКА!!! Диаметр пятна не может быть 0 или меньше")
        return False
    return True


def impulse_duration_verify() -> bool:
    """Верификафия длительности импульса"""
    impulse_duration = laser_tay.get()
    common_verify(impulse_duration, laser_tay)
    if float(impulse_duration) <= 0:
        laser_tay.delete(0, tk.END)
        laser_tay.insert(0, "ОШИБКА!!! Длительность импульса не может быть 0 или меньше")
        return False
    return True


def frequency_verify() -> bool:
    """Верификафия частоты"""
    frequency = laser_f.get()
    common_verify(frequency, laser_f)
    if float(frequency) <= 0:
        laser_f.delete(0, tk.END)
        laser_f.insert(0, "ОШИБКА!!! Частота не может быть 0 или меньше")
        return False
    return True


def angel_verify() -> bool:
    """Верификафия угла наблюдения"""
    angel = viewing_angel.get()
    common_verify(angel, viewing_angel)
    if 0 >= float(angel) > 180:
        viewing_angel.delete(0, tk.END)
        viewing_angel.insert(0, "ОШИБКА!!! Угол наблюдения должен быть в диапазоне от 0 до 180 градусов")
        return False
    return True


def distance_verify() -> bool:
    """Верификафия расстояния отисточника"""
    distance = laser_distance.get()
    common_verify(distance, laser_distance)
    if float(distance) <= 0:
        laser_distance.delete(0, tk.END)
        laser_distance.insert(0, "ОШИБКА!!! Расстояние от источника дожно быть более 0")
        return False
    return True


# **********************************Очистка полей**********************************
def clear_all() -> None:
    """Очистить все поля ввода"""
    laser_lambda.delete(0, tk.END)
    laser_time.delete(0, tk.END)
    laser_diameter.delete(0, tk.END)
    laser_tay.delete(0, tk.END)
    laser_f.delete(0, tk.END)
    # viewing_angel.delete(0, tk.END)
    # laser_distance.delete(0, tk.END)
    measure_laser_value.delete(0, tk.END)
    measure_skin.delete(0, tk.END)
    measure_eyes.delete(0, tk.END)


# **********************************Error**********************************
def crash() -> None:
    """Заполняет поля результатов расчета сообщением о ошибке"""
    skin.delete(0, tk.END)
    eyes.delete(0, tk.END)
    measure_skin.delete(0, tk.END)
    measure_eyes.delete(0, tk.END)
    skin.insert(0, "Невозможно рассчитать ПДУ для кожи!!!")
    eyes.insert(0, "Невозможно рассчитать ПДУ для глаз!!!")
    measure_skin.insert(0, "---")
    measure_eyes.insert(0, "---")


# ********************************** Вычисление специальных коэффициентов **********************************

def alpha_calculation(diam: int | float, ang: int | float, dist: int | float) -> float | int:
    """Вычисление предельного угла (alpha)"""
    print(f"1 слогаемое = {diam / 100 / dist}")
    print(f"2 слогаемое = {sqrt(cos(radians(ang)))}")
    alpha = diam / 100 / dist * sqrt(cos(radians(ang)))
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


def table_7(len_w: float, t: float) -> float | int:
    """ТАБЛИЦА 7"""
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


# ********************************** НЕПРЕРЫВНЫЙ 2 СПЕКТРАЛЬНЫЙ ДИАПАЗОН **********************************

# ********************************** Кожа

def continuous_calculation_skin() -> None:
    """Расчитывает ПДУ для кожи непрерывного лазера и заполняет виджет ответа ПДУ для кожи"""
    length_of_wave = float(laser_lambda.get())
    work_time = float(laser_time.get())
    pdu_skin: float = table_6(length_of_wave, work_time) / 10
    print(f"ПДУ для кожи непр лазера = {pdu_skin}")
    skin.insert(0, str(pdu_skin))


# ********************************** Глаза

def continuous_calculation_eyes() -> None:
    """Расчитывает ПДУ для глаз непрерывного лазера и заполняет виджет ответа ПДУ для глаз"""
    length_of_wave = float(laser_lambda.get())
    work_time = float(laser_time.get())
    diameter_spot = float(laser_diameter.get())
    angel = float(viewing_angel.get()) / 100
    distance = float(laser_distance.get())
    b = table_5(work_time, alpha_calculation(diameter_spot, angel, distance))
    pdu_eyes: float = table_4(length_of_wave, work_time) / 10 * b
    print(f"Коэф B = {b}")
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


# ********************************** MAIN **********************************
def go():
    skin.delete(0, tk.END)
    eyes.delete(0, tk.END)
    measure_skin.delete(0, tk.END)
    measure_skin.delete(0, tk.END)
    work_mode: int = mode.get()
    specter_values: int = sp_range.get()
    if work_mode == 1 and specter_values == 2:
        if all([lambda_verify(), time_verify(), diameter_verify()]):
            continuous_calculation_skin()
            continuous_calculation_eyes()
        else:
            crash()
    # elif work_mode == 2 and not long_wave_laser:
    #     if all([lambda_verify(), time_verify(), diameter_verify(), impulse_duration_verify(), frequency_verify()]):
    #         impulse_calculation_skin()
    #         impulse_calculation_eyes()
    #     else:
    #         crash()
    # elif work_mode == 1 and long_wave_laser:
    #     if all([lambda_verify(), time_verify(), diameter_verify(), long_wave_verify()]):
    #         long_wave_continuous_calculation()
    #     else:
    #         crash()
    # elif work_mode == 2 and long_wave_laser:
    #     if all([lambda_verify(), time_verify(), diameter_verify(), impulse_duration_verify(), frequency_verify(),
    #             long_wave_verify()]):
    #         long_wave_impulse_calculation()
    #     else:
    #         crash()


# Функции выбора режима работы
def constant():
    clear_all()
    laser_tay.insert(0, "---")
    laser_f.insert(0, "---")


def impulse():
    clear_all()


# ОКНО
win = tk.Tk()
win.geometry("1200x600+170+20")
# win.attributes("-fullscreen", True)
win.resizable(False, False)
win.title("Laser Desktop_v2")

image = tk.PhotoImage(file='laser.png')
win.iconphoto(False, image)

tk.Label(win,
         text="Программа для расчета ПДУ отраженного лазерного излучения",
         font=("Times New Roman", 17, "bold"),
         height=3,
         ).grid(row=0, column=0, sticky="we", columnspan=4)

# ********************************** ЛЕВОЕ МЕНЮ **********************************
# Измеренные значнения
measure_values = tk.Label(win,
                          text="Введите измеренные значания:",
                          font=("Times New Roman", 16, "bold"),
                          )
measure_values.grid(row=1, column=0, sticky="we", columnspan=2)

tk.Label(win,
         text="- фоновое значение:",
         font=("Times New Roman", 15),
         ).grid(row=2, column=0, sticky="we")

background_laser_value = tk.Entry(win)
background_laser_value.grid(row=2, column=1, sticky="we")
background_laser_value.insert(0, "0")

tk.Label(win,
         text="- измеренное значение:",
         font=("Times New Roman", 15),
         ).grid(row=3, column=0, sticky="we")

measure_laser_value = tk.Entry(win)
measure_laser_value.grid(row=3, column=1, sticky="we")

# Параметры лазера
laser_values = tk.Label(win,
                        text="Введите параметры лазера:",
                        font=("Times New Roman", 16, "bold"),
                        )
laser_values.grid(row=5, column=0, sticky="we", columnspan=2)

# Длина волны
tk.Label(win,
         text="- длина волны (мкм):",
         font=("Times New Roman", 15),
         ).grid(row=6, column=0, sticky="we")

laser_lambda = tk.Entry(win, font=("Times New Roman", 15))
laser_lambda.grid(row=6, column=1, sticky="we")
#
# # Время работы
tk.Label(win,
         text="- время работы (сек):",
         font=("Times New Roman", 15),
         ).grid(row=7, column=0, sticky="we")

laser_time = tk.Entry(win, font=("Times New Roman", 15))
laser_time.grid(row=7, column=1, sticky="we")

# Диаметр пятна
tk.Label(win,
         text="- диаметр пятна (см):",
         font=("Times New Roman", 15),
         ).grid(row=8, column=0, sticky="we")

laser_diameter = tk.Entry(win, font=("Times New Roman", 15))
laser_diameter.grid(row=8, column=1, sticky="we")

# Длительность импульса
tk.Label(win,
         text="- длительность импулься (сек):",
         font=("Times New Roman", 15),
         ).grid(row=9, column=0, sticky="we")

laser_tay = tk.Entry(win, font=("Times New Roman", 15))
laser_tay.grid(row=9, column=1, sticky="we")

# Частота
tk.Label(win,
         text="- частота (Гц):",
         font=("Times New Roman", 15),
         ).grid(row=10, column=0, sticky="we")

laser_f = tk.Entry(win, font=("Times New Roman", 15))
laser_f.grid(row=10, column=1, sticky="we")

# Угол наблюдения
tk.Label(win,
         text="- угол наблюдения (градусы):",
         font=("Times New Roman", 15),
         ).grid(row=11, column=0, sticky="we")

viewing_angel = tk.Entry(win, font=("Times New Roman", 15))
viewing_angel.grid(row=11, column=1, sticky="we")
viewing_angel.insert(0, "30")

# Рсстояние от источника
tk.Label(win,
         text="- расстояние от источника (м):",
         font=("Times New Roman", 15),
         ).grid(row=12, column=0, sticky="we")

laser_distance = tk.Entry(win, font=("Times New Roman", 15))
laser_distance.grid(row=12, column=1, sticky="we")
laser_distance.insert(0, "0.5")

# ********************************** КНОПКИ **********************************
start = tk.Button(win, text="Расчитать", font=("Times New Roman", 15), command=go, width=15, bg="#00FF00")
start.grid(row=13, column=1, pady=20, padx=50, sticky="w")

reset = tk.Button(win, text="Сброс", font=("Times New Roman", 15), command=clear_all, width=15, bg="red")
reset.grid(row=13, column=0, padx=50, sticky="e")

# ********************************** ПРАВОЕ МЕНЮ **********************************
# Выбор режима работы
mode = tk.IntVar()
sp_range = tk.IntVar()

working_mode = tk.Label(win,
                        text="Выберите режим работы лазера:",
                        font=("Times New Roman", 16, "bold"),
                        justify=tk.CENTER,
                        )
working_mode.grid(row=2, column=2, sticky="we", columnspan=2)

tk.Radiobutton(win,
               text="Непрерывный",
               font=("Times New Roman", 15),
               variable=mode,
               command=constant,
               value=1
               ).grid(row=3, column=2, columnspan=2)

tk.Radiobutton(win,
               text="Импульсный",
               font=("Times New Roman", 15),
               variable=mode, command=impulse,
               value=2
               ).grid(row=4, column=2, columnspan=2)

# Выбор спектрального диапазона
spectral_range = tk.Label(win,
                          text="Выберите спектральный диапазон лазера:      ",
                          font=("Times New Roman", 16, "bold"),
                          )
spectral_range.grid(row=5, column=2, sticky="we", columnspan=2)

tk.Radiobutton(win,
               text="от 380 до 1400 нм (вкл.)",
               font=("Times New Roman", 15),
               variable=sp_range,
               value=2
               ).grid(row=6, column=2, columnspan=2)

tk.Radiobutton(win,
               text="более 1400 нм",
               variable=sp_range,
               font=("Times New Roman", 15),
               value=3
               ).grid(row=7, column=2, columnspan=2)

# **********************************Результаты**********************************
tk.Label(win,
         text="Результаты расчета:",
         font=("Times New Roman", 16, "bold"),
         ).grid(row=8, column=2, sticky="we", columnspan=2)

tk.Label(win,
         text="- рассчитаное значение для кожи:",
         font=("Times New Roman", 15),
         ).grid(row=9, column=2, sticky="w")
#
measure_skin = tk.Entry(win)
measure_skin.grid(row=9, column=3, sticky="we")

tk.Label(win,
         text="- рассчитаное значение для глаз:",
         font=("Times New Roman", 15),
         ).grid(row=10, column=2, sticky="w")

measure_eyes = tk.Entry(win)
measure_eyes.grid(row=10, column=3, sticky="we")

tk.Label(win,
         text="- ПДУ для кожи:",
         font=("Times New Roman", 15),
         ).grid(row=11, column=2, sticky="w")

skin = tk.Entry(win)
skin.grid(row=11, column=3, sticky="we")

tk.Label(win,
         text="- ПДУ для глаз:",
         font=("Times New Roman", 15),
         ).grid(row=12, column=2, sticky="w")

eyes = tk.Entry(win)
eyes.grid(row=12, column=3, sticky="we")

win.mainloop()
