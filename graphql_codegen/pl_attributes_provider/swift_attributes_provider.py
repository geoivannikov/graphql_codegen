from graphql_codegen.pl_attributes_provider.pl_attributes_provider import PLAttributesProvider

class SwiftAttributeProvider(PLAttributesProvider):
    def file_extension(self):
        return '.swift'

    def field_del(self):
        return '\n'
