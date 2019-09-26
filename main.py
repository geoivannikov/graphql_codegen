import graphql_codegen.core as core
from pathlib import Path
import os

from main_helpers import get_arg
from main_helpers import create_pl_file

from graphql_codegen.pl_templates import PLTemplatesRender
from graphql_codegen.graphql_model.graphql_data import GraphQLData
from graphql_codegen.converter import Converter
import graphql_codegen.pl_attributes_provider.pl_attributes_provider_helpers as ph


def main():
    arguments = get_arg()

    attribute_provider = ph.get_attribute_provider(arguments.language)
    template_render = PLTemplatesRender(arguments.struct_template,
                                        arguments.field_template,
                                        arguments.enum_template,
                                        arguments.case_template,
                                        attribute_provider)
    converter = Converter(attribute_provider)
    graphql_data = GraphQLData(arguments.graphql_content)
    pl_files = core.generate_code(graphql_data, converter, template_render, attribute_provider)

    if not os.path.exists(Path(arguments.dst)):
        os.makedirs(Path(arguments.dst))
    for pl_file in pl_files:
        create_pl_file(pl_file, Path(arguments.dst))


if __name__ == '__main__':
    main()
