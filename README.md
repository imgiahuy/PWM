
Das Programm wird in Python programmiert. 

Modul : 

math für sinus und pi 
time 
matplotlib.pyplot f+r plotting

Hauptfunktionsweise : 

da PWM ist ungerade => f(t) = A sin(2pi*t)

Für jedes "step" (diskret Punkt) in einer Periode 1/f berechnen sin_value oder helligkeit value des LED => duty circle = sin_value an Zeitpunkt t = current time - start time

sin_value = A/2 * (sin(2pi * step/steps) + 1)

sin(2pi * t) immer in [-1, 1]

deswegen offset + 1 => [0,2]

A/2 * [0, 2] => [0, 255] (by default)


