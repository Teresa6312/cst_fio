from .base import *
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY', 'SOME+RANDOM+KEY(z9+3vnm(jb0u@&w68t#5_e8s9-lbfhv-')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES = {
    'default': db_from_env
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_FRAME_DENY               = True
X_FRAME_OPTIONS                 = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF     = True
SECURE_HSTS_PRELOAD             = True


support_email = os.environ.get('support_email','cuishan1122@gmail.com')