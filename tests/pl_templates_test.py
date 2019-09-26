import pytest
import context

from graphql_codegen.pl_attributes_provider.pl_attributes_provider import PLAttributesProvider
from graphql_codegen.pl_attributes_provider.kotlin_attributes_provider import KotlinAttributeProvider
from graphql_codegen.pl_attributes_provider.swift_attributes_provider import SwiftAttributeProvider

import graphql_codegen.pl_attributes_provider.pl_attributes_provider_helpers as ph

from graphql_codegen.pl_content.pl_struct_content.pl_struct import PLStruct
from graphql_codegen.pl_content.pl_struct_content.pl_struct_field import PLStructField
from graphql_codegen.pl_content.pl_enum_content.pl_enum import PLEnum

from graphql_codegen.pl_templates import PLTemplatesRender

def test_swift():
    structure_swift_template = 'struct {{strucure_name}} {\n{{fields}}\n}'
    field_swift_template = '    let {{field_name}}: {{type}}'
    swift_enum_template = 'enum {{enum_name}}: String {\n{{cases}}\n}'
    swift_case_template = '    case {{case_name}}'

    swift_attribute_provider = SwiftAttributeProvider()
    template = PLTemplatesRender(structure_swift_template, field_swift_template, swift_enum_template, swift_case_template, swift_attribute_provider)

    pl_struct = PLStruct('Struct', [PLStructField('field1', 'type1'), PLStructField('field2', 'type2')])
    expect = 'struct Struct {\n    let field1: type1\n    let field2: type2\n}'
    res = template.render_structure(pl_struct)

    assert res == expect

    pl_enum = PLEnum('Enum', ['case1', 'case2'])
    res = template.render_enum(pl_enum)
    expect = 'enum Enum: String {\n    case case1\n    case case2\n}'

    assert res == expect


def test_kotlin():
    structure_kotlin_template = 'data class {{strucure_name}} {\n{{fields}}\n}'
    field_kotlin_template = '    val {{field_name}}: {{type}}'
    kotlin_enum_template = 'enum {{enum_name}} {\n{{cases}}\n}'
    kotlin_case_template = '    {{case_name}}'

    kotlin_attribute_provider = KotlinAttributeProvider()
    template = PLTemplatesRender(structure_kotlin_template, field_kotlin_template, kotlin_enum_template, kotlin_case_template, kotlin_attribute_provider)

    pl_struct = PLStruct('Struct', [PLStructField('field1', 'type1'), PLStructField('field2', 'type2')])
    expect = 'data class Struct {\n    val field1: type1,\n    val field2: type2\n}'
    res = template.render_structure(pl_struct)

    assert res == expect

    pl_enum = PLEnum('Enum', ['case1', 'case2'])
    res = template.render_enum(pl_enum)
    expect = 'enum Enum {\n    case1,\n    case2\n}'

    assert res == expect

