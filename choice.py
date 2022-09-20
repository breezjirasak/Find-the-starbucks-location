class CountryStrategy:
    def __init__(self, map):
        """ to initialize the country class

        :param map: Map widget
        """
        self.map = map
        # list of marker
        self.mark_list = []

    def zoom(self, lat, lon, zoom):
        """ to set position and zoom in to that position

        :param lat: Average latitude of country
        :param lon: Average longitude of country
        :param zoom: number to zoom
        """
        self.map.set_zoom(zoom)
        self.map.set_position(lat, lon)

    def mark(self, list_lat, list_lon, list_text):
        """ To mark all the position on the country

        :param list_lat: List of all position
        :param list_lon: List of all position
        :param list_text: Store name
        """
        for i in range(len(list_lat)):
            mark = self.map.set_marker(list_lat[i], list_lon[i], text=list_text[i])
            self.mark_list.append(mark)

    def delete(self):
        """ to delete the marker"""
        for mark in self.mark_list:
            mark.delete()


class CityStrategy:
    def __init__(self, map):
        """ to initialize the City class

        :param map: Map widget
        """
        self.map = map
        # list of marker
        self.mark_list = []

    def zoom(self, lat, lon, zoom):
        """ to set position and zoom in to that position

        :param lat: Average latitude of city
        :param lon: Average longitude of city
        :param zoom: number to zoom
        """
        self.map.set_zoom(zoom)
        self.map.set_position(lat, lon)

    def mark(self, list_lat, list_lon, list_text):
        """ To mark all the position in the city

        :param list_lat: List of all position
        :param list_lon: List of all position
        :param list_text: Store name
        """
        for i in range(len(list_lat)):
            mark = self.map.set_marker(list_lat[i], list_lon[i], text=list_text[i])
            self.mark_list.append(mark)

    def delete(self):
        """ to delete the marker"""
        for mark in self.mark_list:
            mark.delete()


class PostCodeStrategy:
    def __init__(self, map):
        """ to initialize the Postcode class

        :param map: Map widget
        """
        self.map = map
        # list of marker
        self.mark_list = []

    def zoom(self, lat, lon, zoom):
        """ to set position and zoom in to that position

        :param lat: Average latitude of postcode area
        :param lon: Average longitude of postcode area
        :param zoom: number to zoom
        """
        self.map.set_zoom(zoom)
        self.map.set_position(lat, lon)

    def mark(self, list_lat, list_lon, list_text):
        """ To mark all the position in the postcode area

        :param list_lat: List of all position
        :param list_lon: List of all position
        :param list_text: Store name
        """
        for i in range(len(list_lat)):
            mark = self.map.set_marker(list_lat[i], list_lon[i], text=list_text[i])
            self.mark_list.append(mark)

    def delete(self):
        """ to delete the marker"""
        for mark in self.mark_list:
            mark.delete()
