from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

@require_http_methods(["POST"])
@csrf_exempt
def message(request):
	event = json.loads(request.body)
	if event["type"] == "MESSAGE":
		return JsonResponse({"text": event["message"]["argumentText"]})
