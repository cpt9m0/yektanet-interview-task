import os
import uuid


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.email.split('@')[0], ext)
    return os.path.join(instance.directory_string_var, filename)
