from django.http import HttpResponse
from .models import Video
from django.views.generic import DetailView
from pustakalaya_apps.review_system.models import Review

from .search import VideoSearch


def videos(request):
    # search all video
    # bs = VideoSearch()

    # search with query
    # bs = VideoSearch(query="video")

    # search with the query and selected filters
    filters = {
        'keywords': "hamro"
    }

    bs = VideoSearch(query="video", filters={'keywords': "hamro videos"})

    response = bs.execute()
    # for facets in response.facets:
    #     print(facets)
    # print(response.facets)


    # access hits and other attributes as usual
    print(response.hits.total, 'hits total')
    for hit in response:
        print(hit.meta.score, hit.title)
    #
    for (tag, count, selected) in response.facets.keywords:
        print(tag, ' (SELECTED):' if selected else ':', count)

    for (tag, count, selected) in response.facets.languages:
        print(tag, ' (SELECTED):' if selected else ':', count)

    for (month, count, selected) in response.facets.year_of_available:
        print(month.strftime('%B %Y'), ' (SELECTED):' if selected else ':', count)

    return HttpResponse("Hello world")


class VideoDetailView(DetailView):
    model = Video
    def get(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        # review system data extractions
        data_review = Review.objects.filter(content_id= self.object.pk,content_type='video',published=True)
        context["data_review"]= data_review
        return self.render_to_response(context)
    template_name = "video/video_detail.html"
