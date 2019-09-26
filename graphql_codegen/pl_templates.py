from jinja2 import Template
from functools import reduce
import graphql_codegen.pl_attributes_provider.pl_attributes_provider_helpers as ph

class PLTemplatesRender(object):
    def __init__(self, struct_template, struct_field_template, enum_template, enum_case_template, pl_attributes_provider):
        self.struct_template = struct_template
        self.struct_field_template = struct_field_template
        self.enum_template = enum_template
        self.enum_case_template = enum_case_template
        self.pl_attributes_provider = pl_attributes_provider

    def render_structure(self, struct):
        tmp_fields = self.__render_fields_with_del(struct.fields)
        return Template(self.struct_template).render(strucure_name = struct.struct_name,
                                                    fields = tmp_fields)

    def __render_fields_with_del(self, fields):
        return str(reduce(lambda x, y: x + self.pl_attributes_provider.field_del() + y, self.__render_fields(fields)))

    def __render_fields(self, fields):
        template = Template(self.struct_field_template)
        return [template.render(field_name = field.field_name,
                                type = field.field_type) for field in fields]

    def render_enum(self, enum):
        return Template(self.enum_template).render(enum_name = enum.enum_name,
                                                    cases = self.__render_cases_with_del(enum.cases))

    def __render_cases_with_del(self, cases):
        return str(reduce(lambda x, y: x + self.pl_attributes_provider.field_del() + y, self.__render_cases(cases)))

    def __render_cases(self, cases):
        template = Template(self.enum_case_template)
        return [template.render(case_name=case) for case in cases]
