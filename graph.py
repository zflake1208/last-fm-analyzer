import matplotlib.pyplot as plt

def create_graph(x_label, y_label, x_values, y_values):
    label_font = {'size': 12}
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 10)
    ax.ticklabel_format(style='plain')
    plt.bar(x_values, y_values)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.xlabel(x_label, label_font)
    plt.ylabel(y_label, label_font)
    plt.show()