from django.shortcuts import render

# Create your views here.

import csv

# def csv_read(request):
#     filename="documents/Libro1.csv"
#     try:
#         file = open(filename)
#         #print(type(file))
#         csv_reader = csv.reader(file, delimiter=";")
#         #print(type(csv_reader))
#         for record in csv_reader:
#             #print(type(record))
#             #print(len(record))
#             print(record)
    
#         file.close()
#     except (IOError) as error:
#         print("Error en el archivo {}".format(error))
    
#     return render(request, 'csv.html')

def csv_read(request):
    filename="documents/Libro1.csv"
    try:
        with open(filename) as file:
            #print(type(file))
            csv_reader = csv.reader(file, delimiter=",")
            #print(type(csv_reader))
            for record in csv_reader:
                #print(type(record))
                #print(len(record))
                print(record)
    except (IOError) as error:
        print("Error en el archivo {}".format(error))
    
    return render(request, 'csv.html')

def csv_read_dict(request):
    filename="documents/Libro1.csv"
    try:
        file = open(filename, 'r')
        #print(type(file))
        csv_reader = csv.DictReader(file, delimiter=";")
        #print(type(csv_reader))
        for record in csv_reader:
            #print(type(record))
            #print(len(record))
            print(record)
    
        file.close()
    except (IOError) as error:
        print("Error en el archivo {}".format(error))
    
    return render(request, 'csv.html')

def csv_write(request):
    filename="documents/Libro2.csv"
    try:
        file = open(filename, 'w', newline="")
        #print(type(file))
        csv_writer = csv.writer(file, delimiter=";")
        # print(type(csv_writer))

        csv_writer.writerow(["Pelicula 1","Pelicula 2", "Pelicula 3"])
        csv_writer.writerow(["Avengers","Batman", "Superman"])
        csv_writer.writerow(["Avengers 3","Batman 2", "Otro"])
        csv_writer.writerow(["Avengers 4","Batman", "Spiderman"])

        file.close()
    except (IOError) as error:
        print("Error en el archivo {}".format(error))
    
    return render(request, 'csv.html')

def csv_write_dict(request):
    filename="documents/Libro2.csv"
    try:
        file = open(filename, 'w', newline="")
        #print(type(file))
        csv_writer = csv.DictWriter(file, delimiter=",", fieldnames=['name','surname'])
        # print(type(csv_writer))
        csv_writer.writeheader()
        csv_writer.writerow({ 'name': 'andres', 'surname': "cruz" })

        file.close()
    except (IOError) as error:
        print("Error en el archivo {}".format(error))
    
    return render(request, 'csv.html')