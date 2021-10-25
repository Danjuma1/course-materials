def handle_uploaded_file(f):  
    with open('course_material/file/materials/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  