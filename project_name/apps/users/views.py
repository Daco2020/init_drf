from django.http import response, JsonResponse
from django.views import View


class ping(View):
    def get(self, request):
        return JsonResponse({"message": "pong"}, status=200)