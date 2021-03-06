# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2013 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.


class TaskAuth(object):

    def __init__(self, project_repo):
        self.project_repo = project_repo

    def can(self, user, action, task=None):
        action = ''.join(['_', action])
        return getattr(self, action)(user, task)

    def _create(self, user, task):
        return self._only_admin_or_owner(user, task)

    def _read(self, user, task=None):
        return True

    def _update(self, user, task):
        return self._only_admin_or_owner(user, task)

    def _delete(self, user, task):
        return self._only_admin_or_owner(user, task)

    def _only_admin_or_owner(self, user, task):
        if not user.is_anonymous():
            app = self.project_repo.get(task.app_id)
            return (app.owner_id == user.id or user.admin)
        return False
