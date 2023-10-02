import tkinter as tk
import time

# Formatare cifre ora in segmente
segments = {
        '0': [' _ ',
              '| |',
              '|_|',
              '   '],

        '1': ['   ',
              '  |',
              '  |',
              '   '],

        '2': [' _ ',
              ' _|',
              '|_ ',
              '   '],

        '3': [' _ ',
              ' _|',
              ' _|',
              '   '],

        '4': ['   ',
              '|_|',
              '  |',
              '   '],

        '5': [' _ ',
              '|_ ',
              ' _|',
              '   '],

        '6': [' _ ',
              '|_ ',
              '|_|',
              '   '],

        '7': [' _ ',
              '  |',
              '  |',
              '   '],

        '8': [' _ ',
              '|_|',
              '|_|',
              '   '],

        '9': [' _ ',
              '|_|',
              ' _|',
              '   '],

        ':': ['   ',
              ' o ',
              ' o ',
              '   ']  # Separator
}

def update_time():                            # Definire format ora curenta
    current_time = time.strftime('%H:%M:%S')
    display_time(current_time)
    clock_label.after(1000, update_time)  # Actualizare ora la 1 secunda

def display_time(current_time):               # Definire afisare ora in segmente
    time_segments = []

    for char in current_time:
        time_segments.extend(segments[char])

    display = ''
    for i in range(4):  # 4 segmente per cifra
        display += ' '.join(time_segments[i::4]) + '\n'

    clock_label.config(text=display)

root = tk.Tk()                              # Creez o fereastra de afisare
root.title('CEAS DIGITAL MAG')

# Formatare fereastra
clock_label = tk.Label(root, font=('Courier', 40), bg='black', fg='green', justify='left')
clock_label.pack(fill='both', expand=True)

update_time()                               # Update ora

root.mainloop()                             # Ruleaza aplicatia
