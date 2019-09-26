from graphql_codegen.pl_file import PLFile
import \
    graphql_codegen.pl_attributes_provider.pl_attributes_provider_helpers as ph


def generate_code(graphql_data, converter, template_render,
                  attributes_provider):
    # function for generating code
    pl_files = []
    parsed_graphql_objects = graphql_data.parsed_objects()
    parsed_graphql_enums = graphql_data.parsed_enums()

    structs = generate_structs(parsed_graphql_objects, converter,
                               parsed_graphql_enums)
    enums = generate_enums(parsed_graphql_enums, converter)

    pl_files += create_struct_file(structs, template_render,
                                   attributes_provider)
    pl_files += create_enum_file(enums, template_render, attributes_provider)

    return pl_files


def generate_structs(parsed_graphql_objects, converter, enums):
    # generating structs
    converted_obj = []
    for obj in parsed_graphql_objects:
        converted_obj.append(converter.convert_object(obj, enums))
    return converted_obj


def generate_enums(parsed_graphql_enums, converter):
    # generating enums
    converted_enums = []
    for enum in parsed_graphql_enums:
        converted_enums.append(converter.convert_enum(enum))
    return converted_enums


def create_struct_file(structs, template_render, attributes_provider):
    # generating file structure for structs (file name, file content)
    struct_files = []
    for struct in structs:
        struct_content = template_render.render_structure(struct)
        new_struct_file = PLFile(
            struct.struct_name + attributes_provider.file_extension(),
            struct_content)
        struct_files.append(new_struct_file)
    return struct_files


def create_enum_file(enums, template_render, attributes_provider):
    # generating file structure for enums (file name, file content)
    if not attributes_provider.gen_enum(): return []
    enum_files = []
    for enum in enums:
        enum_content = template_render.render_enum(enum)
        new_struct_file = PLFile(
            enum.enum_name + attributes_provider.file_extension(),
            enum_content)
        enum_files.append(new_struct_file)
    return enum_files
