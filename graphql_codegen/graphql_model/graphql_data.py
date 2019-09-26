from graphql.language import ast
from graphql.language.parser import parse
from graphql_codegen.graphql_model.graphql_enum import GraphQLEnum
from graphql_codegen.graphql_model.graphql_field import GraphQLField
from graphql_codegen.graphql_model.graphql_object import GraphQLObject
from graphql_codegen.graphql_model.graphql_type_adds import GraphQLTypeAdd


class GraphQLData(object):
    def __init__(self, content):
        definitions = parse(content).definitions
        self.enums = [i for i in definitions if
                      type(i) is ast.EnumTypeDefinition]
        self.objects = [i for i in definitions if
                        type(i) is ast.ObjectTypeDefinition]

    def __get_field_types_adds(self, field, current_adds, prev_add):
        # parsing graphql object type
        if type(field.type) is ast.NamedType \
                and prev_add == GraphQLTypeAdd.OPTIONAL:
            return current_adds
        if type(field.type) is ast.NamedType \
                and prev_add != GraphQLTypeAdd.OPTIONAL:
            return [GraphQLTypeAdd.OPTIONAL, *current_adds]
        if type(field.type) is ast.NonNullType:
            return self.__get_field_types_adds(field.type, current_adds,
                                               GraphQLTypeAdd.OPTIONAL)
        if type(field.type) is ast.ListType \
                and prev_add == GraphQLTypeAdd.OPTIONAL:
            return self.__get_field_types_adds(field.type,
                                               [GraphQLTypeAdd.LIST,
                                                *current_adds],
                                               GraphQLTypeAdd.LIST)
        if type(field.type) is ast.ListType \
                and prev_add != GraphQLTypeAdd.OPTIONAL:
            return self.__get_field_types_adds(field.type,
                                               [GraphQLTypeAdd.LIST,
                                                GraphQLTypeAdd.OPTIONAL,
                                                *current_adds],
                                               GraphQLTypeAdd.LIST)
        return []

    def __get_field_type(self, field):
        if type(field.type) is ast.NamedType:
            return field.type.name.value
        return self.__get_field_type(field.type)

    def __parse_object_fields(self, fields):
        # creating list with fields for graphql object
        parsed_fields = []
        for field in fields:
            type_adds = self.__get_field_types_adds(field, [],
                                                    GraphQLTypeAdd.NONE)
            new_graphql_field = GraphQLField(field.name.value,
                                             self.__get_field_type(field),
                                             type_adds)
            parsed_fields.append(new_graphql_field)
        return parsed_fields

    def parsed_enums(self):
        # getting list with graphql enums
        result = []
        for enum in self.enums:
            cases = [i.name.value for i in enum.values]
            result.append(GraphQLEnum(enum.name.value, cases))
        return result

    def parsed_objects(self):
        # getting list with graphql objects
        result = []
        for object_unit in self.objects:
            object_fields = self.__parse_object_fields(object_unit.fields)
            graphql_object = GraphQLObject(object_unit.name.value,
                                           object_fields)
            result.append(graphql_object)
        return result
