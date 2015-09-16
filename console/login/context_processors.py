from django.conf import settings  # import the settings file


def global_settings(context):

    return {'PAGINATION_LIMIT': settings.PAGINATION_LIMIT}
