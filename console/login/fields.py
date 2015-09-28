from django.forms import ModelChoiceField


class NameModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name

class CartypeModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.cartype