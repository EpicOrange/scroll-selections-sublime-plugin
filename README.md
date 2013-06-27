Scroll Selections for Sublime Text 2
====================================

Scroll to previous/next selection region in multiple selection mode, especially for find all in a long file.

Installation
------------

Copy **[scroll_selections.py](https://github.com/zerosyn/scroll-selections-sublime-plugin/raw/master/scroll_selections.py)** into your ST2 User packages folder *(Sublime Text 2 > Preferences > Browse Packages... > User)*


Usage
-----

Add commands to your User Key Bindings, for example:

	{ "keys": ["ctrl+pageup"], "command": "show_prev_selections" },
	{ "keys": ["ctrl+pagedown"], "command": "show_next_selections" },

Then select multiple regions in a long file and scroll with hotkeys handily.