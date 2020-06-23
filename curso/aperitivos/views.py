from django.shortcuts import get_object_or_404, render
from curso.aperitivos.models import Video


videos = [
        Video(slug='motivacao', titulo='Recados: Motivação', vimeo_id='430007361'),
        Video(slug='atendimentos', titulo='Recados: Atendimentos', vimeo_id='430004576'),
    ]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
