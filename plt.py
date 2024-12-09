import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def plot_data(x, y, title, x_label, y_label):
    plt.scatter(x, y, color='blue', label='Dados')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid()
    plt.show()

def plot_interpolation(x, y, title, x_label, y_label):
    poly = CubicSpline(x, y)
    x_new = np.linspace(min(x), max(x), 500)
    y_new = poly(x_new)
    plt.scatter(x, y, color='blue', label='Dados')
    plt.plot(x_new, y_new, color='red', label='Interpolação')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid()
    plt.show()
    print(poly)
    return poly

def plot_derivative(poly, x, title, x_label, y_label):
    poly_derivative = poly.derivative()
    x_new = np.linspace(min(x) , max(x), 500)
    y_derivative = poly_derivative(x_new)
    plt.plot(x_new, y_derivative, color='green', label='Derivada')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid()
    plt.show()

def calculate_integral(poly, a, b):
    integral = poly.integrate(a, b)
    return integral
