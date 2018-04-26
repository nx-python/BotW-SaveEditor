"""
This is taken from DavidBuchanan314's rupee edit script.

IMPORTANT:
Obligatory disclamer: back up your saves first, your switch may explode, etc.
You need to launch and close a game prior to launching hbl.
This script modifies the 0th save slot, which doesn't seem to relate to any particular
entry in the game menu.
"""

import struct
import _nx
import sys

TITLE_ID = 0x01007ef00011e000
RUPEE_ID = 0x23149BF8

_nx.account_initialize()
user_id = _nx.account_get_active_user()

if user_id is None:
    print("No active user, you need to launch and close a game prior to launching hbl.")
    sys.exit()

_nx.fs_mount_savedata("save", TITLE_ID, user_id)

gamedata = open("save:/0/game_data.sav", "rb+")

"""
some code to be added here
"""

gamedata.flush()
gamedata.close()

_nx.fsdev_commit_device("save")
_nx.fsdev_unmount_device("save")
