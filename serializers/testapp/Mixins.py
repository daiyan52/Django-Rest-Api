from django.core.serializers import serialize
import json
class SerializeMixin(object):
    def serialize(self,stu_data):
        json_data = serialize('json',stu_data)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            stu_data = obj['fields']
            final_list.append(stu_data)
        json_data = json.dumps(final_list)
        return json_data