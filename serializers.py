from rest_framework import serializers

class DynamicFieldsSerializerMixin(object):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        if fields and exclude:
            raise Exception(
                "You can't enable fields AND exclude at the same time"
            )

        super(self.__class__, self).__init__(*args, **kwargs)

        if fields is not None:
            map(self.fields.pop, set(fields).symmetric_difference(self.fields.keys())

        elif exclude is not None:
            map(self.fields.pop, exclude)

class DynamicFieldsModelSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    pass
    
class DynamicFieldsHyperlinkedModelSerializer(DynamicFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):
    pass
