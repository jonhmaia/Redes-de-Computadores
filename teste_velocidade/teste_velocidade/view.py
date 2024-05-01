# Em teste_velocidade/views.py
from django.shortcuts import render
import speedtest

def testar_velocidade_view(request):
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # Convertendo para megabits por segundo
    upload_speed = st.upload() / 10**6  # Convertendo para megabits por segundo
    context = {
        'download_speed': download_speed,
        'upload_speed': upload_speed
    }
    return render(request, 'teste_velocidade.html', context)
