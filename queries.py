import graphene

import models
from db_conf import db_session
from schemas import BoardModel, PostModel, TablesModel, ViewsModel

db = db_session.session_factory()


class Query(graphene.ObjectType):

    all_posts = graphene.List(PostModel)
    post_by_id = graphene.Field(PostModel, post_id=graphene.Int(required=True))

    def resolve_all_posts(self, info):
        posts_query = PostModel.get_query(info)
        return posts_query.all()

    def resolve_post_by_id(self, info, post_id):
        return db.query(models.Post).filter(models.Post.id == post_id).first()

    all_boards = graphene.List(BoardModel)
    board_by_tenant_id = graphene.Field(BoardModel, tenant_id=graphene.String(required=True))

    def resolve_all_boards(self, info):
        board_query = BoardModel.get_query(info)
        return board_query.all()

    def resolve_board_by_tenant_id(self, info, tenant_id):
        return db.query(models.Board).filter(models.Board.tenant_id == tenant_id).first()

    all_tables = graphene.List(TablesModel)
    table_by_table_schema = graphene.Field(TablesModel, table_schema=graphene.String(required=True))

    def resolve_all_tables(self, info):
        table_query = TablesModel.get_query(info)
        return table_query.all()

    def resolve_table_by_table_schema(self, info, table_schema):
        return db.query(models.Board).filter(models.Tables.table_schema == table_schema).first()

    all_views = graphene.List(ViewsModel)
    view_by_table_schema = graphene.Field(ViewsModel, table_schema=graphene.String(required=True))

    def resolve_all_views(self, info):
        view_query = ViewsModel.get_query(info)
        return view_query.all()

    def resolve_view_by_table_schema(self, info, table_schema):
        return db.query(models.Board).filter(models.Views.table_schema == table_schema).first()
