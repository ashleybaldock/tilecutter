# coding: UTF-8
#
# TileCutter, User Interface Module - menuObject
#
# This module creates the program's menus
#
import wx, imres, tcui

from debug import DebugFrame as debug

class menuObject:
    """Class containing the main program menu"""
    def __init__(self, parent, app):
        """Create the menu"""
        self.app = app
        self.parent = parent
        self.menu = wx.MenuBar()
        # File menu
        self.fileMenu = wx.Menu()
        self.menu_file_new = self.AddMenuItem(self.fileMenu, self.OnNewProject)
        self.menu_file_open = self.AddMenuItem(self.fileMenu, self.OnOpenProject)
        self.fileMenu.AppendSeparator()
        self.menu_file_save = self.AddMenuItem(self.fileMenu, self.OnSaveProject)
        self.menu_file_saveas = self.AddMenuItem(self.fileMenu, self.OnSaveProjectAs)
        self.fileMenu.AppendSeparator()
        self.menu_file_cut = self.AddMenuItem(self.fileMenu, self.OnCutProject)
        self.menu_file_export = self.AddMenuItem(self.fileMenu, self.OnExportProject)
        self.fileMenu.AppendSeparator()
        self.menu_file_exit = self.AddMenuItem(self.fileMenu, self.OnExit, id=wx.ID_EXIT)
        # Tools menu
        self.toolsMenu = wx.Menu()
        self.menu_tools_dat = self.AddMenuItem(self.toolsMenu, self.OnDatEdit)
        self.menu_tools_smoke = self.AddMenuItem(self.toolsMenu, self.OnSmokeEdit)
        self.toolsMenu.AppendSeparator()
        self.menu_tools_language = self.AddMenuItem(self.toolsMenu, self.OnSelectLanguage)
        self.menu_tools_prefs = self.AddMenuItem(self.toolsMenu, self.OnPreferences, id=wx.ID_PREFERENCES)
        # Help menu
        self.helpMenu = wx.Menu()
        self.menu_help_help = self.AddMenuItem(self.helpMenu, self.OnHelp, id=wx.ID_HELP)
        # Need to fix this so that separator doesn't appear on the mac
        self.helpMenu.AppendSeparator()
        self.menu_help_about = self.AddMenuItem(self.helpMenu, self.OnAbout, id=wx.ID_ABOUT)

        self.menu.Append(self.fileMenu, "")
        self.menu.Append(self.toolsMenu, "")
        self.menu.Append(self.helpMenu, "")

        self.translate()    # Load the initial translation
