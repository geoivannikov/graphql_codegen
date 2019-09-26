from graphql_codegen.pl_attributes_provider.swift_attributes_provider import \
    SwiftAttributeProvider
from graphql_codegen.pl_attributes_provider.kotlin_attributes_provider import \
    KotlinAttributeProvider
from graphql_codegen.languages_enum import Language


def graphql_types(pl_attributes_provider, graphql_type_name, enums):
    if graphql_type_name == 'String' or graphql_type_name == 'ID':
        return pl_attributes_provider.string_type()
    elif graphql_type_name == 'Boolean':
        return pl_attributes_provider.bool_type()
    elif graphql_type_name == 'Int':
        return pl_attributes_provider.int_type()
    elif graphql_type_name == 'Float':
        return pl_attributes_provider.double_type()
    elif graphql_type_name in [i.enum_name for i in enums]:
        return pl_attributes_provider.enum_type(graphql_type_name)
    else:
        return graphql_type_name


def get_attribute_provider(language):
    if language == Language.swift:
        return SwiftAttributeProvider()
    elif language == Language.kotlin:
        return KotlinAttributeProvider()
    else:
        raise NotImplementedError()
