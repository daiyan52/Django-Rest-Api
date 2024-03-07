from django.core.serializers import serialize
from django.http import HttpResponse
import json
class SerializeMixin():
    def serialize(self,emp_data):
        json_data = serialize('json',emp_data)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
        return json_data

class HttpResponseMixin():
    def render_to_http_response(self, json_data):
        return HttpResponse(json_data, content_type='application/json')