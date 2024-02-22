from django.shortcuts import render
from core.models import Categories, Sentences
from django.views.decorators.csrf import csrf_exempt
from core.forms import SentenceForm
from django.http import JsonResponse

# from django.core.cache import cache
from django.conf import settings
from django.http import StreamingHttpResponse
from core.tasks import download_data, do_sentiment_analysis
from rest_framework.views import APIView

import json


def dashboard(request):
    categories = Categories.objects.all()
    category_selected = request.GET.get("category", None)
    sentences = None
    form = SentenceForm()
    taskid = 0

    if category_selected:
        sentences = Sentences.objects.filter(category__name=category_selected).order_by(
            "-id"
        )

    if request.method == "POST":
        new_sentence = request.POST.get("text", None)
        # category = Categories.objects.get(name=category_selected)
        # sentence_id = Sentences.objects.create(category=category, text=new_sentence)
        # sentence_id = sentence_id.id
        task = do_sentiment_analysis.apply_async(args=[new_sentence])
        taskid = task.id
    context = {
        "categories": categories if len(categories) != 0 else None,
        "category_selected": category_selected,
        "sentences": sentences,
        "form": form,
        "sen_taskid": taskid,
    }
    return render(request, "dashboard.html", context)


def fetch_data(category):
    queryset = Sentences.objects.filter(category__name=category).select_related(
        "category"
    )
    queryset_values = list(queryset.values())
    return queryset_values


@csrf_exempt
def download(request):
    if request.method == "POST":
        category = json.load(request)["category"]
        print("DATA recieved-----", category)

        queryset_values = fetch_data(category)

        task = download_data.apply_async(args=[queryset_values])
        taskid = task.id
        file_path = settings.MEDIA_ROOT + f"downloads/"
        file_name = f"{taskid}.xlsx"

        return JsonResponse(
            {"taskid": task.id, "file_path": file_path, "file_name": file_name}
        )


class DownloadFileViews(APIView):

    def get(self, request, taskid):
        print("TASK--ID:", taskid)
        file_path = settings.MEDIA_ROOT + f"downloads/{taskid}.xlsx"
        try:
            response = StreamingHttpResponse(
                self.generate_excel_file(file_path),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        except Exception as e:
            print("---------------exception", e)
        response["Content-Disposition"] = f"attachment; filename={taskid}.xlsx"
        return response

    def generate_excel_file(self, file_path):

        # Open the temporary file as a stream
        with open(file_path, "rb") as f:
            while True:
                data = f.read(8192)
                if not data:
                    break
                yield data
