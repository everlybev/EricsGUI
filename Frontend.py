from Backend import *
from tkinter import *
from Widgets import *
import ctypes
from PIL import Image, ImageTk

class Window(Tk):
    def __init__(self, media_path=r"D:\Pictures\Eagle", master_csv='Media.csv',
                 icon_filename='icon.png', title='Eric\'s GUI'):
        self.root = Tk()
        self.backend = BackendFuncs(media_path, master_csv)
        u = ctypes.windll.user32
        [self.screenwidth_in_pixels, self.screenheight_in_pixels] = [u.GetSystemMetrics(0), u.GetSystemMetrics(1)]
        #print(self.screenwidth_in_pixels, self.screenheight_in_pixels)
        self.root.title(title)
        self.icon = Image.open(icon_filename)
        self.photo = ImageTk.PhotoImage(self.icon)
        self.root.wm_iconphoto(False, self.photo)


    def set_title(self, title):
        self.title(title)
    
    def scale_image(self):
        pass

    def set_background(self, image):
        self.image_filename = image
        self.image = Image.open(self.image_filename)
        resize_image = self.image.resize((self.window_width, self.window_height))
        img = ImageTk.PhotoImage(resize_image)
        self.image_Lable = Label(self.root, image=img)
        self.image_Lable.image = img
        self.image_Lable.pack()


    def set_window_dimensions(self, width, height):
        self.window_width = width
        self.window_height = height
        self.root.geometry('{}x{}'.format(width, height))

    def build_app(self, image=r"Background.png", w=960, h=540):
        self.set_window_dimensions(w, h)
        self.set_background(image)


        personList = Listbox_widget(self.root)
        personList.add_widget('Multiple', self.backend.list_of_people, 555, 200,
                     self.screenwidth_in_pixels, 2*self.screenheight_in_pixels/3)
        personList.place_here(1, 31, 1, 1)
        personListx = personList.width
        personListy = personList.height
        
        personADD = Button_Widget(self.root)
        personADD.add_widget('Add', self.backend.add_people_to_search, personList.listboxess[0], 222, 123)
        personADD.place_here(personList.width+1, 40, 1, 1)
        personADDx = personADD.x
        personADDy = personADD.y

        personRemove = Button_Widget(self.root)
        personRemove.add_widget('Remove', self.backend.remove_people_from_search,
                                  personList.listboxess[0], 123, 222)
        personRemove.place_here(personListx+1, personADDy+(personRemove.height/2), 2, 3)

        personExclude = Button_Widget(self.root)
        personExclude.add_widget('Exclude', self.backend.set_desire,
                                   self.backend.desired_or_undesired_options[1], 123, 222)
        personExclude.place_here(personListx+1, personRemove.y+(personExclude.height/2), 3, 4)

        personInclude = Button_Widget(self.root)
        personInclude.add_widget('Include', self.backend.set_desire,
                                   self.backend.desired_or_undesired_options[0], 123, 222)
        personInclude.place_here(personListx+1,
                                personExclude.y+(personInclude.height/2), 3, 4)

        personLabel = Label_Widget(self.root)
        personLabel.add_widget('People', 555, 10)
        personLabel.place_here(personLabel.x/2, 5, 0, 1)


        genreList = Listbox_widget(self.root)
        genreList.add_widget('Multiple', self.backend.list_of_genres, 555, 200,
                     self.screenwidth_in_pixels, int(1.5*self.screenheight_in_pixels/3))
        longest_buttonx = max(personExclude.x, personRemove.x, personADD.x)
        longest_buttonw = max(personExclude.width, personRemove.width, personADD.width)
        genreListCenterX = longest_buttonx+longest_buttonw+1
        genreList.place_here(genreListCenterX, 31, 1, 1)
        
        genreADD = Button_Widget(self.root)
        genreADD.add_widget('Add', self.backend.add_genres_to_search, genreList.listboxess[0], 222, 123)
        genreADD.place_here(genreListCenterX+genreList.width+1, 40, 1, 1)

        genreRemove = Button_Widget(self.root)
        genreRemove.add_widget('Remove', self.backend.remove_genres_from_search,
                                  genreList.listboxess[0], 123, 222)
        genreRemove.place_here(genreListCenterX+genreList.width+1, genreADD.y+(genreRemove.height/2), 2, 3)

        genreExclude = Button_Widget(self.root)
        genreExclude.add_widget('Exclude', self.backend.set_desire,
                                   self.backend.desired_or_undesired_options[1], 123, 222)
        genreExclude.place_here(genreListCenterX+genreList.width+1, genreRemove.y+(genreExclude.height/2), 3, 4)

        genreInclude = Button_Widget(self.root)
        genreInclude.add_widget('Include', self.backend.set_desire,
                                   self.backend.desired_or_undesired_options[0], 123, 222)
        genreInclude.place_here(genreListCenterX+genreList.width+1, genreExclude.y+(genreInclude.height/2), 3, 4)

        genreLabel = Label_Widget(self.root)
        genreLabel.add_widget('Genres', 555, 10)
        genreLabel.place_here(genreList.x-(genreLabel.width/2), 5, 0, 1)


        placesList = Listbox_widget(self.root)
        placesList.add_widget('Multiple', self.backend.list_of_places, 555, 200,
                     self.screenwidth_in_pixels, (self.screenheight_in_pixels/3))
        longest_buttonx = max(genreExclude.x, genreRemove.x, genreADD.x)
        longest_buttonw = max(genreExclude.width, genreRemove.width, genreADD.width)
        placesListCenterX = longest_buttonx+longest_buttonw+1
        placesList.place_here(placesListCenterX, 31, 1, 1)
        
        placesADD = Button_Widget(self.root)
        placesADD.add_widget('Add', self.backend.add_places_to_search, placesList.listboxess[0], 222, 123)
        placesADD.place_here(placesListCenterX+placesList.width+1, 40, 1, 1)

        placesRemove = Button_Widget(self.root)
        placesRemove.add_widget('Remove', self.backend.remove_places_from_search,
                                  placesList.listboxess[0], 123, 222)
        placesRemove.place_here(placesListCenterX+placesList.width+1,
                                     placesADD.y+(placesRemove.height/2), 2, 3)

        placesExclude = Button_Widget(self.root)
        placesExclude.add_widget('Exclude', self.backend.set_desire,
                                   self.backend.desired_or_undesired_options[1], 123, 222)
        placesExclude.place_here(placesListCenterX+placesList.width+1,
                                      placesRemove.y+(placesExclude.height/2), 3, 4)

        placesInclude = Button_Widget(self.root)
        placesInclude.add_widget('Include', self.backend.set_desire,
                                   self.backend.desired_or_undesired_options[0], 123, 222)
        placesInclude.place_here(placesListCenterX+placesList.width+1,
                                placesExclude.y+(placesInclude.height/2), 3, 4)

        placesLabel = Label_Widget(self.root)
        placesLabel.add_widget('Places', 555, 10)
        placesLabel.place_here(placesList.x-(placesLabel.width/2), 5, 0, 1)


        hoursInput = Textinput_Widget(self.root)
        hoursInput.add_widget(2, 1)
        leftWidgetX = max([placesInclude.x, placesExclude.x, placesADD.x, placesRemove.x])
        widget_widths = [placesInclude.width, placesExclude.width,
                         placesADD.width, placesRemove.width]
        leftWidgetw = max(widget_widths)
        hoursInput.place_here(leftWidgetX+leftWidgetw, placesList.y-(placesList.height/2))
        
        hoursButton = Button_Widget(self.root)
        hoursButton.add_widget('H', self.backend.update_hours, hoursInput.inputboxes[len(hoursInput.inputboxes)-1],
                               222, 123)
        hoursButton.place_here(hoursInput.x+(hoursInput.width/2)+1, hoursInput.y-(hoursInput.height/2), 1, -1)


        minutesInput = Textinput_Widget(self.root)
        minutesInput.add_widget(2, 1)
        minutesInput.place_here(hoursButton.x+(hoursButton.width/2), placesList.y-(placesList.height/2))
        
        minutesButton = Button_Widget(self.root)
        minutesButton.add_widget('M', self.backend.update_minutes,
                                 minutesInput.inputboxes[len(minutesInput.inputboxes)-1], 222, 123)
        minutesButton.place_here(minutesInput.x+(minutesInput.width/2)+1,
                                 minutesInput.y-(minutesInput.height/2), 1, -1)


        secondsInput = Textinput_Widget(self.root)
        secondsInput.add_widget(4, 1)
        secondsInput.place_here(minutesButton.x+(minutesButton.width/2), placesList.y-(placesList.height/2))
        
        secondsButton = Button_Widget(self.root)
        secondsButton.add_widget('S', self.backend.update_seconds,
                                 secondsInput.inputboxes[len(secondsInput.inputboxes)-1], 222, 123)
        secondsButton.place_here(secondsInput.x+(secondsInput.width/2)+1,
                                 secondsInput.y-(secondsInput.height/2), 1, -1)
        

        EqualsButton = Button_Widget(self.root)
        comparor = '='
        EqualsButton.add_widget(comparor, self.backend.update_comparator, comparor, 222, 123)
        EqualsButton.place_here(hoursInput.x-hoursInput.width/2,
                                 hoursInput.y+(hoursInput.height), 1, -1)
        leftwidgetx = EqualsButton.x
        leftWidgetw = EqualsButton.width
        
        GreaterthanEqualsButton = Button_Widget(self.root)
        comparor = '>='
        GreaterthanEqualsButton.add_widget(comparor, self.backend.update_comparator, comparor, 222, 123)
        GreaterthanEqualsButton.place_here(leftwidgetx+leftWidgetw/2,
                                 hoursInput.y+(hoursInput.height), 1, -1)
        leftwidgetx = GreaterthanEqualsButton.x
        leftWidgetw = GreaterthanEqualsButton.width
        
        LessthanEqualsButton = Button_Widget(self.root)
        comparor = '<='
        LessthanEqualsButton.add_widget(comparor, self.backend.update_comparator, comparor, 222, 123)
        LessthanEqualsButton.place_here(leftwidgetx+leftWidgetw/2,
                                 hoursInput.y+(hoursInput.height), 1, -1)
        leftwidgetx = LessthanEqualsButton.x
        leftWidgetw = LessthanEqualsButton.width
        
        NotEqualsButton = Button_Widget(self.root)
        comparor = '!='
        NotEqualsButton.add_widget(comparor, self.backend.update_comparator, comparor, 222, 123)
        NotEqualsButton.place_here(leftwidgetx+leftWidgetw/2,
                                 hoursInput.y+(hoursInput.height), 1, -1)
        leftwidgetx = NotEqualsButton.x
        leftWidgetw = NotEqualsButton.width
        
        LessButton = Button_Widget(self.root)
        comparor = '<'
        LessButton.add_widget(comparor, self.backend.update_comparator, comparor, 222, 123)
        LessButton.place_here(leftwidgetx+leftWidgetw/2,
                                 hoursInput.y+(hoursInput.height), 1, -1)
        leftwidgetx = LessButton.x
        leftWidgetw = LessButton.width
        
        GreatButton = Button_Widget(self.root)
        comparor = '>'
        GreatButton.add_widget(comparor, self.backend.update_comparator, comparor, 222, 123)
        GreatButton.place_here(leftwidgetx+leftWidgetw/2,
                                 hoursInput.y+(hoursInput.height), 1, -1)
        leftwidgetx = GreatButton.x
        leftWidgetw = GreatButton.width


        FilteredList = Listbox_widget(self.root)
        FilteredList.add_widget('Single', self.backend.list_of_filez_from_dataframe(self.backend.filtereddataframe),
                                'Not using', 'Not using',
                     self.screenwidth_in_pixels, (self.screenheight_in_pixels/1.75))
        FilteredList.place_here(1, personList.x+personList.width*2, 1, 1)
        
        PlayButton = Button_Widget(self.root)
        PlayButton.add_widget('Play', self.backend.open_file,
                              FilteredList, 222, 123)
        PlayButton.place_here(1, FilteredList.y+(FilteredList.height/2), 1, 8)
        
        PlayRandomButton = Button_Widget(self.root)
        PlayRandomButton.add_widget('Filter Random', self.backend.open_random_file,
                              self.backend.filtereddataframe, 222, 123)
        PlayRandomButton.place_here(PlayButton.x+PlayButton.width, FilteredList.y+(FilteredList.height/2), 2, 8)
        
        TrueRandomButton = Button_Widget(self.root)
        TrueRandomButton.add_widget('True Random', self.backend.open_random_file_for_real,
                              self.backend.filtereddataframe, 222, 123)
        TrueRandomButton.place_here(PlayRandomButton.x+PlayRandomButton.width,
                                    FilteredList.y+(FilteredList.height/2), 2, 8)
        
        
        FilterButton = Button_Widget(self.root)
        FilterButton.add_widget('Filter', self.backend.complete_filter,
                              FilteredList, 222, 123)
        FilterButton.place_here(secondsButton.x+secondsButton.width, LessButton.y-LessButton.height/4, 0, 0)
        
        ClearButton = Button_Widget(self.root)
        ClearButton.add_widget('Clear', self.backend.clear_everything,
                              FilteredList, 222, 123)
        ClearButton.place_here(FilterButton.x+FilterButton.width/2, FilterButton.y-FilterButton.height/2, 0, 0)


        FilenameChangeInput = Textinput_Widget(self.root)
        FilenameChangeInput.add_widget(26, 1)
        FilenameChangeInput.place_here(EqualsButton.x-EqualsButton.width/2, EqualsButton.y+(EqualsButton.height/2),
                                       paddingy=10)
        
        renameButton = Button_Widget(self.root)
        renameButton.add_widget('Rename', self.backend.rename_file, 'NA', 'NA', 'NA',
                   multiargument=True, args=[FilenameChangeInput.inputboxes[0], FilteredList])
        renameButtonyPadding = 1
        renameButtonxPadding = 1
        renameButton.place_here(FilenameChangeInput.x+(FilenameChangeInput.width/2)+1,
                                 FilenameChangeInput.y-FilenameChangeInput.height/2,
                                 renameButtonxPadding, renameButtonyPadding)


        personUpdate = Button_Widget(self.root)
        personUpdate.add_widget('Update', self.backend.update_field,
                                   self.backend.desired_or_undesired_options[0], 123,
                                   222,multiargument=True,
                                   args=[personList.listboxess[0], FilteredList, 'People'])
        personUpdate.place_here(personListx+1,
                                personInclude.y+(personUpdate.height/2), 3, 4)
        
        persondeUpdate = Button_Widget(self.root)
        persondeUpdate.add_widget('DeUpdate', self.backend.deupdate_field,
                                   'NA', 'NA', 'NA',multiargument=True,
                                   args=[personList.listboxess[0], FilteredList, 'People'])
        persondeUpdate.place_here(personListx+1,
                                personUpdate.y+(persondeUpdate.height/2), 3, 4)


        genreUpdate = Button_Widget(self.root)
        genreUpdate.add_widget('Update', self.backend.update_field,
                                   self.backend.desired_or_undesired_options[0], 123,
                                   222,multiargument=True,
                                   args=[genreList.listboxess[0], FilteredList, 'Genres'])
        genreUpdate.place_here(genreListCenterX+genreList.width+1,
                                genreInclude.y+(genreUpdate.height/2), 3, 4)
        
        genredeUpdate = Button_Widget(self.root)
        genredeUpdate.add_widget('DeUpdate', self.backend.deupdate_field,
                                   'NA', 'NA', 'NA',multiargument=True,
                                   args=[genreList.listboxess[0], FilteredList, 'Genres'])
        genredeUpdate.place_here(genreListCenterX+genreList.width+1,
                                genreUpdate.y+(genredeUpdate.height/2), 3, 4)


        placeUpdate = Button_Widget(self.root)
        placeUpdate.add_widget('Update', self.backend.update_field,
                                   self.backend.desired_or_undesired_options[0], 123,
                                   222,multiargument=True,
                                   args=[placesList.listboxess[0], FilteredList, 'Places'])
        placeUpdate.place_here(placesListCenterX+placesList.width+1,
                                      placesInclude.y+(placeUpdate.height/2), 3, 4)
        
        placedeUpdate = Button_Widget(self.root)
        placedeUpdate.add_widget('DeUpdate', self.backend.deupdate_field,
                                   'NA', 'NA', 'NA',multiargument=True,
                                   args=[placesList.listboxess[0], FilteredList, 'Places'])
        placedeUpdate.place_here(placesListCenterX+placesList.width+1,
                                placeUpdate.y+(placedeUpdate.height/2), 3, 4)


        genreUpdate = Button_Widget(self.root)
        genreUpdate.add_widget('Update', self.backend.update_field,
                                   self.backend.desired_or_undesired_options[0], 123,
                                   222,multiargument=True,
                                   args=[genreList.listboxess[0], FilteredList, 'Genres'])
        genreUpdate.place_here(genreListCenterX+genreList.width+1,
                                genreInclude.y+(genreUpdate.height/2), 3, 4)


        AnimatedLabel = Label_Widget(self.root)
        AnimatedLabel.add_widget(self.backend.animated, 'Not', 'Used', w=len('False'))
        AnimatedLabel.place_here(ClearButton.x+(ClearButton.width/2),
                                 ClearButton.y-ClearButton.height*2, 0, 1)

        AnimatedToggle = Button_Widget(self.root)
        AnimatedToggle.add_widget('Animated', self.backend.set_selection,
                                   AnimatedLabel.labels[0], 'Not', 'Used')
        difference_in_height = abs(AnimatedToggle.height - AnimatedLabel.height)
        max_number_of_letters = max([len('False'), len('True'), len('')])
        AnimatedToggle.place_here(AnimatedLabel.x-AnimatedLabel.width/2-AnimatedToggle.width,
                                      AnimatedLabel.y-(difference_in_height/2)-(AnimatedToggle.height/2),
                                      -(max_number_of_letters+5), 4)

        
        RefreshButton = Button_Widget(self.root)
        RefreshButton.add_widget('Refresh', self.backend.refresh,
                                   multiargument=True,
                                   args=[personList, genreList, placesList, FilteredList])
        ycenter = int((AnimatedLabel.y+renameButton.y)/2)-RefreshButton.height/2
        RefreshButton.place_here(ClearButton.x+ClearButton.width/2, ycenter, 3, 0)

        
        DeleteButton = Button_Widget(self.root)
        DeleteButton.add_widget('Delete', self.backend.delete_file, FilteredList)
        DeleteButton.place_here(TrueRandomButton.x+TrueRandomButton.width,
                                    FilteredList.y+(FilteredList.height/2), 2, 8)


        FilenameSearchInput = Textinput_Widget(self.root)
        i = 27
        FilenameSearchInput.add_widget(i, 1)
        max_legnth = (FilenameChangeInput.width+renameButton.width+renameButtonxPadding)
        while FilenameSearchInput.width < max_legnth:
            i = i + 1
            FilenameSearchInput.remove_widget()
            FilenameSearchInput.add_widget(i, 1)
        FilenameSearchInput.place_here(EqualsButton.x-EqualsButton.width/2, renameButton.y+(renameButton.height/2),
                                       paddingy=10)
        
        SearchButton = Button_Widget(self.root)
        SearchButton.add_widget('Search', self.backend.search_and_filter,
                                   multiargument=True,
                                   args=[FilteredList, FilenameSearchInput])
        SearchButton.place_here(FilenameSearchInput.x+FilenameSearchInput.width/2,
                                FilenameSearchInput.y-FilenameSearchInput.height/2, 3, -2)

    def display_app(self):
        self.root.mainloop()
