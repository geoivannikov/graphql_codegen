class GraphQLField(object):
    def __init__(self, field_name, field_type, field_type_adds):
        self.field_name = field_name
        self.field_type = field_type
        self.field_type_adds = field_type_adds
