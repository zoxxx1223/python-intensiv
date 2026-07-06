"""
          0   1    2    3
    - -|----|----|----|----|-
     0 |    |    |    |    |
    - -|----|----|----|----|-
 Y   1 |    | S  |    |    |
    - -|----|----|----|----|-
     2 |    |    |    |    |
    - -|----|----|----|----|-
     3 |    |    |    |    |
    - -|----|----|----|----|-

    <- X ->

Gegeben ist ein Spielfeld mit einer Größe von **200 × 200 Pixeln**.
Es ist in ein **4 × 4 Raster** unterteilt. Jedes Rasterfeld hat eine Kantenlänge
von **50 Pixeln**.

Der Ursprung des Koordinatensystems liegt oben links bei **(0, 0)**.
Die X-Achse verläuft nach rechts, die Y-Achse nach unten.


Die Spielfigur besteht aus genau **einem Pixel**.
Die Position der Spielfigur gibt an, **an welchem Pixel** sie sich befindet.

Da das Spielfeld bei `(0, 0)` beginnt und bei `(199, 199)` endet, sind nur
Koordinaten von **0 bis 199** gültig. Eine Position mit `x = 200` oder
`y = 200` liegt bereits außerhalb des Spielfelds.

Die Bodenarten der Rasterfelder sind in folgender Matrix gespeichert
(`0=Fels`, `1=Wiese`, `2=Wasser`, `3=Schlamm`, `4=Wüste`):

```python
GROUND = [
    [1, 1, 1, 1],
    [1, 3, 1, 2],
    [1, 0, 3, 1],
    [2, 1, 1, 0],
]
```

### Aufgabe

1. Lies die **X- und Y-Koordinate** per `input()` ein.
2. Prüfe, ob sich die Spielfigur noch innerhalb des Spielfelds befindet.
3. Bestimme das Rasterfeld, in dem sich die Spielfigur befindet.
4. Gib zusätzlich die Bodenart des Feldes aus.
5. Liegt die Spielfigur außerhalb des Spielfelds, gib `"Player befindet sich
außerhalb des Spielfelds."` aus.

### Beispiele

```text
x=0,   y=0    -> Raster: 0/0
x=50,  y=10   -> Raster: 1/0
x=52,  y=50   -> Raster: 1/1
x=48,  y=190  -> Raster: 0/3
x=199, y=199  -> Raster: 3/3
x=200, y=90   -> Player befindet sich außerhalb des Spielfelds.
```

Verwende sinnvolle **Konstanten** (z.B. Spielfeldgröße und Feldgröße),
Variablen sowie **f-Strings** für die Ausgabe.

Du kannst davon ausgehen, dass die Eingaben immer positive,
nach `int` konvertierbare Werte sind.
"""