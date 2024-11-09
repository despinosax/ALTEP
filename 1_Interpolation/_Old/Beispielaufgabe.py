import numpy as np
import matplotlib.pyplot as plt

# Funktion zur linearen Interpolatin
def interpolate(x, x1, x2, y1, y2):
    '''
    Lineare Interpolation von x zwischen den Punkten (x1, y1) und (x2, y2)
    
        Parameter:
            x           : x-Wert, an dem interpoliert werden soll
            (x1, x2)    : Bekannte Stützstellen
            (y1, y2)    : Bekannte Stützwerte
            
        Rückgabe:
            y           : Lösungsvektor
    '''

    # Bedingung, dass x zwischen x1 und x2 liegt
    if x1 <= x <= x2:
    
        return (y2 - y1) / (x2 - x1) * (x - x1) + y1

    # Falls Bedingung nicht erfüllt, Fehlermeldung
    else:

        raise ValueError('x-Wert liegt nicht zwischen den Stützstellen!')


# Rohdaten von Zeit und Windgeschwindigkeit
zeit, geschwindigkeit = np.genfromtxt("Daten/geschwindigkeit.csv", delimiter=",", unpack=True)

# Schleife über alle (inneren) Zeiten
for index in range(1, len(zeit)-1):

    # Überprüfe, ob Windgeschwindigkeit fehlerhaft (d.h. = 0) ist
    if geschwindigkeit[index] == 0:

        # Aufruf der Interpolationsfunktion und Überschreiben der fehlerhaften Geschwindigkeit
        geschwindigkeit[index] = interpolate(
            zeit[index],
            zeit[index-1],
            zeit[index+1],
            geschwindigkeit[index-1],
            geschwindigkeit[index+1]
        )
    
# Darstellen der korrigierten Geschwindigkeiten
plt.xlabel("Zeit [min]")
plt.ylabel("Windgeschwindigkeit [m/s]")
plt.title("Korrigierte Windgeschwindigkeit")
plt.grid(linewidth=0.5,zorder=0)
plt.scatter(zeit, geschwindigkeit, zorder=3)
plt.tight_layout()
plt.ylim(0,10)

plt.show()