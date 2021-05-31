#!/usr/bin/env python
import sys
from datetime import datetime
import os
from os.path import expanduser

home = expanduser('~')
NoteLocation = os.path.join(home,'notes')
quickNoteLocation = os.path.join(NoteLocation,'quickNotes')

def clearConsole():
    os.system('clear')
    return

def dateOrTime(value):
    rawTime = datetime.now()
    if value == 'time':
        time = rawTime.strftime('%I:%M %p')
        return time
    elif value == 'date':
        date = rawTime.strftime('%d-%B-%Y')
        return date


def printNote(noteLocation):
    print('\nNote Location: {}\n'.format(noteLocation))
    note = open(noteLocation, 'r')
    notevar = note.read()
    print (notevar)
    note.close()


def main(argv):
    clearConsole()
    try:
        if argv[0] == '-l' or argv[0] == '--list':
            print('\nIndex \t Folder Name')
            for num, folders in enumerate(os.listdir(NoteLocation)):
                print('{} \t {}'.format(num,folders))
            openFolder = int(input('\n: '))
            clearConsole()
            currentLocation = os.path.join(NoteLocation,os.listdir(NoteLocation)[openFolder])
            print('\nCurrent Location: {}'.format(currentLocation))
            notesInFile = len(os.listdir(currentLocation))
            print('\n{} Note(s) In This Folder.'.format(notesInFile))
            print('\nIndex \t Date Created')
            for num, file in enumerate(os.listdir(currentLocation)):
                print('{} \t {}'.format(num,file))
            openNote = int(input('\n: '))
            clearConsole()
            currentLocation = (os.path.join(NoteLocation, os.listdir(NoteLocation)[openFolder], os.listdir(currentLocation)[openNote]))
            printNote(currentLocation)

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
            fileLocation = ('{}/{}'.format(quickNoteLocation, dateOrTime('date')))
            try:
                newNote = open(fileLocation, 'a+')
            except:
                os.makedirs(quickNoteLocation)
            fileLocation = ('{}/{}'.format(quickNoteLocation, dateOrTime('date')))
            note = '{}:\t{}\n'.format(dateOrTime('time') ,' '.join(argv))
            newNote = open(fileLocation, 'a+')
            newNote.write(note)
            newNote.close()
            print('~Todays Notes~')
            printNote(fileLocation)
    except IOError:
        print("ERROR")
        
if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except IndexError:
        print('note: missing NOTE.\n')
        print('try "note HELLO WORLD!"')
