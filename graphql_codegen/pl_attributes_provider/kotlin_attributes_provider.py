from graphql_codegen.pl_attributes_provider.pl_attributes_provider import PLAttributesProvider

class KotlinAttributeProvider(PLAttributesProvider):
    def file_extension(self):
        return '.kt'

    def default_value(self):
        return ' = null'

    def list_type(self, content):
        return 'List<{0}>'.format(content)

    def double_type(self):
        return 'String'

    def bool_type(self):
        return 'Boolean'

    def enum_type(self, content):
        return 'String'

    def gen_enum(self):
        return False
