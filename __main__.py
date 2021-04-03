#!/usr/bin/env python
import sys
from datetime import datetime
import os
from os.path import expanduser

home = expanduser('~')
NoteLocation = os.path.join(home,'notes')
quickNoteLocation = os.path.join(NoteLocation,'quickNotes')

def dateOrTime(value):
    rawTime = datetime.now()
    if value == 'time':
        time = rawTime.strftime('%I:%M%p')
        return time
    elif value == 'date':
        date = rawTime.strftime('%d-%B-%Y')
        return date

def main(argv):
    try:
        if argv[0] == '-l' or argv[0] == '--list':
            for num, folders in enumerate(os.listdir(NoteLocation)):
                print('{} ------- {}'.format(num,folders))
            openFolder = int(input(': '))
            currentLocation = os.path.join(NoteLocation,os.listdir(NoteLocation)[openFolder])
            print(os.listdir(NoteLocation)[openFolder])
            notesInFile = len(os.listdir(currentLocation))
            print('{} NOTES IN THIS FOLDER.'.format(notesInFile)) 
            for num, file in enumerate(os.listdir(currentLocation)):
                print('{} ------- {}'.format(num,file))
            openNote = int(input(': '))
            print(currentLocation)
            currentLocation = (os.path.join(NoteLocation, os.listdir(NoteLocation)[openFolder], os.listdir(currentLocation)[openNote]))
            note = open(currentLocation, 'r')
            notevar = note.read()
            print (notevar)
            note.close()

        elif argv[0] == '-h' or argv[0] == '--help':
            print('\nUsage: note [options]')
            print('Alternative Usage: note [NOTE SECTION]\n')
            print('note is a simple note taking comand. Notes can be sorted using folders and time. It can be used as an a daily joural.\n')
            print('Commonly used commands:')
            print('-l, --list     -  list is used to list all the folders and notes within the users directory.')
            print('-v, --version  -  print program version')
            print('')

        elif argv[0] == '-v' or argv[0] == '--version':
            print('note alpha 1 (amd64)')

        else:
            print(argv)
            fileLocation = ('{}/{}'.format(quickNoteLocation, dateOrTime('time')))
            print(fileLocation)
            newNote = open(fileLocation, 'a+')
            newNote.write(' '.join(argv))
            newNote.close()
    except IOError:
        os.makedirs(quickNoteLocation)

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except IndexError:
        print('note: missing NOTE.\n')
        print('try "note HELLO WORLD!"')