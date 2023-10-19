import pandas as pd
import os
from pymediainfo import MediaInfo
import secrets
from tkinter import Label

class BackendFuncs:
    def __init__(self, root_path, the_csv,
                 peopletxt='People.txt', genretxt='Genres.txt', placetxt='Places.txt'):
        self.peopletxt = peopletxt
        self.genretxt = genretxt
        self.placetxt = placetxt
        self.root_path = root_path
        self.the_csv = the_csv
        self.list_of_people = self.get_list_of_contents(self.peopletxt)
        self.list_of_people.sort()
        self.list_of_genres = self.get_list_of_contents(self.genretxt)
        self.list_of_genres.sort()
        self.list_of_places = self.get_list_of_contents(self.placetxt)
        self.list_of_places.sort()
        self.update_csv(self.get_all_files_from_root(self.root_path), self.the_csv)
        self.dataframe = pd.read_csv(self.the_csv, delimiter=',', header=0, skip_blank_lines=True)
        if self.list_of_filez_from_dataframe(self.dataframe) == []:
            #csv file is empty
            self.update_csv(self.get_all_files_from_root(self.root_path), self.the_csv)
            self.dataframe = pd.read_csv(self.the_csv, delimiter=',', header=0, skip_blank_lines=True, na_values='')
        self.dataframe.replace(float('nan'), '')
        self.dataframe.replace(',nan,', '')
        self.dataframe.replace('NaN', '')
        self.dataframe.replace('NAN', '')
        self.dataframe.replace('; nan ;', '')
        self.dataframe.replace(',nan ;', '')
        self.dataframe.replace('; nan,', '')
        self.dataframe.to_csv(self.the_csv, index=False)
        self.filtereddataframe = pd.read_csv(self.the_csv, delimiter=',', header=0, skip_blank_lines=True, na_values='')
        self.filtereddataframe.replace(float('nan'), '')
        self.filtereddataframe.replace(',nan,', '')
        self.dataframe['Places'] = self.dataframe['Places'].astype(str)
        self.filtereddataframe['Places'] = self.filtereddataframe['Places'].astype(str)
        self.dataframe['Genres'] = self.dataframe['Genres'].astype(str)
        self.filtereddataframe['Genres'] = self.filtereddataframe['Genres'].astype(str)
        self.dataframe['People'] = self.dataframe['People'].astype(str)
        self.filtereddataframe['People'] = self.filtereddataframe['People'].astype(str)
        self.dataframe['Animated'] = self.dataframe['Animated'].astype(str)
        self.filtereddataframe['Animated'] = self.filtereddataframe['Animated'].astype(str)
        self.desired_genres = []
        self.desired_people = []
        self.undesired_genres = []
        self.undesired_people = []
        self.desired_places = []
        self.undesired_places = []
        self.selections = ['People', 'Places', 'Genre']
        self.selection = self.selections[self.generate_random_integer(0, len(self.selections)-1)]
        self.desired_or_undesired_options = ['Desired', 'Undesired']
        self.desired_or_undesired = self.desired_or_undesired_options[self.generate_random_integer(0, len(self.desired_or_undesired_options)-1)]#'Desired'
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.duration = (self.hours * 60 *60) + (self.minutes * 60) + self.seconds
        self.comparator = '>='
        self.animated = ''
        self.filename = ''

    def ave_num_char(self, heading):
        names = []
        for index in range(0, len(self.dataframe)):
            names.append(len(self.get_value_at_cell(index, heading, self.dataframe)))
        print(max(names), min(names), int((max(names)+min(names))/2))

    def add_people_to_search(self, listbox):
        if self.desired_or_undesired == self.desired_or_undesired_options[0]:
            self.get_multiple_selection(listbox, self.desired_people)
            print(self.desired_people)
        elif self.desired_or_undesired == self.desired_or_undesired_options[1]:
            self.get_multiple_selection(listbox, self.undesired_people)
            print(self.undesired_people)
        else:
            print('Was {} which is not valid.  It is now set to {}'.format(self.desired_or_undesired_options[0]))
            self.get_multiple_selection(listbox, self.desired_people)
            print(self.desired_people)
        listbox.selection_clear(0, 'end')

    def add_genres_to_search(self, listbox):
        if self.desired_or_undesired == self.desired_or_undesired_options[0]:
            self.get_multiple_selection(listbox, self.desired_genres)
            print(self.desired_genres)
        elif self.desired_or_undesired == self.desired_or_undesired_options[1]:
            self.get_multiple_selection(listbox, self.undesired_genres)
            print(self.undesired_genres)
        else:
            print('Was {} which is not valid.  It is now set to {}'.format(self.desired_or_undesired_options[0]))
            self.get_multiple_selection(listbox, self.desired_genres)
            print(self.desired_genres)
        listbox.selection_clear(0, 'end')

    def add_places_to_search(self, listbox):
        if self.desired_or_undesired == self.desired_or_undesired_options[0]:
            self.get_multiple_selection(listbox, self.desired_places)
            print(self.desired_places)
        elif self.desired_or_undesired == self.desired_or_undesired_options[1]:
            self.get_multiple_selection(listbox, self.undesired_places)
            print(self.undesired_places)
        else:
            print('Was {} which is not valid.  It is now set to {}'.format(self.desired_or_undesired_options[0]))
            self.get_multiple_selection(listbox, self.desired_places)
            print(self.desired_places)
        listbox.selection_clear(0, 'end')

    def remove_people_from_search(self, listbox):
        if self.desired_or_undesired == self.desired_or_undesired_options[0]:
            self.get_multiple_selections_removed(listbox, self.desired_people)
            print(self.desired_people)
        elif self.desired_or_undesired == self.desired_or_undesired_options[1]:
            self.get_multiple_selections_removed(listbox, self.undesired_people)
            print(self.undesired_people)
        else:
            print('Was {} which is not valid.  It is now set to {}'.format(self.desired_or_undesired_options[0]))
            self.get_multiple_selections_removed(listbox, self.desired_people)
            print(self.desired_people)
        listbox.selection_clear(0, 'end')

    def remove_genres_from_search(self, listbox):
        if self.desired_or_undesired == self.desired_or_undesired_options[0]:
            self.get_multiple_selections_removed(listbox, self.desired_genres)
            print(self.desired_genres)
        elif self.desired_or_undesired == self.desired_or_undesired_options[1]:
            self.get_multiple_selections_removed(listbox, self.undesired_genres)
            print(self.undesired_genres)
        else:
            print('Was {} which is not valid.  It is now set to {}'.format(self.desired_or_undesired_options[0]))
            self.get_multiple_selections_removed(listbox, self.desired_genres)
            print(self.desired_genres)
        listbox.selection_clear(0, 'end')

    def remove_places_from_search(self, listbox):
        if self.desired_or_undesired == self.desired_or_undesired_options[0]:
            self.get_multiple_selections_removed(listbox, self.desired_places)
            print(self.desired_places)
        elif self.desired_or_undesired == self.desired_or_undesired_options[1]:
            self.get_multiple_selections_removed(listbox, self.undesired_places)
            print(self.undesired_places)
        else:
            print('Was {} which is not valid.  It is now set to {}'.format(self.desired_or_undesired_options[0]))
            self.get_multiple_selections_removed(listbox, self.desired_places)
            print(self.desired_places)
        listbox.selection_clear(0, 'end')
    
    def get_multiple_selection(self, listbox, liste):
        for selection in listbox.curselection():
            if listbox.get(selection) not in liste:
                liste.append(listbox.get(selection))
        return liste
    
    def get_multiple_selections_removed(self, listbox, liste):
        for selection in listbox.curselection():
            if listbox.get(selection) in liste:
                liste.remove(listbox.get(selection))
        return liste

    def get_list_of_contents(self, filename):
        file = open(filename, 'r')
        contents = file.readlines()
        file.close()
        real_list = []
        for content in contents:
            real_list.append(content.replace('\n', '').strip())
        return real_list
    
    def set_selection(self, selection):
        if selection in self.selections:
            self.selection = selection
            print('{} is selected'.format(selection))
        elif type(selection) == type(Label()):
            if self.animated == '':
                self.animated = 'True'
            elif self.animated == 'True':
                self.animated = 'False'
            elif self.animated == 'False':
                self.animated = ''
            self.selection = selection
            print('{} is selected'.format(selection))
            selection.config(text=self.animated)
        else:
            print('{} is not allowed'.format(selection))
            self.selection = self.selections[0]

    def update_hours(self, inputbod):
        inp = inputbod.get(1.0, "end-1c")
        print(inp)
        try:
            inp = int(inp)
        except:
            print('{} is not a number'.format(inp))
            inp = 1
        self.hours = inp
        self.update_duration()

    def update_minutes(self, inputbod):
        inp = inputbod.get(1.0, "end-1c")
        print(inp)
        try:
            inp = int(inp)
        except:
            print('{} is not a number'.format(inp))
            inp = 1
        self.minutes = inp
        self.update_duration()

    def update_seconds(self, inputbod):
        inp = inputbod.get(1.0, "end-1c")
        print(inp)
        try:
            inp = int(inp)
        except:
            print('{} is not a number'.format(inp))
            inp = 1
        self.seconds = inp
        self.update_duration()

    def update_duration(self):
        self.duration = (self.hours * 60 *60) + (self.minutes * 60) + self.seconds

    def update_comparator(self, comparator):
        print(comparator)
        self.comparator = comparator

    def get_single_selection(self, box):
        try:
            try:
                listbox = box.listboxess[len(box.listboxess)-1]
                try:
                    item = listbox.get(listbox.curselection())
                except Exception as error:
                    print(error)
                    item = ''
            except:
                item = ''
        except Exception as error:
            print('Error:', error)
            index = self.generate_random_integer(0, len(self.dataframe))
            path = self.get_value_at_cell(index, 'Path', self.dataframe)
            name = self.get_value_at_cell(index, 'Filename', self.dataframe)
            item = os.path.join(path, name)
            print(item)
        return item
    
    def open_file(self, listbox):
        item = self.get_single_selection(listbox)
        if os.path.exists(item):
            print('Opening {}'.format(item))
            os.startfile(item)
        else:
            print('{} does not exist'.format(item))
            self.open_random_file(self.dataframe)

    def generate_random_integer(self, minimum, maximum):
        secretsGenerator = secrets.SystemRandom()
        return secretsGenerator.randint(minimum, maximum-1)
    
    def clear_everything(self, box):
        self.desired_genres = []
        self.desired_people = []
        self.undesired_genres = []
        self.undesired_people = []
        self.desired_places = []
        self.undesired_places = []
        self.animated = ''
        self.filename = ''
        self.hours = 0
        self.minutes = 0
        self.seconds = 0 #seconds
        self.duration = (self.hours * 60 *60) + (self.minutes * 60) + self.seconds
        self.comparator = '>='
        self.filter_dataframe(self.dataframe,self.animated,
                                                       self.desired_people, '', self.duration,
                                                       self.comparator, 's', self.desired_genres,
                                                       '', self.desired_places, '',
                                                       self.undesired_people, self.undesired_genres,
                                                       self.undesired_places)
        self.update_files_listbox(box)

    def update_field(self, listbox, files_listbox, heading):
        item = self.get_single_selection(files_listbox)
        absolute_path, file = os.path.split(item)
        for dataframe in [self.dataframe, self.filtereddataframe]:
            index = self.get_row_index(dataframe, file, absolute_path)
            known_things = self.get_value_at_cell(index, heading, dataframe)
            for index in listbox.curselection():
                new_thing = listbox.get(index)
                if not known_things.__contains__(new_thing):
                    if (known_things == '') or (known_things.lower() == 'nan'):
                        known_things = new_thing
                    else:
                        known_things = known_things + '; ' + new_thing
            known_things = known_things.replace('nan', '')
            known_things = known_things.replace('NAN', '')
            known_things = known_things.replace('NaN', '')
            known_things = known_things.replace(float('nan'), '')
            self.edit_dataframe(dataframe, file, absolute_path, heading, known_things)
        self.dataframe.to_csv(self.the_csv, index=False)
        listbox.selection_clear(0, 'end')

    def deupdate_field(self, listbox, files_listbox, heading):
        item = self.get_single_selection(files_listbox)
        absolute_path, file = os.path.split(item)
        for dataframe in [self.dataframe, self.filtereddataframe]:
            index = self.get_row_index(dataframe, file, absolute_path)
            known_things = self.get_value_at_cell(index, heading, dataframe)
            for index in listbox.curselection():
                thing_to_be_removed = listbox.get(index)
                if known_things.__contains__('; '+thing_to_be_removed):
                    known_things = known_things.replace('; '+thing_to_be_removed, '')
                elif known_things.__contains__(thing_to_be_removed+'; '):
                    known_things = known_things.replace(thing_to_be_removed+'; ', '')
                elif known_things.__contains__(thing_to_be_removed):
                    known_things = known_things.replace(thing_to_be_removed, '')
            known_things = known_things.replace('nan', '')
            known_things = known_things.replace('NAN', '')
            known_things = known_things.replace('NaN', '')
            known_things = known_things.replace('; ;', ';')
            known_things = known_things.replace(';;', ';')
            self.edit_dataframe(dataframe, file, absolute_path, heading, known_things)
        self.dataframe.to_csv(self.the_csv, index=False)
        listbox.selection_clear(0, 'end')
    
    def get_value_at_cell(self, rowindex, heading, frame):
        return frame.at[rowindex, heading]
    
    def open_random_file(self, frame):
        index = self.generate_random_integer(0, len(self.filtereddataframe))
        path = self.get_value_at_cell(index, 'Path', self.filtereddataframe)
        name = self.get_value_at_cell(index, 'Filename', self.filtereddataframe)
        item = os.path.join(path, name)
        print(item)
        if os.path.exists(item):
            os.startfile(item)
        else:
            print('{} does not exist.  Will open a different random item'.format(item))
            list_of_filez = self.get_all_files_from_root(self.root_path)
            index = self.generate_random_integer(0, len(list_of_filez))
            path = self.get_value_at_cell(index, 'Path', self.filtereddataframe)
            name = self.get_value_at_cell(index, 'Filename', self.filtereddataframe)
            item = os.path.join(path, name)
            os.startfile(item)
    
    def open_random_file_for_real(self, frame):
        index = self.generate_random_integer(0, len(self.dataframe))
        path = self.get_value_at_cell(index, 'Path', self.dataframe)
        name = self.get_value_at_cell(index, 'Filename', self.dataframe)
        item = os.path.join(path, name)
        print(item)
        if os.path.exists(item):
            os.startfile(item)
        else:
            print('{} does not exist.  Will open a different random file'.format(item))
            list_of_filez = self.get_all_files_from_root(self.root_path)
            index = self.generate_random_integer(0, len(list_of_filez))
            path = self.get_value_at_cell(index, 'Path', self.filtereddataframe)
            name = self.get_value_at_cell(index, 'Filename', self.filtereddataframe)
            item = os.path.join(path, name)
            os.startfile(item)
    
    def set_desire(self, selection):
        if selection in self.desired_or_undesired_options:
            self.desired_or_undesired = selection
            print('You are set to {}'.format(selection))
        else:
            print('{} is not allowed'.format(selection))
            self.desired_or_undesired = self.desired_or_undesired_options[0]

    def write2ANYfile(self, string, filename, option):
        string = str(string)
        logger = open(filename, option)
        logger.write(string)
        logger.close()

    def add_to_list(self, a_list, list_file, addition):
        if addition not in a_list:
            a_list.append(addition)
            self.write2ANYfile('\n'+addition, list_file, 'a')
            a_list.sort()
        return a_list

    def get_item_type(self, item):
        item = str(item)
        item = item.lower()
        if item.__contains__('temp'):
            return 'exit'
        elif item.endswith('.avi'):
            return 'video'
        elif item.endswith('.wmv'):
            return 'video'
        elif item.endswith('.WMV'):
            return 'video'
        elif item.endswith('.mp4'):
            return 'video'
        elif item.endswith('.mpeg'):
            return 'video'
        elif item.endswith('.mov'):
            return 'video'
        elif item.endswith('.mpg'):
            return 'video'
        elif item.endswith('.zip'):
            return 'exit'
        elif item.endswith('.rar'):
            return 'exit'
        elif item.endswith('.ini'):
            return 'exit'
        elif item.endswith('.txt'):
            return 'exit'
        elif item.endswith('.tiff'):
            return 'image'
        elif item.endswith('.tif'):
            return 'image'
        elif item.endswith('.jpeg'):
            return 'image'
        elif item.endswith('.png'):
            return 'image'
        elif item.endswith('.jpg'):
            return 'image'
        elif item.__contains__('.'):
            return 'exit'
        else:
            return 'folder'

    def get_all_files_from_root(self, root_path):
        filez = []
        for path, subdirs, files in os.walk(root_path):
            for name in files:
                if (self.get_item_type(name) == 'video') or (self.get_item_type(name) == 'image'):
                    filez.append(os.path.join(path, name))
                else:
                    pass
        return filez

    def write2file(self, string):
        string = str(string)
        filename = 'EricsGUI.txt'
        if(os.path.exists(filename)):
            pass
        else:
            logger = open(filename, 'w')
            logger.write('Debug Log\n')
            logger.close()
        logger = open(filename, 'a')
        print(string)
        logger.write(string + '\n')
        logger.close()

    def get_duration(self, a_file):
        if self.get_item_type(a_file) == 'video':
            try:
                clip_info = MediaInfo.parse(a_file)
                duration = (clip_info.tracks[0].duration) / 1000
                return duration
            except Exception as Error:
                self.write2file(Error)
                return 45510
        else:
            return 0
        
    def add_general_genres(self, genres, path_and_file):
        genres = str(genres)
        path_and_file = str(path_and_file)
        for _genre in self.list_of_genres:
            if _genre.__contains__('\n'):
                genre = _genre.replace('\n', '')
            else:
                genre = _genre
            if path_and_file.lower().__contains__(genre.lower()):
                if not genres.lower().__contains__(genre.lower()):
                    if genres == '':
                        genres = genre
                    else:
                        genres = genres + '; ' + genre
        return genres

    def update_dataframe(self, old_frame, the_path, filename, extension, dur):
        genre = ''
        genre = self.add_general_genres(genre, os.path.join(the_path, filename))
        people = '11037'
        if True:
            for star in self.list_of_people:
                star = star.replace('\n', '')
                person = star.lower().strip()
                if filename.lower().__contains__(person):
                    if people == '11037':
                        people = people + star
                    else:
                        if star.__contains__(' '):
                            first_name = star.split(' ')[0]
                        else:
                            first_name = star
                        if not (people.__contains__(first_name)):
                            people = people + '; ' + star
                        else:
                            if people.__contains__('11037' + first_name + '; '):
                                people = people.replace(first_name + '; ', star + '; ')
                            elif (people.__contains__('11037' + first_name)) and not (people.__contains__(' ')):
                                people = people.replace(first_name, star)
                            elif people.__contains__('; ' + first_name + ';'):
                                people = people.replace('; ' + first_name, '; ' + star)
                            elif people.__contains__('; ' + first_name):
                                people = people.replace('; ' + first_name, '; ' + star)
                            else:
                                people = people + '; ' + star
        people = people.replace('11037', '')
        if genre.lower().__contains__('3d CGI'.lower()):
            animation = True
        else:
            animation = ''
        update_dic = {
                        'Path': [the_path],
                        'Filename': [filename],
                        'Filetype': [extension],
                        'Animated': [animation],
                        'People': [people],
                        'Places': [''],
                        'Genres': [genre],
                        'Duration': [dur]
                        }
        new_df = pd.DataFrame(update_dic)
        dataframe = pd.concat([old_frame, new_df], ignore_index = True)
        print(os.path.join(the_path, filename))
        return dataframe
    
    def generic_update(self):
        for frame in [self.dataframe, self.filtereddataframe]:
            for rowindex in range(0, len(frame)):
                for head in ['People', 'Places', 'Genres']:
                    filename = self.get_value_at_cell(rowindex, 'Filename', frame)
                    path = self.get_value_at_cell(rowindex, 'Path', frame)
                    full_file_name = os.path.join(path, filename)
                    thing = self.get_value_at_cell(rowindex, head, frame)
                    if head == 'People':
                        liste = self.list_of_people
                    elif head == 'Places':
                        liste = self.list_of_places
                    elif head == 'Genres':
                        liste = self.list_of_genres
                    for element in liste:
                        if full_file_name.__contains__(element) and (not (thing.__contains__(element))):
                            if thing == '':
                                thing = element
                            else:
                                thing = thing + element
    
    def get_row_index(self, frame, filename, abs_path):
        print(filename, 'file')
        print(filename, 'path')
        row_index = frame[(frame['Filename'] == filename) & (frame['Path'] == abs_path)].index[0]
        return row_index

    def edit_dataframe(self, dataframe_to_be_updated, filename, abs_path, heading, cell_value):
        row_index = dataframe_to_be_updated[(dataframe_to_be_updated['Filename'] == filename) & (dataframe_to_be_updated['Path'] == abs_path)].index[0]
        dataframe_to_be_updated.at[row_index, heading] = cell_value
        return dataframe_to_be_updated
    
    def rename_file(self, textbox, listbox):
        new_name = str(textbox.get(1.0, "end-1c")).replace('\n', '').strip()
        item = self.get_single_selection(listbox)
        absolute_path, file = os.path.split(item)
        if not new_name.__contains__('.'):
            extension = file.split('.')[1]
            new_name = new_name + '.' + extension
        try:
            os.rename(item, os.path.join(absolute_path, new_name))
            self.edit_dataframe(self.dataframe, file, absolute_path, 'Filename', new_name)
            self.edit_dataframe(self.filtereddataframe, file, absolute_path, 'Filename', new_name)
            self.update_files_listbox(listbox)
            self.dataframe.to_csv(self.the_csv, index=False)
        except:
            print('Can not rename file {}'.format(os.rename(item, os.path.join(absolute_path, new_name))))

    def refresh(self, person_widget, genres_widget, place_widget, filtered_widget):
        self.people = self.get_list_of_contents(self.peopletxt)
        self.list_of_people.sort()
        self.list_of_genres = self.get_list_of_contents(self.genretxt)
        self.list_of_genres.sort()
        self.list_of_places = self.get_list_of_contents(self.placetxt)
        self.list_of_places.sort()
        self.update_csv(self.get_all_files_from_root(self.root_path), self.the_csv)
        self.dataframe = pd.read_csv(self.the_csv, delimiter=',', header=0, skip_blank_lines=True)
        self.dataframe.replace(float('nan'), '')
        self.dataframe.replace(',nan,', '')
        self.dataframe.replace('NaN', '')
        self.dataframe.replace('NAN', '')
        self.dataframe.replace('; nan ;', '')
        self.dataframe.replace(',nan ;', '')
        self.dataframe.replace('; nan,', '')
        self.dataframe.to_csv(self.the_csv, index=False)
        self.filtereddataframe = pd.read_csv(self.the_csv, delimiter=',', header=0, skip_blank_lines=True, na_values='')
        self.filtereddataframe.replace(float('nan'), '')
        self.filtereddataframe.replace(',nan,', '')
        self.dataframe['Places'] = self.dataframe['Places'].astype(str)
        self.filtereddataframe['Places'] = self.filtereddataframe['Places'].astype(str)
        self.dataframe['Genres'] = self.dataframe['Genres'].astype(str)
        self.filtereddataframe['Genres'] = self.filtereddataframe['Genres'].astype(str)
        self.dataframe['People'] = self.dataframe['People'].astype(str)
        self.filtereddataframe['People'] = self.filtereddataframe['People'].astype(str)
        self.dataframe['Animated'] = self.dataframe['Animated'].astype(str)
        self.filtereddataframe['Animated'] = self.filtereddataframe['Animated'].astype(str)
        self.desired_genres = []
        self.desired_people = []
        self.undesired_genres = []
        self.undesired_people = []
        self.desired_places = []
        self.undesired_places = []
        self.selections = ['People', 'Places', 'Genre']
        self.selection = self.selections[self.generate_random_integer(0, len(self.selections)-1)]
        self.desired_or_undesired_options = ['Desired', 'Undesired']
        self.desired_or_undesired = self.desired_or_undesired_options[self.generate_random_integer(0, len(self.desired_or_undesired_options)-1)]#'Desired'
        self.hours = 0
        self.minutes = 0
        self.seconds = 0 #seconds
        self.duration = (self.hours * 60 *60) + (self.minutes * 60) + self.seconds
        self.comparator = '>='
        self.animated = ''
        self.filename = ''
        self.update_generic_listbox(person_widget, self.list_of_people)
        self.update_generic_listbox(genres_widget, self.list_of_genres)
        self.update_generic_listbox(place_widget, self.list_of_places)
        self.update_files_listbox(filtered_widget)

    def delete_file(self, listbox_widget):
        item = self.get_single_selection(listbox_widget)
        if os.path.exists(item):
            print(item)
            os.remove(item)
        else:
            print('{} DNE'.format(item))
        absolute_path, file = os.path.split(item)
        print(absolute_path, file)
        self.dataframe = self.remove_row_from_dataframe(self.dataframe, file, absolute_path)
        self.filtereddataframe = self.remove_row_from_dataframe(self.filtereddataframe, file, absolute_path)
        self.update_files_listbox(listbox_widget)
        self.dataframe.to_csv(self.the_csv, index=False)

    def update_csv(self, list_of_files, csv_file):
        #list_of_files must have full abolute path
        dataframe = pd.read_csv(csv_file, delimiter=',', header=0, skip_blank_lines=True)
        list_of_files_in_dataframe = self.list_from_dataframe(dataframe, 'Filename')
        print('Updating...')
        for file_with_absolute_path in list_of_files:
            if os.path.exists(file_with_absolute_path):#checking if it exits
                absolute_path, file = os.path.split(file_with_absolute_path)
                #check if file is already in the dataframe
                if not (file in list_of_files_in_dataframe):
                    #Add to dataframe
                    duration = self.get_duration(file_with_absolute_path) #in seconds
                    file_type = file_with_absolute_path.split('.')[1]
                    dataframe = self.update_dataframe(dataframe, absolute_path, file, file_type, duration)
                else:
                    #Check if path is the same
                    filtered_df = self.filter_dataframe(dataframe, Filename=file, Path=absolute_path)
                    path_filtered_list = self.list_from_dataframe(filtered_df, 'Path')
                    if len(path_filtered_list) == 0:
                        duration = self.get_duration(file_with_absolute_path) #in seconds
                        file_type = file_with_absolute_path.split('.')[1]
                        dataframe = self.update_dataframe(dataframe, absolute_path, file, file_type, duration)
                    elif len(path_filtered_list) == 1:
                        #Check if duration is the same
                        duration = self.get_duration(file_with_absolute_path) #in seconds
                        duration_filtered_list = self.list_from_dataframe(filtered_df, 'Duration')
                        if abs(duration - duration_filtered_list[0]) < 1:
                            pass
                        else:
                            dataframe = self.edit_dataframe(dataframe, file, absolute_path, 'Duration', duration)
                    else:
                        #There are multiple files in the dataframe with the same name and path
                        #Windows does not allow that so there must be a duplicate
                        #Might be better to just start from scratch on this one
                        dataframe = self.remove_row_from_dataframe(dataframe, file, absolute_path)
                        duration = self.get_duration(file_with_absolute_path) #in seconds
                        file_type = file_with_absolute_path.split('.')[1]
                        dataframe = self.update_dataframe(dataframe, absolute_path, file, file_type, duration)
        print('Updating is complete!!!')
        self.dataframe = dataframe
        self.dataframe.to_csv(csv_file, index=False)

    def remove_row_from_dataframe(self, dataframe_to_be_updated, filename, abs_path):
        row_indexes = dataframe_to_be_updated[(dataframe_to_be_updated['Filename'] == filename) & (dataframe_to_be_updated['Path'] == abs_path)].index.tolist()
        for row in row_indexes:
            dataframe_to_be_updated = dataframe_to_be_updated.drop(row)
        #self.dataframe = dataframe_to_be_updated
        return dataframe_to_be_updated

    def remove_nonexistent_files(self, frame, csv_file=''):
        paths = []
        files = []
        for row in range(0, len(frame)):
            filename = frame.at[row, 'Filename']
            file_path = frame.at[row, 'Path']
            full_name = os.path.join(file_path, filename)
            if not os.path.exists(full_name):
                paths.append(file_path)
                files.append(filename)
                print(full_name)
        for i in range(0, len(paths)):
            frame = self.remove_row_from_dataframe(frame, files[i], paths[i])
            self.dataframe = frame
        if not csv_file == '':
            frame.to_csv(csv_file, index=False)
        self.dataframe = frame

    def update_files_listbox(self, box):
        originalx = box.x
        originaly = box.y
        #Empty listbox
        box.remove_everything()
        #Update listbox
        box.populate_box(box.listboxess[len(box.listboxess)-1], self.list_of_filez_from_dataframe(self.filtereddataframe))
        box.listboxess[len(box.listboxess)-1].place(
            x = originalx,
            anchor = 'center',
            y = originaly
        )

    def update_generic_listbox(self, box_widget, liste):
        box = box_widget
        originalx = box.x
        originaly = box.y
        #Empty listbox
        box.remove_everything()
        #Update listbox
        box.populate_box(box.listboxess[len(box.listboxess)-1], liste)
        box.listboxess[len(box.listboxess)-1].place(
            x = originalx,
            anchor = 'center',
            y = originaly
        )

    def complete_filter(self, box):
        #filter dataframe
        self.filter_dataframe(self.dataframe, self.animated, self.desired_people, 
                                 self.filename, self.duration,
                              self.comparator, 's', self.desired_genres, '', self.desired_places,
                              '', self.undesired_people, self.undesired_genres,
                              self.undesired_places)
        self.update_files_listbox(box)

    def search_and_filter(self, box_widget, search_widget):
        self.filename = str(search_widget.inputboxes[0].get(1.0, "end-1c"))
        #filter dataframe
        self.filter_dataframe(self.dataframe, self.animated, self.desired_people, 
                                 self.filename, self.duration,
                              self.comparator, 's', self.desired_genres, '', self.desired_places,
                              '', self.undesired_people, self.undesired_genres,
                              self.undesired_places)
        self.update_files_listbox(box_widget)

    def filter_dataframe(self, dataframe, Animated='', People='', Filename='',
                         Duration='', Duration_Comparer='>', Duration_Unit='m',
                         Genres='', extention='', Places='', Path='', undersired_people='', undersired_genres='',
                         undersired_places=''):
        Headings = dataframe.columns.tolist()
        init = dataframe.filter(items=Headings)

        #Windows reports duration as seconds;  Must convert given to seconds
        Duration_Unit = Duration_Unit.lower()
        if (Duration_Unit == 's') or (Duration_Unit == 'seconds') or (Duration_Unit == 'second') or (Duration_Unit == 'sec') or (Duration_Unit == 'secs'):
            Duration = Duration
        elif (Duration_Unit == 'm') or (Duration_Unit == 'minutes') or (Duration_Unit == 'minute') or (Duration_Unit == 'min') or (Duration_Unit == 'mins'):
            Duration = Duration * 60
        
        if not (Path==''):
            filtered_dataframe = init.loc[init['Path'] == Path]
        else:
            filtered_dataframe = init
        
        if not (extention==''):
            filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Filetype'] == Animated]
        else:
            filtered_dataframe = filtered_dataframe
        
        if not (Animated==''):
            filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Animated'] == Animated]
        else:
            filtered_dataframe = filtered_dataframe

        if not (People==''): #this is a list
            for Person in People:
                filtered_dataframe = filtered_dataframe[filtered_dataframe['People'].str.contains(Person, na=False)]
        else:
            filtered_dataframe = filtered_dataframe

        if not (undersired_people==''): #this is a list
            for Person in undersired_people:
                filtered_dataframe = filtered_dataframe[~filtered_dataframe['People'].str.contains(Person, na=False)]
        else:
            filtered_dataframe = filtered_dataframe

        if not (Genres==''): #this is a list
            for Genre in Genres:
                filtered_dataframe = filtered_dataframe[filtered_dataframe['Genres'].str.contains(Genre, na=False)]
        else:
            filtered_dataframe = filtered_dataframe

        if not (undersired_genres==''): #this is a list
            for genre in undersired_genres:
                filtered_dataframe = filtered_dataframe[~filtered_dataframe['Genres'].str.contains(genre, na=False)]
        else:
            filtered_dataframe = filtered_dataframe

        if not (Places==''): #this is a list
            for Place in Places:
                filtered_dataframe = filtered_dataframe[filtered_dataframe['Places'].str.contains(Place, na=False)]
        else:
            filtered_dataframe = filtered_dataframe

        if not (undersired_places==''): #this is a list
            for Place in undersired_places:
                filtered_dataframe = filtered_dataframe[~filtered_dataframe['Places'].str.contains(Place, na=False)]
        else:
            filtered_dataframe = filtered_dataframe

        if not (Filename==''):
            filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Filename'].str.contains(Filename, na=False, case=False)]
        else:
            filtered_dataframe = filtered_dataframe

        if not (Duration==''):
            if Duration_Comparer == '=':
                filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Duration'] == Duration]
            elif Duration_Comparer == '<':
                filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Duration'] < Duration]
            elif Duration_Comparer == '>':
                filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Duration'] > Duration]
            elif Duration_Comparer == '<=':
                filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Duration'] <= Duration]
            elif Duration_Comparer == '>=':
                filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Duration'] >= Duration]
            else:
                filtered_dataframe = filtered_dataframe.loc[filtered_dataframe['Duration'] < 277353]
        else:
            filtered_dataframe = filtered_dataframe
        self.filtereddataframe = filtered_dataframe.reset_index(drop=True)
        return filtered_dataframe

    def list_from_dataframe(self, dataframe, Heading):
        Headings = dataframe.columns.tolist()
        init = dataframe.filter(items=Headings)
        init = init[Heading]
        return init.values.tolist()

    def list_of_filez_from_dataframe(self, dataframe):
        paths = self.list_from_dataframe(dataframe, 'Path')
        names = self.list_from_dataframe(dataframe, 'Filename')
        filez = []
        for i in range(0, len(paths)):
            filez.append(os.path.join(paths[i], names[i]))
        filez.sort()
        return filez