import context
from graphql_codegen.graphql_model.graphql_enum import GraphQLEnum
from graphql_codegen.graphql_model.graphql_object import GraphQLObject
from graphql_codegen.graphql_model.graphql_field import GraphQLField
from graphql_codegen.graphql_model.graphql_type_adds import GraphQLTypeAdd
from graphql_codegen.converter import Converter
from graphql_codegen.pl_attributes_provider.kotlin_attributes_provider import \
    KotlinAttributeProvider
from graphql_codegen.pl_attributes_provider.swift_attributes_provider import \
    SwiftAttributeProvider


def test_enum():
    gr_enum = GraphQLEnum('enum_name', ['case1', 'case2'])
    kotlin_attribute_provider = KotlinAttributeProvider()
    converter = Converter(kotlin_attribute_provider)
    converted_enum = converter.convert_enum(gr_enum)
    assert converted_enum.enum_name == 'enum_name'
    assert converted_enum.cases == ['case1', 'case2']

    swift_attribute_provider = SwiftAttributeProvider()
    converter = Converter(swift_attribute_provider)
    convert_enum = converter.convert_enum(gr_enum)
    assert convert_enum.enum_name == 'enum_name'
    assert convert_enum.cases == ['case1', 'case2']


def test_object():
    gr_object = GraphQLObject('object_name', [
        GraphQLField('field_name', 'field_type', [GraphQLTypeAdd.OPTIONAL])])
    kotlin_attribute_provider = KotlinAttributeProvider()
    converter = Converter(kotlin_attribute_provider)
    converted_object = converter.convert_object(gr_object, [])
    assert converted_object.struct_name == 'object_name'
    assert converted_object.fields[0].field_name == 'field_name'
    assert converted_object.fields[0].field_type == 'field_type? = null'

    gr_object = GraphQLObject('object_name', [
        GraphQLField('field_name', 'field_type', [GraphQLTypeAdd.LIST])])
    swift_attribute_provider = SwiftAttributeProvider()
    converter = Converter(swift_attribute_provider)
    converted_object = converter.convert_object(gr_object, [])
    assert converted_object.struct_name == 'object_name'
    assert converted_object.fields[0].field_name == 'field_name'
    assert converted_object.fields[0].field_type == '[field_type]'
