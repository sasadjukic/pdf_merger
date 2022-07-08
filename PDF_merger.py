
from PyPDF2 import PdfFileWriter, PdfFileMerger
from pathlib import Path
import os 

directory = (
    Path.home()
)

pdf_merger = PdfFileMerger()

def search_for_PDF(file, path) -> str:

    for root, dirs, files in os.walk(path):
        if file in files:
            return os.path.join(root, file)

def append_PDF(f1, f2) -> None:
    
    pdf_merger.append(str(f1))
    pdf_merger.append(str(f2))

    with open('append_merger.pdf', 'wb') as a_merger:
        pdf_merger.write(a_merger)

def custom_merge_PDF(f1, f2, page) -> None:
    
    pdf_merger.append(str(f1))
    pdf_merger.merge(page, str(f2))

    with open('custom_merger.pdf', 'wb') as c_merger:
        pdf_merger.write(c_merger)

def main():

    while True:
        f1 = input('Enter file one: ')
        file_one = search_for_PDF(f1, directory)
        if file_one != None:
            f2 = input('Enter file to append to file one: ')
            file_two = search_for_PDF(f2, directory)
            if file_two != None:
                decision = input('Append second file to the end of the first file or at specific page?[E/S]: ').upper()

                if decision == 'E':
                    append_PDF(file_one, file_two)
                    break
                elif decision == 'S':
                    page = int(input(f'At what page of {f1} do you want to insert {f2}?: '))
                    custom_merge_PDF(file_one, file_two, page)
                    break
                else:
                    print('This choice not supported')
            else:
                print('File not found')
                continue
        else:
            print('File not found')
            continue

        

if __name__ == '__main__':
    main()




