from .dev import *

from os import path
from pathlib import Path

DEPLOY_ENVIRONMENT = Environment.TEST

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "server"]

LOGGING["loggers"]["core.views"] = {
    "level": "ERROR",
    "handlers": ["console"],
    "propagate": False,
}

SHARE_DIR = path.realpath("library/tests/tmp")
LIBRARY_ROOT = path.join(SHARE_DIR, "library")
LIBRARY_PREVIOUS_ROOT = path.join(SHARE_DIR, ".latest")
REPOSITORY_ROOT = path.join(BASE_DIR, "repository")
BACKUP_ROOT = path.join(SHARE_DIR, "backups")
BORG_ROOT = path.join(BACKUP_ROOT, "repo")
EXTRACT_ROOT = path.join(SHARE_DIR, "extract")
MEDIA_ROOT = path.join(SHARE_DIR, "media")

DATABASES["dump_restore"] = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "dump_restore_{}".format(config.get("database", "DB_NAME")),
    "USER": config.get("database", "DB_USER"),
    "PASSWORD": config.get("database", "DB_PASSWORD"),
    "HOST": config.get("database", "DB_HOST"),
    "PORT": config.get("database", "DB_PORT"),
}


DATABASE_ROUTERS = [
    "core.database_routers.DumpRestoreRouter",
    "core.database_routers.DefaultRouter",
]

# Spam detection configuration
SPAM_DIR_PATH = Path("/shared/curator/spam")
