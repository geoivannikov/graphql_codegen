from abc import ABCMeta
from abc import abstractmethod

class PLAttributesProvider(object):
    __metaclass__ = ABCMeta

    def file_extension(self):
        raise NotImplementedError()

    def field_del(self):
        return ',\n'

    def default_value(self):
        return ''

    def list_type(self, content):
        return '[{0}]'.format(content)

    def int_type(self):
        return 'Int'

    def double_type(self):
        return 'Double'

    def string_type(self):
        return 'String'

    def bool_type(self):
        return 'Bool'

    def enum_type(self, content):
        return content

    def convert_to_optional(self, content):
        return content + self.get_optional()

    def get_optional(self):
        return '?'

    def gen_enum(self):
        return True
