from django.template import TemplateDoesNotExist
from django_mobile.loader import Loader as MobileLoader

class Loader(MobileLoader):

    def load_template_source(self, template_name, template_dirs=None):
        template_name = self.prepare_template_name(template_name)
        for loader in self.template_source_loaders:
            try:
                return loader.load_template_source(template_name, template_dirs)
            except TemplateDoesNotExist:
                pass
        raise TemplateDoesNotExist("Tried %s" % template_name)
