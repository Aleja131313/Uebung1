class WGS84Coord:
    def __init__ (self, longitud = 0, latitud = 0):
        self._longitud = longitud
        self._latitud = latitud

        if self._longitud <-180 or self._longitud > 180:
            if self._longitud > 0:
                self._longitud = self._longitud - 360 
            else:
                self._longitud = self._longitud + 360

        if self._latitud <-90 or self._latitud > 90:
            if self._latitud > 0:
                self._latitud = self._latitud - 180 
            else:
                self._latitud = self._latitud + 180

    def getLongitud (self):
        return self._longitud
    
    def getLatitud (self):
        return self._latitud
    
    def setLongitud (self, newLongitud):
        self._longitud = newLongitud

    def setLatitud (self, newLatitud):
        self._latitud = newLatitud
    
Koord = WGS84Coord (181, 100)

print (Koord.getLongitud (), Koord.getLatitud ())