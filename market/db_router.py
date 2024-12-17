class PrimaryReplicaRouter:
    """
    A router to control all database operations on models in the 'product' and 'category' apps
    to use the 'replica2' database.
    """
    def db_for_read(self, model, **hints):
        return 'replica2'

    def db_for_write(self, model, **hints):

        return 'default'


    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True


