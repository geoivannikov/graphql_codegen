import context

from graphql_codegen.pl_attributes_provider.pl_attributes_provider import PLAttributesProvider
from graphql_codegen.pl_attributes_provider.kotlin_attributes_provider import KotlinAttributeProvider
from graphql_codegen.pl_attributes_provider.swift_attributes_provider import SwiftAttributeProvider

import graphql_codegen.pl_attributes_provider.pl_attributes_provider_helpers as ph

def test_kotlin():
    kotlin_attribute_provider = KotlinAttributeProvider()
    assert ph.get_bool_type(kotlin_attribute_provider) == 'Boolean'
    assert ph.get_default_value(kotlin_attribute_provider) == ' = null'
    assert ph.get_double_type(kotlin_attribute_provider) == 'String'
    assert ph.get_enum_type(kotlin_attribute_provider, 'EnumType') == 'String'
    assert ph.get_field_del(kotlin_attribute_provider) == ',\n'
    assert ph.get_file_extension(kotlin_attribute_provider) == '.kt'
    assert ph.get_gen_enum(kotlin_attribute_provider) == False
    assert ph.get_int_type(kotlin_attribute_provider) == 'Int'
    assert ph.get_list_type(kotlin_attribute_provider, 'Int') == 'List<Int>'
    assert ph.get_string_type(kotlin_attribute_provider) == 'String'


def test_swift():
    swift_attribute_provider = SwiftAttributeProvider()
    assert ph.get_bool_type(swift_attribute_provider) == 'Bool'
    assert ph.get_default_value(swift_attribute_provider) == ''
    assert ph.get_double_type(swift_attribute_provider) == 'Double'
    assert ph.get_enum_type(swift_attribute_provider, 'EnumType') == 'EnumType'
    assert ph.get_field_del(swift_attribute_provider) == '\n'
    assert ph.get_file_extension(swift_attribute_provider) == '.swift'
    assert ph.get_gen_enum(swift_attribute_provider) == True
    assert ph.get_int_type(swift_attribute_provider) == 'Int'
    assert ph.get_list_type(swift_attribute_provider, 'Int') == '[Int]'
    assert ph.get_string_type(swift_attribute_provider) == 'String'