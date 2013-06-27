import sublime, sublime_plugin

class ShowNextSelectionsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        visible_region = self.view.visible_region()
        regions = self.view.sel()

        if len(regions) > 0:
            nearest = first = False
            for r in regions:
                if first == False or r.begin() < first.begin():
                    first = r
                if not visible_region.contains(r) and r.begin() > visible_region.end() and ( nearest == False or r.begin() < nearest.begin() ):
                    nearest = r

            self.view.show(nearest or first)


class ShowPrevSelectionsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        visible_region = self.view.visible_region()
        regions = self.view.sel()

        if len(regions) > 0:
            nearest = last = False
            for r in regions:
                if last == False or r.end() > last.end():
                    last = r
                if not visible_region.contains(r) and r.end() < visible_region.begin() and ( nearest == False or r.end() > nearest.end() ):
                    nearest = r

            self.view.show(nearest or last)