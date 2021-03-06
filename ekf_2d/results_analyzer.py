import pandas as pd
import matplotlib.pyplot as plt

import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
log_dir = str(current_dir) + '/log/'

def show_plt(title, data_list):
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.set_title(title)

    for data in data_list:
        ax.plot(data[0], data[1], label=data[2])

    plt.legend()

true_state = pd.read_csv(log_dir + 'true_state.csv')
ekf_state = pd.read_csv(log_dir + 'ekf_state.csv')
integral_state = pd.read_csv(log_dir + 'integral_state.csv')
target_state = pd.read_csv(log_dir + 'target_state.csv')

show_plt('X Y', [[ekf_state['X'], ekf_state['Y'], 'ekf'],
                 [integral_state['X'], integral_state['Y'], 'only integral'],
                 [true_state['X'], true_state['Y'], 'true']])

show_plt('yaw', [[ekf_state['time'], ekf_state['yaw'], 'ekf'],
                 [integral_state['time'], integral_state['yaw'], 'only integral'],
                 [true_state['time'], true_state['yaw'], 'true']])

show_plt('X error', [[ekf_state['time'], ekf_state['X'] - true_state['X'], 'ekf'],
                     [integral_state['time'], integral_state['X'] - true_state['X'], 'only integral']])

show_plt('Y error', [[ekf_state['time'], ekf_state['Y'] - true_state['Y'], 'ekf'],
                     [integral_state['time'], integral_state['Y'] - true_state['Y'], 'only integral']])

show_plt('yaw error', [[ekf_state['time'], ekf_state['yaw'] - true_state['yaw'], 'ekf'],
                     [integral_state['time'], integral_state['yaw'] - true_state['yaw'], 'only integral']])

show_plt('X', [[target_state['time'], target_state['X'], 'target'],
                 [true_state['time'], true_state['X'], 'true']])

show_plt('Y', [[target_state['time'], target_state['Y'], 'target'],
                 [true_state['time'], true_state['Y'], 'true']])

show_plt('yaw', [[target_state['time'], target_state['yaw'], 'target'],
                 [true_state['time'], true_state['yaw'], 'true']])


plt.show()
