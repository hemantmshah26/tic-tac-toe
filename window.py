# window.py
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

import gi
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Window(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_title('cross')
        _ui_file = os.path.join(os.path.dirname(__file__), 'window.ui')

        self.builder = Gtk.Builder.new_from_file(_ui_file)
        self.state = [ [self.builder.get_object('btn11'), self.builder.get_object('btn12'), self.builder.get_object('btn13')],
        [self.builder.get_object('btn21'),self.builder.get_object('btn22'),self.builder.get_object('btn23')],
        [self.builder.get_object('btn31'),self.builder.get_object('btn32'),self.builder.get_object('btn33')]]
        self.add(self.builder.get_object('board'))
        self.present()
