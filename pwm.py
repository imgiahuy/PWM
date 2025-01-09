import math
import time
import matplotlib.pyplot as plt


def sinus_pwm(frequency=500, amplitude=255, duration=10):
    period = 1 / frequency  # Period of the PWM signal
    steps = 100 # Steps per period
    interval = period / steps  # Time interval between steps

    start_time = time.time()

    plt.ion()  #real time plot
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    line, = ax.plot([], [], 'r-')

    ax.set_xlim(0, duration)  # X-axis (time)
    ax.set_ylim(0, amplitude)  # Y-axis (duty cycle)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Duty Cycle")
    ax.set_title("PWM Duty Cycle Simulation (Sine Wave)")

    while time.time() - start_time < duration:
        for step in range(steps):
            # Calculate sine value (between 0 and 255), already in Helligkeit calculated
            sin_value = (amplitude / 2) * (1 + math.sin(2 * math.pi * step / steps))

            # Calculate PWM duty cycle, simply = sin_value
            duty_cycle = int(sin_value)

            # Append data for plotting
            elapsed_time = time.time() - start_time
            x_data.append(elapsed_time)
            y_data.append(duty_cycle)

            # Update the plot
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            fig.canvas.draw()
            fig.canvas.flush_events()

            time.sleep(interval)

    plt.ioff()
    plt.show()


def main():
    try:
        print("PWM Signal Control and LED Brightness")
        frequency = float(input("Enter PWM frequency (Hz, e.g., 500): "))
        amplitude = int(input("Enter amplitude (e.g., 255 for 8-bit PWM): "))
        duration = float(input("Enter simulation duration (seconds): "))
        sinus_pwm(frequency, amplitude, duration)

    except KeyboardInterrupt:
        print("Program interrupted.")


if __name__ == "__main__":
    main()
