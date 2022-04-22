import os
import traceback
from django import db
from asgiref.sync import sync_to_async


def db_health_check():
    try:
        if not os.getenv('PYTEST_RUNNING'):
            with db.connections['default'].cursor() as cursor:
                try:
                    cursor.execute("SELECT 1")
                    one = cursor.fetchone()[0]
                    if one != 1:
                        raise Exception('Database is not healthy')
                finally:
                    cursor.close()
        return True
    except Exception:
        traceback.print_exc()
        return False


def request_started():
    '''
    Django.db.__init__
    '''
    if not os.getenv('PYTEST_RUNNING'):
        for conn in db.connections.all():
            conn.queries_log.clear()
        for conn in db.connections.all():
            conn.close_if_unusable_or_obsolete()


def request_finished():
    '''
    Django.db.__init__
    '''
    if not os.getenv('PYTEST_RUNNING'):
        for conn in db.connections.all():
            conn.close_if_unusable_or_obsolete()


async def async_request_started():
    await sync_to_async(request_started, thread_sensitive=True)()


async def async_request_finished():
    await sync_to_async(request_finished, thread_sensitive=True)()
