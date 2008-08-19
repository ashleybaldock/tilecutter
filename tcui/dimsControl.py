# coding: UTF-8
#
# TileCutter, User Interface Module - dimsControl
#
import wx, imres

class dimsControl(wx.StaticBox):
    """Box containing dimensions controls"""
    def __init__(self, parent, app, parent_sizer):
        self.app = app
        wx.StaticBox.__init__(self, parent, wx.ID_ANY, self.gt("Dimensions"))
            # Setup sizers
        self.s_dims = wx.StaticBoxSizer(self, wx.VERTICAL)
        self.s_dims_flex = wx.FlexGridSizer(0,2,0,0)
        self.s_dims_flex.AddGrowableCol(1)
            # Add items
        self.dims_p_label = wx.StaticText(parent, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.dims_p_select = wx.ComboBox(parent, wx.ID_ANY, "", (-1, -1), (54, -1), "", wx.CB_READONLY)
        self.dims_z_label = wx.StaticText(parent, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.dims_z_select = wx.ComboBox(parent, wx.ID_ANY, "", (-1, -1), (54, -1), "", wx.CB_READONLY)
        self.dims_x_label = wx.StaticText(parent, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.dims_x_select = wx.ComboBox(parent, wx.ID_ANY, "", (-1, -1), (54, -1), "", wx.CB_READONLY)
        self.dims_y_label = wx.StaticText(parent, wx.ID_ANY, "", (-1, -1), (-1, -1), wx.ALIGN_LEFT)
        self.dims_y_select = wx.ComboBox(parent, wx.ID_ANY, "", (-1, -1), (54, -1), "", wx.CB_READONLY)
            # Add to sizers
        self.s_dims_flex.Add(self.dims_p_label, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT, 3)
        self.s_dims_flex.Add(self.dims_x_label, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT, 3)
        self.s_dims_flex.Add(self.dims_p_select, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.BOTTOM, 3)
        self.s_dims_flex.Add(self.dims_x_select, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.BOTTOM, 3)
        self.s_dims_flex.Add(self.dims_z_label, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT, 3)
        self.s_dims_flex.Add(self.dims_y_label, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT, 3)
        self.s_dims_flex.Add(self.dims_z_select, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT, 3)
        self.s_dims_flex.Add(self.dims_y_select, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT, 3)
        self.s_dims.Add(self.s_dims_flex, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
            # Add element to its parent sizer
        parent_sizer.Add(self.s_dims, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 0)
            # Bind functions
        self.dims_p_select.Bind(wx.EVT_COMBOBOX, self.OnPaksizeSelect, self.dims_p_select)
        self.dims_z_select.Bind(wx.EVT_COMBOBOX, self.OnZdimsSelect, self.dims_z_select)
        self.dims_x_select.Bind(wx.EVT_COMBOBOX, self.OnXdimsSelect, self.dims_x_select)
        self.dims_y_select.Bind(wx.EVT_COMBOBOX, self.OnYdimsSelect, self.dims_y_select)

    def translate(self):
        """Update the text of all controls to reflect a new translation"""
        self.dims_p_label.SetLabel(self.gt("Paksize"))
        self.dims_p_select.SetToolTipString(self.gt("tt_dims_paksize_select"))
        self.dims_z_label.SetLabel(self.gt("Z dimension"))
        self.dims_z_select.SetToolTipString(self.gt("tt_dims_z_select"))
        self.dims_x_label.SetLabel(self.gt("X dimension"))
        self.dims_x_select.SetToolTipString(self.gt("tt_dims_x_select"))
        self.dims_y_label.SetLabel(self.gt("Y dimension"))
        self.dims_y_select.SetToolTipString(self.gt("tt_dims_y_select"))
        # To allow for translation of values in combobox controls, master list is int list, translated list is generated
        #   on the fly from the master list, these lists then index each other to determine the values to set
        # Translate the choicelist values for paksize
        self.choicelist_packsize = self.app.tctranslator.translateIntArray(self.app.choicelist_paksize_int)
        self.dims_p_select.Clear()
        for i in self.choicelist_packsize:
            self.dims_p_select.Append(i)
        # And set value to value in the project
        self.dims_p_select.SetStringSelection(self.choicelist_packsize[self.app.choicelist_paksize_int.index(self.app.activeproject.paksize())])
        # Translate the choicelist values for z dims
        self.choicelist_dims_z = self.app.tctranslator.translateIntArray(self.app.choicelist_dims_z_int)
        self.dims_z_select.Clear()
        for i in self.choicelist_dims_z:
            self.dims_z_select.Append(i)
        # And set value to value in the project
        self.dims_z_select.SetStringSelection(self.choicelist_dims_z[self.app.choicelist_dims_z_int.index(self.app.activeproject.z())])
        # Translate the choicelist values for x and y dims
        self.choicelist_dims = self.app.tctranslator.translateIntArray(self.app.choicelist_dims_int)
        self.dims_x_select.Clear()
        self.dims_y_select.Clear()
        for i in self.choicelist_dims:
            self.dims_x_select.Append(i)
            self.dims_y_select.Append(i)
        # And set value to value in the project
        self.dims_x_select.SetStringSelection(self.choicelist_dims[self.app.choicelist_dims_int.index(self.app.activeproject.x())])
        self.dims_y_select.SetStringSelection(self.choicelist_dims[self.app.choicelist_dims_int.index(self.app.activeproject.y())])
    def gt(self,text):
        return self.app.tctranslator.gt(text)

    def update(self):
        """Set the values of the controls in this group to the values in the model"""
        self.dims_p_select.SetStringSelection(self.choicelist_packsize[self.app.choicelist_paksize_int.index(self.app.activeproject.paksize())])
        self.dims_z_select.SetStringSelection(self.choicelist_dims_z[self.app.choicelist_dims_z_int.index(self.app.activeproject.z())])
        self.dims_x_select.SetStringSelection(self.choicelist_dims[self.app.choicelist_dims_int.index(self.app.activeproject.x())])
        self.dims_y_select.SetStringSelection(self.choicelist_dims[self.app.choicelist_dims_int.index(self.app.activeproject.y())])

    def OnPaksizeSelect(self,e):
        """Change value of the paksize"""
        self.app.activeproject.paksize(self.app.choicelist_paksize_int[self.choicelist_packsize.index(self.dims_p_select.GetValue())])
        self.app.frame.display.update()
    def OnZdimsSelect(self,e):
        """Change value of the Z dims"""
        self.app.activeproject.z(self.app.choicelist_dims_z_int[self.choicelist_dims_z.index(self.dims_z_select.GetValue())])
        self.app.frame.display.update()
    def OnXdimsSelect(self,e):
        """Change value of the X dims"""
        self.app.activeproject.x(self.app.choicelist_dims_int[self.choicelist_dims.index(self.dims_x_select.GetValue())])
        self.app.frame.display.update()
    def OnYdimsSelect(self,e):
        """Change value of the Y dims"""
        self.app.activeproject.y(self.app.choicelist_dims_int[self.choicelist_dims.index(self.dims_y_select.GetValue())])
        self.app.frame.display.update()
