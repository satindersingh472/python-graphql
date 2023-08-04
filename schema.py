from ariadne import gql, QueryType, make_executable_schema, ObjectType
from ariadne.asgi import GraphQL

type_defs = gql("""
type Query {
                user: User
},
type User {
                username: String!
}
            


""")


query = ObjectType("Query")


@query.field("user")
def resolve_user(_, info):
    return [
        {"firstname": "satinder", "lastname": "singh","game":"soccer"},
        {"firstname": "am", "lastname": "kk","game":"cricket"},
        {"firstname": "satindedfaddsfdr", "lastname": "singdadfdfdfh","game":"hockey"}
    ]


user = ObjectType("User")


@user.field("username")
def resolve_username(obj, *_):
    return f"{obj['firstname']} {obj['lastname']}"


schema = make_executable_schema(type_defs,query,user)
app = GraphQL(schema, debug=True)
