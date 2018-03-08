from django.http import HttpResponse
from .models import Video
from django.views.generic import DetailView
from pustakalaya_apps.review_system.models import Review
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger

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

        #adding pagination to the review system

        # review system data extractions
        data_review = Review.objects.filter(content_id= self.object.pk,content_type='video',published=True)

        # adding pagination to the review system
        ##########################Review pagination add########################
        #print(len(data_review))
        length = len(data_review)
        number_per_page = 15
        if length > number_per_page:
            #print("inside pagination")
            # for pagination we have following code
            paginator = Paginator(data_review, number_per_page)
            page = request.GET.get('page')
            try:
                users = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                users = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 7777), deliver last page of results.
                users = paginator.page(paginator.num_pages)

            context["paginated_data"] = users

            ########################Review Pagination end########################
        if length > 0 and length <= number_per_page:
            context["data_review"] = data_review

        return self.render_to_response(context)
    template_name = "video/video_detail.html"
