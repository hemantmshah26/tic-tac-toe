# __main__.py
#
# Copyright (C) 2017 Rohit Kaushik
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
from bot import Bot

class TicTacToe():
    def __init__(self, window):
        self.window = window
        self.bot = Bot()
        self._connect_buttons()

    def _connect_buttons(self):
        for i in range(3):
            for j in range(3):
                self.window.state[i][j].connect('clicked', self._update_state)

    def _update_state(self, button):
        current_label = button.get_label()
        print (current_label)
        if current_label is None:
            button.set_label('X')
            self.bot.make_move()
