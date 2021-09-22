# Galaxy Music - Telegram bot project

# Copyright (C) 2021 Roj Serbest
# Copyright (C) 2021 Deshadeeth Thisarana

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by InukaAsith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Shadow")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ShadowBotUpdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/e588c075d8b49ee0819fd.png")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_USERNAME = getenv("BOT_USERNAME", "Mr_Shadow_Robot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Shadow_Helper")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "ShadowBotSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "ShadowMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamOfShadow/ShadowMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1041727415 1578642178").split()))
