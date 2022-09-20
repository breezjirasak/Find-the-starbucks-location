import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkintermapview import TkinterMapView
from choice import *


class App(tk.Tk):

    def __init__(self, data):
        """ To initialize the app object

        :param data: Dataframe
        """
        super().__init__()

        # Dataframe
        self.data = data

        # list of marker
        self.list_country_marker = []
        self.list_city_marker = []
        self.list_postcode_marker = []

        # keep the value of combobox
        self.name_country = tk.StringVar()
        self.name_city = tk.StringVar()
        self.name_postcode = tk.StringVar()

        # initialize all component
        self.init_component()
        self.load_country()

    def init_component(self):
        """ Initialize the component"""

        self.title('Find The Starbucks Location')

        # combobox color
        combobox_style = ttk.Style()

        combobox_style.theme_create('combobox_style', parent='alt',
                                    settings={'TCombobox': {
                                        'configure': {'selectbackground': '#00704A', 'fieldbackground': '#00704A',
                                                      'background': 'white', 'foreground': 'white'}}})
        combobox_style.theme_use('combobox_style')

        # progress bar color
        progress_style = ttk.Style()
        progress_style.configure("green.Horizontal.TProgressbar",
                                 foreground='#00704A', background='#00704A')

        self.geometry("800x600")

        self.configure(background='#00704A')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)

        # Frame of map

        self.frame_map = tk.Frame(self, bg='#00704A')
        self.frame_map.grid(row=0, column=0, columnspan=2, pady=10, padx=20, sticky=tk.NSEW)

        self.map_widget = TkinterMapView(self.frame_map, corner_radius=9)
        self.map_widget.grid(row=0, column=0, sticky=tk.NSEW, padx=20, pady=20)
        self.map_widget.set_position(13, 100)
        self.map_widget.set_zoom(3)

        self.frame_map.grid_rowconfigure(0, weight=1)
        self.frame_map.grid_columnconfigure(0, weight=1)

        # frame for searching
        self.frame_buttom = tk.Frame(self, bg='#00704A')
        self.frame_buttom.grid(row=1, column=0, columnspan=2, padx=20, sticky=tk.NSEW)

        self.title_ = tk.Label(self.frame_buttom, text='Starbucks location', anchor='center', bg='#00704A', fg='white',
                               font=('Arial', 18))
        self.title_.grid(row=0, column=1)

        self.country_label = tk.Label(self.frame_buttom, text='Country', bg='#00704A', fg='white')
        self.country_label.grid(row=1, column=0, padx=5, sticky=tk.NSEW)
        self.country_combo = ttk.Combobox(self.frame_buttom, state='readonly', textvariable=self.name_country)
        self.country_combo.grid(row=2, column=0, padx=5, pady=5, sticky=tk.NSEW)
        self.country_combo.bind('<<ComboboxSelected>>', lambda event: self.country_selected())

        self.city_label = tk.Label(self.frame_buttom, text='City', bg='#00704A', fg='white')
        self.city_label.grid(row=1, column=1, padx=5, sticky=tk.NSEW)
        self.city_combo = ttk.Combobox(self.frame_buttom, state='readonly', textvariable=self.name_city)
        self.city_combo.grid(row=2, column=1, padx=5, pady=5, sticky=tk.NSEW)
        self.city_combo.bind('<<ComboboxSelected>>', lambda event: self.city_selected())

        self.postcode_label = tk.Label(self.frame_buttom, text='Postcode', bg='#00704A', fg='white')
        self.postcode_label.grid(row=1, column=2, padx=5, sticky=tk.NSEW)
        self.postcode_combo = ttk.Combobox(self.frame_buttom, state='readonly', textvariable=self.name_postcode)
        self.postcode_combo.grid(row=2, column=2, padx=5, pady=5, sticky=tk.NSEW)
        self.postcode_combo.bind('<<ComboboxSelected>>', lambda event: self.postcode_selected())

        self.frame_buttom.grid_columnconfigure(0, weight=1)
        self.frame_buttom.grid_columnconfigure(1, weight=1)
        self.frame_buttom.grid_columnconfigure(2, weight=1)
        self.frame_buttom.grid_rowconfigure(0, weight=1)
        self.frame_buttom.grid_rowconfigure(1, weight=1)

        # frame for progress bar
        self.frame_progress = tk.Frame(self, bg='#00704A')
        self.frame_progress.grid(row=2, column=0, padx=20, pady=20, sticky=tk.NSEW)

        self.bar = ttk.Progressbar(self.frame_progress, mode="determinate", style="green.Horizontal.TProgressbar")
        self.bar.grid(row=0, column=0, sticky=tk.EW)

        self.frame_progress.grid_rowconfigure(0, weight=1)
        self.frame_progress.grid_columnconfigure(0, weight=1)

        # frame for quit and clear
        self.frame_ = tk.Frame(self, width=150, bg='#00704A')
        self.frame_.grid(row=2, column=1, padx=20, pady=20, sticky=tk.NSEW)

        self.quit = tk.Button(self.frame_, text='Quit', command=self.destroy)
        self.quit.grid(row=0, column=1, padx=5, sticky=tk.EW)

        self.clear = tk.Button(self.frame_, text='Clear', command=self.clear)
        self.clear.grid(row=0, column=0, padx=5, sticky=tk.EW)

        self.frame_.grid_rowconfigure(0, weight=1)
        self.frame_.grid_columnconfigure(1, weight=1)

    def clear(self):
        """ Clear method"""

        # Start the progress bar
        self.bar.start()

        # Clear all marker
        if len(self.list_country_marker) > 0:
            for i in self.list_country_marker:
                i.delete()
            self.list_country_marker = []

        if len(self.list_city_marker) > 0:
            for i in self.list_city_marker:
                i.delete()
            self.list_city_marker = []

        if len(self.list_postcode_marker) > 0:
            for i in self.list_postcode_marker:
                i.delete()
            self.list_postcode_marker = []

        # Clear the combobox
        self.city_combo['values'] = ''
        self.postcode_combo['values'] = ''
        self.name_country.set('')
        self.name_city.set('')
        self.name_postcode.set('')

        self.map_widget.set_zoom(3)

        # Stop the progressbar
        self.bar.stop()
        self.bar.configure(value=100)

    def load_country(self):
        """ load unit to the country combobox"""
        self.country_combo['values'] = self.data.get_column(self.data.df, 'Country')
        self.name_city.set('')
        self.name_postcode.set('')

    def country_selected(self):
        """ Update method when the country is selected"""

        # Start the progress bar
        self.bar.start()
        # dataframe of country that already filter by user
        filter_country = self.data.filter('Country', self.name_country.get(), self.data.df)
        # load unit to the city combobox
        self.city_combo['values'] = self.data.get_column(filter_country, 'City')
        self.name_city.set('')
        self.name_postcode.set('')

        # Clear the old marker
        if len(self.list_city_marker) > 0:
            for i in self.list_city_marker:
                i.delete()
            self.list_city_marker = []

        if len(self.list_postcode_marker) > 0:
            for i in self.list_postcode_marker:
                i.delete()
            self.list_postcode_marker = []

        if len(self.list_country_marker) > 0:
            for i in self.list_country_marker:
                i.delete()
            self.list_country_marker = []

        # Set position and mark the position
        set_pos = CountryStrategy(self.map_widget)
        set_pos.zoom(self.data.get_avg(filter_country, 'Latitude'), self.data.get_avg(filter_country, 'Longitude'), 3)
        # for the US it is too many location in there around ten thousand.
        # It can not mark all the position that will make the program freeze.
        if self.name_country.get() == 'United States':
            messagebox.showinfo('Information',
                                'To many location on United states, can not mark all, Please select the city first.')
        else:
            set_pos.mark(list(filter_country['Latitude']), list(filter_country['Longitude']),
                         list(filter_country['Store Name']))
            self.list_country_marker.append(set_pos)

        # Stop the progress bar
        self.bar.stop()
        self.bar.configure(value=100)

    def city_selected(self):
        """ Update method when the city is selected"""

        # Start the progress bar
        self.bar.start()

        # Dataframe of city that already filter by user
        filter_country = self.data.filter('Country', self.name_country.get(), self.data.df)
        filter_city = self.data.filter('City', self.name_city.get(), filter_country)
        # load unit to the postcode combobox
        self.postcode_combo['values'] = self.data.get_column(filter_city, 'Postcode')
        self.name_postcode.set('')

        # Clear the old marker
        if len(self.list_country_marker) > 0:
            for i in self.list_country_marker:
                i.delete()
            self.list_country_marker = []

        if len(self.list_postcode_marker) > 0:
            for i in self.list_postcode_marker:
                i.delete()
            self.list_postcode_marker = []

        if len(self.list_city_marker) > 0:
            for i in self.list_city_marker:
                i.delete()
            self.list_city_marker = []

        # Set position and mark the position
        set_pos = CityStrategy(self.map_widget)
        set_pos.zoom(self.data.get_avg(filter_city, 'Latitude'), self.data.get_avg(filter_city, 'Longitude'), 8)
        set_pos.mark(list(filter_city['Latitude']), list(filter_city['Longitude']), list(filter_city['Store Name']))
        self.list_city_marker.append(set_pos)

        # Stop the progress bar
        self.bar.stop()
        self.bar.configure(value=100)

    def postcode_selected(self):
        """ Update method when the postcode is selected"""

        # Start the progress bar
        self.bar.start()
        filter_country = self.data.filter('Country', self.name_country.get(), self.data.df)
        filter_city = self.data.filter('City', self.name_city.get(), filter_country)
        filter_postcode = self.data.filter('Postcode', self.name_postcode.get(), filter_city)

        # Clear the old marker
        if len(self.list_country_marker) > 0:
            for i in self.list_country_marker:
                i.delete()
            self.list_country_marker = []

        if len(self.list_city_marker) > 0:
            for i in self.list_city_marker:
                i.delete()
            self.list_city_marker = []

        if len(self.list_postcode_marker) > 0:
            for i in self.list_postcode_marker:
                i.delete()
            self.list_postcode_marker = []

        # Set position and mark the position
        set_pos = PostCodeStrategy(self.map_widget)
        set_pos.zoom(self.data.get_avg(filter_postcode, 'Latitude'), self.data.get_avg(filter_postcode, 'Longitude'), 10)
        set_pos.mark(list(filter_postcode['Latitude']), list(filter_postcode['Longitude']),
                     list(filter_postcode['Store Name']))
        self.list_postcode_marker.append(set_pos)

        # Stop the progress bar
        self.bar.stop()
        self.bar.configure(value=100)

    def run(self):
        """ Run the program"""
        self.mainloop()
