from data.config import ADMINS

import typing

from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin:typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, obj):
        if not self.is_admin:
            return False

        return str(obj.from_user.id) in ADMINS