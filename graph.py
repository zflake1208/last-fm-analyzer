import matplotlib.pyplot as plt

def create_graph(x_label, y_label, x_values, y_values):
    plt.bar(x_values, y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()