# coding: UTF-8
#
# TileCutter, User Interface Module - aboutDialog
#
import wx, imres

class aboutDialog(wx.Dialog):
    """Dialog which displays information about the program"""
    def __init__(self, parent, app, version_number):
        """Intialise the dialog"""
        self.app = app
        self.version_number = version_number
        size = (300,300)
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "", (-1,-1), size)

        # Overall panel sizer
        self.s_panel = wx.BoxSizer(wx.VERTICAL)
        self.icon = wx.StaticBitmap(self, wx.ID_ANY, imres.catalog["tc_icon2_128_plain"].getBitmap())
        f = self.GetFont()
        self.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.title_text = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_CENTER)
        self.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.subtitle_text = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_CENTER)
        self.SetFont(f)
        self.version_text = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_CENTER)
        self.copyright_text = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_CENTER)

        # Add close button at the bottom
        self.buttons = wx.BoxSizer(wx.HORIZONTAL)
        self.close_button = wx.Button(self, wx.ID_ANY, "", (-1,-1), (-1,-1), wx.ALIGN_RIGHT)
        self.buttons.Add(self.close_button, 0 ,wx.ALIGN_RIGHT, 0)

        self.s_panel.Add(self.icon,1,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 10)
        self.s_panel.Add(self.title_text,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 2)
        self.s_panel.Add(self.subtitle_text,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 4)
        self.s_panel.Add(self.version_text,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 4)
        self.s_panel.Add(self.copyright_text,0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 10)
        # These bits are non-mac only
        self.s_panel.Add(wx.StaticLine(self, wx.ID_ANY, (-1,-1), (-1,1)),0,wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.s_panel.Add(self.buttons,0,wx.ALIGN_RIGHT|wx.ALL, 3)

        # Bind events
        self.close_button.Bind(wx.EVT_BUTTON, self.OnClose, self.close_button)

        # Layout sizers
        self.SetSizer(self.s_panel)
        self.SetAutoLayout(1)
##        self.Layout()

        self.translate()

    def translate(self):
        """Update the text of all controls to reflect a new translation"""
        self.SetLabel(self.gt("About TileCutter"))
        self.close_button.SetLabel(self.gt("Close"))
        self.title_text.SetLabel(self.gt("TileCutter"))
        self.subtitle_text.SetLabel(self.gt("Simutrans Building Editor"))
        self.version_text.SetLabel(self.gt("Version %s") % self.version_number)
        self.copyright_text.SetLabel("Copyright � 2008 Timothy Baldock. All rights reserved.")

        self.Layout()
        self.Refresh()
    def gt(self,text):
        return self.app.tctranslator.gt(text)

    def update(self):
        """Set the values of the controls in this group to the values in the model"""

    def OnClose(self,e):
        """On click of the close button"""
        self.EndModal(wx.ID_OK)


class translationDialog(wx.Dialog):
    """Dialog for choosing which translation to use"""
    def __init__(self,parent,app):
        """Initialise the dialog and populate lists"""
        self.app = app
        size = (300,200)
        wx.Dialog.__init__(self,parent,wx.ID_ANY, "", (-1,-1), size)

        # Overall panel sizer
        self.s_panel = wx.BoxSizer(wx.VERTICAL)
        self.top_label = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.language_picker = wx.ComboBox(self, wx.ID_ANY, self.app.tctranslator.active.longname(), (-1, -1), (-1, -1), self.app.tctranslator.language_longnames_list, wx.CB_READONLY|wx.ALIGN_CENTER_VERTICAL)

        # Within the static box
        self.dialog_box = wx.StaticBox(self, wx.ID_ANY, self.gt("Language Details:"))
        self.s_dialog_box = wx.StaticBoxSizer(self.dialog_box, wx.HORIZONTAL)
        # Bitmap flag display on the left
        self.country_icon = wx.StaticBitmap(self, wx.ID_ANY, self.app.tctranslator.active.icon())
        # Three static texts on the right containing information within a vertical sizer
        self.s_dialog_box_right = wx.FlexGridSizer(0,2,0,0)
        self.s_dialog_box_right.AddGrowableCol(1)
        self.label_name = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.label_createdby = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.label_createdon = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.label_name_value = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.label_createdby_value = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.label_createdon_value = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        # Add these to their sizer
        self.s_dialog_box_right.Add(self.label_name,0,wx.EXPAND, 0)
        self.s_dialog_box_right.Add(self.label_name_value,0,wx.EXPAND|wx.LEFT, 3)
        self.s_dialog_box_right.Add(self.label_createdby,0,wx.EXPAND, 0)
        self.s_dialog_box_right.Add(self.label_createdby_value,0,wx.EXPAND|wx.LEFT, 3)
        self.s_dialog_box_right.Add(self.label_createdon,0,wx.EXPAND, 0)
        self.s_dialog_box_right.Add(self.label_createdon_value,0,wx.EXPAND|wx.LEFT, 3)
        
        # Add close button at the bottom
        self.buttons = wx.BoxSizer(wx.HORIZONTAL)
        self.close_button = wx.Button(self, wx.ID_ANY, "", (-1,-1), (-1,-1), wx.ALIGN_RIGHT)
        self.buttons.Add(self.close_button, 0 ,wx.ALIGN_RIGHT, 0)

        # Then add bitmap and texts to the static box sizer
        self.s_dialog_box.Add(self.country_icon,0,wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5)
        self.s_dialog_box.Add(self.s_dialog_box_right,1,wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 10)

        # And finally add that, the language picker and the other static text to the panel sizer
        self.s_panel.Add(self.top_label,0,wx.EXPAND|wx.ALL, 3)
        self.s_panel.Add(self.language_picker,0,wx.EXPAND|wx.LEFT|wx.RIGHT, 3)
        self.s_panel.Add(self.s_dialog_box,1,wx.EXPAND|wx.ALL, 3)
        self.s_panel.Add(self.buttons,0,wx.ALIGN_RIGHT|wx.ALL, 3)

        # Bind events
        self.language_picker.Bind(wx.EVT_COMBOBOX, self.OnSelection, self.language_picker)
        self.close_button.Bind(wx.EVT_BUTTON, self.OnClose, self.close_button)

        # Layout sizers
        self.SetSizer(self.s_panel)
        self.SetAutoLayout(1)
        self.Layout()

        self.translate()    # Load the initial translation
##        self.update()

    def translate(self):
        """Update the text of all controls to reflect a new translation"""
        self.SetLabel(self.gt("Language"))
        self.top_label.SetLabel(self.gt("Select from the options below:"))
        self.close_button.SetLabel(self.gt("Close"))
        # These values taken from the active translation
        self.label_name.SetLabel(self.gt("Language:"))
        self.label_name_value.SetLabel(self.app.tctranslator.active.longname())
        self.label_createdby.SetLabel(self.gt("Created by:"))
        self.label_createdby_value.SetLabel(self.app.tctranslator.active.created_by())
        self.label_createdon.SetLabel(self.gt("Created on:"))
        self.label_createdon_value.SetLabel(self.app.tctranslator.active.created_date())
        # And finally change the image
        self.country_icon.SetBitmap(self.app.tctranslator.active.icon())
        self.Layout()
        self.Refresh()
    def gt(self,text):
        return self.app.tctranslator.gt(text)

    def update(self):
        """Set the values of the controls in this group to the values in the model"""

    def OnClose(self,e):
        """On click of the close button"""
        self.EndModal(wx.ID_OK)
    def OnSelection(self,e):
        """When user changes the language selection"""
        # Set active translation to the one specified
        self.app.tctranslator.setActiveTranslation(self.app.tctranslator.longnameToName(self.language_picker.GetValue()))
        # Call own translate function
        self.translate()
        self.app.frame.translate()