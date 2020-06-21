from django.shortcuts import render
from curso.aperitivos.models import Video


videos = [
        Video(slug='motivacao', titulo='Recados: Motivação', vimeo_id='430007361'),
        Video(slug='atendimentos', titulo='Recados: Atendimentos', vimeo_id='430004576'),
    ]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = Video.objects.get(slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
