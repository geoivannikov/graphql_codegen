from graphql_codegen.graphql_model.graphql_data import GraphQLData
from graphql_codegen.graphql_model.graphql_type_adds import GraphQLTypeAdd


def test_enum():
    graphql_file_content = '''
    enum ExceptionLevel {
      ERROR
      WARNING
      NONE
    }
    '''
    graphql_data = GraphQLData(graphql_file_content)
    result = graphql_data.parsed_enums()
    assert result[0].enum_name == 'ExceptionLevel'
    assert result[0].enum_cases == ['ERROR', 'WARNING', 'NONE']


def test_object():
    graphql_file_content = '''
    type Currency {
      key: ID!
      code: [String]
    }
    '''
    graphql_data = GraphQLData(graphql_file_content)
    result = graphql_data.parsed_objects()
    assert result[0].object_name == 'Currency'
    assert result[0].object_fields[0].field_name == 'key'
    assert result[0].object_fields[0].field_type == 'ID'
    assert result[0].object_fields[0].field_type_adds == []

    assert result[0].object_fields[1].field_name == 'code'
    assert result[0].object_fields[1].field_type == 'String'
    assert result[0].object_fields[1].field_type_adds == \
           [GraphQLTypeAdd.OPTIONAL,
            GraphQLTypeAdd.LIST,
            GraphQLTypeAdd.OPTIONAL]
