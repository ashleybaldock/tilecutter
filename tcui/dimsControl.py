# coding: UTF-8
#
# TileCutter User Interface Module - dimsControl
#

# Copyright © 2008-2011 Timothy Baldock. All Rights Reserved.

import wx, imres

# Utility functions
import translator
gt = translator.Translator()
import config
config = config.Config()
import logger
debug = logger.Log()

class dimsControl(wx.Panel):
    """Box containing dimensions controls"""
    def __init__(self, parent, app):
        """"""
        debug(u"tcui.DimsControl: __init__")
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.app = app
        # Setup sizers
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        # Header text
        self.label = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        # Add items
        self.dims_p_label = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1))
        self.dims_p_select = wx.ComboBox(self, wx.ID_ANY, "", (-1, -1), (-1, -1), "", wx.CB_READONLY)
        self.dims_z_label = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1))
        self.dims_z_select = wx.ComboBox(self, wx.ID_ANY, "", (-1, -1), (-1, -1), "", wx.CB_READONLY)
        self.dims_pz_sizer = wx.BoxSizer(wx.VERTICAL)
        self.dims_x_label = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1))
        self.dims_x_select = wx.ComboBox(self, wx.ID_ANY, "", (-1, -1), (-1, -1), "", wx.CB_READONLY)
        self.dims_y_label = wx.StaticText(self, wx.ID_ANY, "", (-1, -1), (-1, -1))
        self.dims_y_select = wx.ComboBox(self, wx.ID_ANY, "", (-1, -1), (-1, -1), "", wx.CB_READONLY)
        self.dims_xy_sizer = wx.BoxSizer(wx.VERTICAL)
        # Add to sizers
        self.dims_pz_sizer.Add(self.dims_p_label, 0, wx.ALIGN_CENTER)
        self.dims_pz_sizer.Add((0,2))
        self.dims_pz_sizer.Add(self.dims_p_select, 0, wx.ALIGN_CENTER)
        self.dims_pz_sizer.Add((0,4))
        self.dims_pz_sizer.Add(self.dims_z_label, 0, wx.ALIGN_CENTER)
        self.dims_pz_sizer.Add((0,2))
        self.dims_pz_sizer.Add(self.dims_z_select, 0, wx.ALIGN_CENTER)
        self.dims_xy_sizer.Add(self.dims_x_label, 0, wx.ALIGN_CENTER)
        self.dims_xy_sizer.Add((0,2))
        self.dims_xy_sizer.Add(self.dims_x_select, 0, wx.ALIGN_CENTER)
        self.dims_xy_sizer.Add((0,4))
        self.dims_xy_sizer.Add(self.dims_y_label, 0, wx.ALIGN_CENTER)
        self.dims_xy_sizer.Add((0,2))
        self.dims_xy_sizer.Add(self.dims_y_select, 0, wx.ALIGN_CENTER)

        self.dims_horizontal = wx.BoxSizer(wx.HORIZONTAL)
        self.dims_horizontal.Add(self.dims_pz_sizer, 0)
        self.dims_horizontal.Add((6,0))
        self.dims_horizontal.Add(self.dims_xy_sizer, 0)
        # Add to default sizer with header and line
        self.sizer.Add((0,2))
        self.sizer.Add(self.label, 0, wx.LEFT, 2)
        self.sizer.Add((0,4))
        self.sizer.Add(self.dims_horizontal, 1, wx.ALIGN_CENTER)
        self.sizer.Add((0,2))

        # Set panel's sizer
        self.SetSizer(self.sizer)


        # Bind functions
        self.dims_p_select.Bind(wx.EVT_COMBOBOX, self.OnPaksizeSelect, self.dims_p_select)
        self.dims_z_select.Bind(wx.EVT_COMBOBOX, self.OnZdimsSelect, self.dims_z_select)
        self.dims_x_select.Bind(wx.EVT_COMBOBOX, self.OnXdimsSelect, self.dims_x_select)
        self.dims_y_select.Bind(wx.EVT_COMBOBOX, self.OnYdimsSelect, self.dims_y_select)

    def translate(self):
        """Update the text of all controls to reflect a new translation"""
        debug(u"tcui.DimsControl: translate")
        self.label.SetLabel(gt("Dimensions:"))
        self.dims_p_label.SetLabel(gt("Paksize"))
        self.dims_p_select.SetToolTipString(gt("tt_dims_paksize_select"))
        self.dims_z_label.SetLabel(gt("Z dimension"))
        self.dims_z_select.SetToolTipString(gt("tt_dims_z_select"))
        self.dims_x_label.SetLabel(gt("X dimension"))
        self.dims_x_select.SetToolTipString(gt("tt_dims_x_select"))
        self.dims_y_label.SetLabel(gt("Y dimension"))
        self.dims_y_select.SetToolTipString(gt("tt_dims_y_select"))
        # To allow for translation of values in combobox controls, master list is int list, translated list is generated
        #   on the fly from the master list, these lists then index each other to determine the values to set
        # Translate the choicelist values for paksize
        self.choicelist_packsize = gt.translateIntArray(config.choicelist_paksize)
        self.dims_p_select.Clear()
        for i in self.choicelist_packsize:
            self.dims_p_select.Append(i)
        # And set value to value in the project
        self.dims_p_select.SetStringSelection(self.choicelist_packsize[config.choicelist_paksize.index(self.app.activeproject.paksize())])
        # Translate the choicelist values for z dims
        self.choicelist_dims_z = gt.translateIntArray(config.choicelist_dims_z)
        self.dims_z_select.Clear()
        for i in self.choicelist_dims_z:
            self.dims_z_select.Append(i)
        # And set value to value in the project
        self.dims_z_select.SetStringSelection(self.choicelist_dims_z[config.choicelist_dims_z.index(self.app.activeproject.z())])
        # Translate the choicelist values for x and y dims
        self.choicelist_dims = gt.translateIntArray(config.choicelist_dims)
        self.dims_x_select.Clear()
        self.dims_y_select.Clear()
        for i in self.choicelist_dims:
            self.dims_x_select.Append(i)
            self.dims_y_select.Append(i)
        # And set value to value in the project
        self.dims_x_select.SetStringSelection(self.choicelist_dims[config.choicelist_dims.index(self.app.activeproject.x())])
        self.dims_y_select.SetStringSelection(self.choicelist_dims[config.choicelist_dims.index(self.app.activeproject.y())])

        # Ensure all combo boxes are the same width
        biggest_width = max(self.dims_p_select.GetBestSize()[0],
                            self.dims_z_select.GetBestSize()[0],
                            self.dims_x_select.GetBestSize()[0],
                            self.dims_y_select.GetBestSize()[0],
                            60)
        self.dims_p_select.SetMinSize((biggest_width,-1))
        self.dims_z_select.SetMinSize((biggest_width,-1))
        self.dims_x_select.SetMinSize((biggest_width,-1))
        self.dims_y_select.SetMinSize((biggest_width,-1))

        self.Fit()

    def update(self):
        """Set the values of the controls in this group to the values in the model"""
        debug(u"tcui.DimsControl: update")
        self.dims_p_select.SetStringSelection(self.choicelist_packsize[config.choicelist_paksize.index(self.app.activeproject.paksize())])
        self.dims_z_select.SetStringSelection(self.choicelist_dims_z[config.choicelist_dims_z.index(self.app.activeproject.z())])
        self.dims_x_select.SetStringSelection(self.choicelist_dims[config.choicelist_dims.index(self.app.activeproject.x())])
        self.dims_y_select.SetStringSelection(self.choicelist_dims[config.choicelist_dims.index(self.app.activeproject.y())])

    def OnPaksizeSelect(self,e):
        """Change value of the paksize"""
        debug(u"tcui.DimsControl: OnPaksizeSelect")
        self.app.activeproject.paksize(config.choicelist_paksize[self.choicelist_packsize.index(self.dims_p_select.GetValue())])
        self.app.frame.display.update()
    def OnZdimsSelect(self,e):
        """Change value of the Z dims"""
        debug(u"tcui.DimsControl: OnZdimsSelect")
        self.app.activeproject.z(config.choicelist_dims_z[self.choicelist_dims_z.index(self.dims_z_select.GetValue())])
        self.app.frame.display.update()
    def OnXdimsSelect(self,e):
        """Change value of the X dims"""
        debug(u"tcui.DimsControl: OnXdimsSelect")
        self.app.activeproject.x(config.choicelist_dims[self.choicelist_dims.index(self.dims_x_select.GetValue())])
        self.app.frame.display.update()
    def OnYdimsSelect(self,e):
        """Change value of the Y dims"""
        debug(u"tcui.DimsControl: OnYdimsSelect")
        self.app.activeproject.y(config.choicelist_dims[self.choicelist_dims.index(self.dims_y_select.GetValue())])
        self.app.frame.display.update()
