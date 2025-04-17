class WGS84Coord:
    def __init__(self, länge=0, breite=0):
        self._longitud = 0
        self._latitud = 0
        self.longitud = länge
        self.latitud = breite

    @property
    def longitud(self):
        return self._longitud

    @longitud.setter
    def longitud(self, value):
        if value < -180 or value > 180:
            print("Warnung: Längengrad korrigiert")

            if value > 180:
                value -= 360
            else:
                value += 360
        self._longitud = value

    @property
    def latitud(self):
        return self._latitud

    @latitud.setter
    def latitud(self, value):
        if value < -90 or value > 90:
            print("Warnung: Breitengrad korrigiert")

            if value > 90:
                value -= 180
            else:
                value += 180
        self._latitud = value


koord = WGS84Coord(181, 100)

print(koord.longitud, koord.latitud)
