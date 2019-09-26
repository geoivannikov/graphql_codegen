from graphql_codegen.pl_content.pl_struct_content.pl_struct import PLStruct
from graphql_codegen.pl_content.pl_struct_content.pl_struct_field import PLStructField
from graphql_codegen.pl_content.pl_enum_content.pl_enum import PLEnum
from graphql_codegen.graphql_model.graphql_type_adds import GraphQLTypeAdd
import graphql_codegen.pl_attributes_provider.pl_attributes_provider_helpers as ph


class Converter(object):
    def __init__(self, pl_attributes_provider):
        self.pl_attributes_provider = pl_attributes_provider

    def __convert_field_type(self, current_type_state, remaining_type):
        # converting graphql field type into language field type
        if not remaining_type:
            if self.pl_attributes_provider.get_optional() in current_type_state:
                return current_type_state + self.pl_attributes_provider.default_value()
            else:
                return current_type_state
        if remaining_type[0] == GraphQLTypeAdd.OPTIONAL:
            return self.__convert_field_type(self.pl_attributes_provider.convert_to_optional(current_type_state), remaining_type[1:])
        if remaining_type[0] == GraphQLTypeAdd.LIST:
            return self.__convert_field_type(self.pl_attributes_provider.list_type(current_type_state), remaining_type[1:])

    def __convert_fields(self, fields, enums):
        # converting graphql type into language type
        convert_fields = []
        for field in fields:
            field_type = self.__convert_field_type(ph.graphql_types(self.pl_attributes_provider,
                                                                    field.field_type,
                                                                    enums),
                                                    field.field_type_adds)
            new_struct_field = PLStructField(field.field_name, field_type)
            convert_fields.append(new_struct_field)
        return convert_fields

    def __convert_cases(self, cases):
        convert_cases = []
        for case in cases:
            convert_cases.append(case)
        return convert_cases

    def convert_object(self, graphql_object, enums):
        return PLStruct(graphql_object.object_name,
                        self.__convert_fields(graphql_object.object_fields, enums))

    def convert_enum(self, graphql_enum):
        return PLEnum(graphql_enum.enum_name,
                      self.__convert_cases(graphql_enum.enum_cases))
