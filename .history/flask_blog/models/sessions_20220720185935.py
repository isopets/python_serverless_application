
from datetime import datetime

from pynamodb.attributes import (NumberAttribute, UnicodeAttribute,
                                 UTCDateTimeAttribute)
from pynamodb.models import Model


class Session(Model):
    class Meta:
        table_name = "serverless_blog_sessions"
        region = 'ap-northeast-1'
        aws_access_key_id = 'AWS_ACEESS_KEY_ID'
        aws_secret_access_key = 'AWS_SECRET_ACCESS_KEY'
        host = "http://localhost:8000"
    SessionId = UnicodeAttribute(hash_key=True, null=False)
    Session = UnicodeAttribute(null=True)
