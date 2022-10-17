from django.shortcuts import render

def matematika(request):
    return render(request, 'matematika.html')

def sejarah(request):
    judul ="Sejarah Matematika Cina", "Sejarah Matematika Arab", "Sejarah Matematika India", "Sejarah Matematika Yunani", "Sejarah Matematika Babilonia"
    
    konteks ={
        'title': judul,
    }
    return render(request, 'sejarahmtk.html', konteks)

def ilmuwan(request):
    judul ="Thales", "Phytagoras", "Archimedes", "Al – Khawarizmi", "Euclides"

    konteks ={
        'title': judul,
    }
    return render(request, 'ilmuwanmtk.html', konteks)

def peluang(request):
    return render(request, 'peluang.html')

def biografi(request):
    return render(request, 'biografi.html')
