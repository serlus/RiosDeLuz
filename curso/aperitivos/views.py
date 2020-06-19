from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Recados: Motivação', 'vimeo_id': 430007361},
        'atendimentos': {'titulo': 'Recados: Atendimentos', 'vimeo_id': 430004576},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
