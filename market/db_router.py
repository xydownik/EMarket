class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'api' and model._meta.model_name ==  ['product','category']:
            return 'replica1'
        elif model._meta.app_label == 'payments' and model._meta.model_name == 'payment':
            return 'my_keyspace'
        return 'default'

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'api' and model._meta.model_name == ['product','category']:
            return 'replica1'
        elif model._meta.app_label == 'payments' and model._meta.model_name == 'payment':
            return 'my_keyspace'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._state.db == obj2._state.db:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if db == 'replica1':
            return app_label == 'api' and model_name in ['product',
                                                         'category']
        if db == 'my_keyspace':
            return app_label == 'payments' and model_name == 'payment'
        return db == 'default'
