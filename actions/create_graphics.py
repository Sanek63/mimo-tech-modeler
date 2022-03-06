import matplotlib.pyplot as plt  # Библиотека для графического отображения объектов
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def create_graphics(Eb_N0_dB, alg, simBer, color):
    """
        Данная функция предназначена
        для создания графика из двух
        полученных аргументов
    """
    fig, ax = plt.subplots()

    ax.set(xlabel='ОСШ', ylabel='Битовый коэффициент ошибок', title='BER системы MIMO 2х2 в канале с МСИ, L=3')
    ax.set_xlim(0, xmax=Eb_N0_dB[-1])
    ax.set_ylim(10 ** -3, ymax=1.5)

    plt.plot(Eb_N0_dB, simBer, label=alg, color="{}".format(color), lw=2, ls="--", marker="*")

    plt.yscale("log")
    plt.grid(True)

    lgnd = ax.legend(loc="upper left", )
    lgnd.get_frame().set_facecolor('#ffb19a')

    canvas = FigureCanvas(fig)
    canvas.draw()
    canvas.show()

    return