##        self.update()       # Init this control with the default values from the active project

    def translate(self):
        """Update the text of all menu items to reflect a new translation"""
        # File menu
        self.menu.SetMenuLabel(0,"&File")
        self.menu_file_new.SetItemLabel(self.gt("&New Project") + self.gsc("menu_file_new", "Ctrl-N"))
        self.menu_file_new.SetHelp(self.gt("tt_menu_file_new"))
        self.menu_file_open.SetItemLabel(self.gt("&Open Project") + self.gsc("menu_file_open", "Ctrl-O"))
        self.menu_file_open.SetHelp(self.gt("tt_menu_file_open"))
        self.menu_file_save.SetItemLabel(self.gt("&Save Project") + self.gsc("menu_file_save", "Ctrl-S"))
        self.menu_file_save.SetHelp(self.gt("tt_menu_file_save"))
        self.menu_file_saveas.SetItemLabel(self.gt("Save Project &As") + self.gsc("menu_file_saveas", "Ctrl-A"))
        self.menu_file_saveas.SetHelp(self.gt("tt_menu_file_saveas"))
        self.menu_file_cut.SetItemLabel(self.gt("&Cut Image") + self.gsc("menu_file_cut", "Ctrl-K"))
        self.menu_file_cut.SetHelp(self.gt("tt_menu_file_cut"))
        self.menu_file_export.SetItemLabel(self.gt("&Export .pak") + self.gsc("menu_file_export", "Ctrl-E"))
        self.menu_file_export.SetHelp(self.gt("tt_menu_file_export"))
        self.menu_file_exit.SetItemLabel(self.gt("E&xit") + self.gsc("menu_file_exit", "Alt-Q"))
        self.menu_file_exit.SetHelp(self.gt("tt_menu_file_exit"))
        # Tools menu
        self.menu.SetMenuLabel(1,"&Tools")
        self.menu_tools_dat.SetItemLabel(self.gt(".&dat file options") + self.gsc("menu_tools_dat", "Ctrl-D"))
        self.menu_tools_dat.SetHelp(self.gt("tt_menu_tools_dat"))
        self.menu_tools_smoke.SetItemLabel(self.gt("&Smoke options") + self.gsc("menu_tools_smoke", "Ctrl-M"))
        self.menu_tools_smoke.SetHelp(self.gt("tt_menu_tools_smoke"))
        self.menu_tools_language.SetItemLabel(self.gt("&Language") + self.gsc("menu_tools_language", "Ctrl-L"))
        self.menu_tools_language.SetHelp(self.gt("tt_menu_languages"))
        self.menu_tools_prefs.SetItemLabel(self.gt("&Preferences...") + self.gsc("menu_tools_prefs", "Ctrl-P"))
        self.menu_tools_prefs.SetHelp(self.gt("tt_menu_tools_prefs"))
        # Help menu
        self.menu.SetMenuLabel(2,"&Help")
        self.menu_help_help.SetItemLabel(self.gt("TileCutter Help") + self.gsc("", ""))
        self.menu_help_help.SetHelp(self.gt("tt_menu_help_help"))
        self.menu_help_about.SetItemLabel(self.gt("&About TileCutter") + self.gsc("", ""))
        self.menu_help_about.SetHelp(self.gt("tt_menu_help_about"))
    def gt(self, text):
        return self.app.tctranslator.gt(text)
    def gsc(self, text, default=None):
        """Return the keyboard shortcut associated with a menu item"""
        # Filler function for now
        if default != None:
            return "\t" + default


    def AddMenuItem(self, menu, itemHandler, enabled=1, id=None):
        itemText = "--!--"  # Item text must be set to something, or wx thinks this is a stock menu item
        if id == None:
            menuId = wx.NewId()
            menuItem = wx.MenuItem(menu, menuId, itemText)
            menu.AppendItem(menuItem)
        else:
            menuId = id
            menuItem = wx.MenuItem(menu, menuId)         # Stock menu item based on a specified id
            menu.AppendItem(menuItem)
        # Bind event to parent frame
        self.parent.Bind(wx.EVT_MENU, itemHandler, id=menuId)
        if enabled == 0:
            menu.Enable(menuId, 0)
        return menuItem

    # Menu event functions
    def OnNewProject(self,e):
        debug("Menu-File-> New Project")
        # Check if current project has been changed since last save
        continue_new_project = False
        if self.app.CheckProjectChanged():
            # If so, pop up a confirmation dialog offering the chance to save the file
            continue_new_project = True
        if continue_new_project:
            # If we should continue (e.g. user hasn't cancelled on confirmation or save dialog)
            self.app.NewProject()
            self.parent.update()
            return 1
        else:
            return 0
    def OnOpenProject(self,e):
        debug("Menu-File-> Open Project")
        # Check if current project has been changed since last save
        continue_new_project = True
        if self.app.CheckProjectChanged():
            # If so, pop up a confirmation dialog offering the chance to save the file
            continue_new_project = True
        if continue_new_project:
            # If we should continue (e.g. user hasn't cancelled on confirmation or save dialog)
            self.app.LoadProject("blah.txt")
            self.parent.update()
            return 1
        else:
            return 0
    def OnSaveProject(self,e):
        debug("Menu-File-> Save Project")
        self.app.SaveProject(self.app.activeproject, "blah.txt")
        return 1
    def OnSaveProjectAs(self,e):
        debug("Menu-File-> Save Project As...")
        return 1
    def OnCutProject(self,e):
        debug("Menu-File-> Cut Project")
        self.parent.update()
        debug(self.app.activeproject.paksize())
        return 1
    def OnExportProject(self,e):
        debug("Menu-File-> Export Project")
        return 1
    def OnExit(self,e):
        debug("Menu-File-> Exit Program")
        return 1

    def OnDatEdit(self,e):
        debug("Menu-Tools-> Open .dat edit dialog")
        return 1
    def OnSmokeEdit(self,e):
        debug("Menu-Tools-> Open smoke edit dialog")
        return 1
    def OnSelectLanguage(self,e):
        debug("Menu-Tools-> Open select language dialog")
        dlg = tcui.translationDialog(self.parent, self.app)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
    def OnPreferences(self,e):
        debug("Menu-Tools-> Open preferences dialog")
        return 1

    def OnHelp(self,e):
        debug("Menu-Help-> Open help")
        return 1
    def OnAbout(self,e):
        debug("Menu-Help-> Open about dialog")
        dlg = tcui.aboutDialog(self.parent, self.app, self.app.VERSION_NUMBER)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()