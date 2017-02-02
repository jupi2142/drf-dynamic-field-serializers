from rest_framework import serializers


class DynamicFieldsSerializerMixin(object):
    def __init__(self, *args, **kwargs):
        fields = set(kwargs.pop('fields', {}))
        exclude = set(kwargs.pop('exclude', {}))

        if fields and exclude:
            raise Exception(
                "You can't enable 'fields' AND 'exclude' at the same time"
            )

        super(self.__class__, self).__init__(*args, **kwargs)
        current_fields = self.fields.keys()
        fields_to_remove = exclude or fields.symmetric_difference(current_fields)
        list(map(self.fields.pop, fields_to_remove))

        
class DynamicFieldsModelSerializer(DynamicFieldsSerializerMixin,
                                   serializers.ModelSerializer):
    pass
    
    
class DynamicFieldsHyperlinkedModelSerializer(DynamicFieldsSerializerMixin,
                                              serializers.HyperlinkedModelSerializer):
    pass
