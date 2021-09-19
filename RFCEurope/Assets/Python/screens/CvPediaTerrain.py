## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
##
## Sevopedia
##   sevotastic.blogspot.com
##   sevotastic@yahoo.com
##


from CvPythonExtensions import *
import CvUtil
import ScreenInput
import CvScreenEnums
import string

# globals
gc = CyGlobalContext()
ArtFileMgr = CyArtFileMgr()
localText = CyTranslator()

class CvPediaTerrain:
	"Civilopedia Screen for Terrain"

	def __init__(self, main):
		self.iTerrain = -1
		self.top = main

		self.X_ICON_PANE = self.top.X_PEDIA_PAGE + 50
		self.Y_ICON_PANE = self.top.Y_PEDIA_PAGE + 30
		self.W_ICON_PANE = 433
		self.H_ICON_PANE = 190

		self.X_ICON = self.X_ICON_PANE + 8
		self.Y_ICON = self.Y_ICON_PANE + 20
		self.W_ICON = 150
		self.H_ICON = 150
		self.ICON_SIZE = 64

		self.X_STATS_PANE = self.X_ICON_PANE + 200
		self.Y_STATS_PANE = self.Y_ICON_PANE + 60
		self.W_STATS_PANE = 950 - self.X_STATS_PANE
		self.H_STATS_PANE = 120

		self.X_SPECIAL_PANE = self.X_ICON_PANE
		self.Y_SPECIAL_PANE = self.Y_ICON_PANE + 200
		self.W_SPECIAL_PANE = 950 - self.X_SPECIAL_PANE
		self.H_SPECIAL_PANE = 150

		self.X_TEXT_PANE = self.X_ICON_PANE
		self.Y_TEXT_PANE = self.Y_ICON_PANE + 360
		self.W_TEXT_PANE = 950 - self.X_SPECIAL_PANE
		self.H_TEXT_PANE = 230

	# Screen construction function
	def interfaceScreen(self, iTerrain):

		self.iTerrain = iTerrain

		self.top.deleteAllWidgets()

		screen = self.top.getScreen()

		bNotActive = (not screen.isActive())
		if bNotActive:
			self.top.setPediaCommonWidgets()

		# Header...
		szHeader = u"<font=4b>" + gc.getTerrainInfo(self.iTerrain).getDescription().upper() + u"</font>"
		szHeaderId = self.top.getNextWidgetName()
		screen.setLabel(szHeaderId, "Background", szHeader, CvUtil.FONT_CENTER_JUSTIFY, self.top.X_SCREEN, self.top.Y_TITLE, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)

		# Top
		screen.setText(self.top.getNextWidgetName(), "Background", self.top.MENU_TEXT, CvUtil.FONT_LEFT_JUSTIFY, self.top.X_MENU, self.top.Y_MENU, 0, FontTypes.TITLE_FONT, WidgetTypes.WIDGET_PEDIA_MAIN, CivilopediaPageTypes.CIVILOPEDIA_PAGE_TERRAIN, -1)

		if self.top.iLastScreen	!= CvScreenEnums.PEDIA_TERRAIN or bNotActive:
			if self.top.iLastScreen != CvScreenEnums.PEDIA_MAIN:
				self.placeLinks()
			self.top.iLastScreen = CvScreenEnums.PEDIA_TERRAIN


		# Icon
		screen.addPanel( self.top.getNextWidgetName(), "", "", False, False,
			self.X_ICON_PANE, self.Y_ICON_PANE, self.W_ICON_PANE, self.H_ICON_PANE, PanelStyles.PANEL_STYLE_BLUE50)
		screen.addPanel(self.top.getNextWidgetName(), "", "", false, false,
			self.X_ICON, self.Y_ICON, self.W_ICON, self.H_ICON, PanelStyles.PANEL_STYLE_MAIN)
		screen.addDDSGFC(self.top.getNextWidgetName(), gc.getTerrainInfo(self.iTerrain).getButton(),
			self.X_ICON + self.W_ICON/2 - self.ICON_SIZE/2, self.Y_ICON + self.H_ICON/2 - self.ICON_SIZE/2, self.ICON_SIZE, self.ICON_SIZE, WidgetTypes.WIDGET_GENERAL, -1, -1 )

		self.placeStats()
		self.placeSpecial()
		self.placeText()


	def placeStats(self):

		screen = self.top.getScreen()

		panelName = self.top.getNextWidgetName()
		screen.addListBoxGFC(panelName, "", self.X_STATS_PANE, self.Y_STATS_PANE, self.W_STATS_PANE, self.H_STATS_PANE, TableStyles.TABLE_STYLE_EMPTY)
#		screen.addPanel( panelName, "", "", true, true, self.X_STATS_PANE, self.Y_STATS_PANE, self.W_STATS_PANE, self.H_STATS_PANE, PanelStyles.PANEL_STYLE_EMPTY )
		screen.enableSelect(panelName, False)

		for k in range(YieldTypes.NUM_YIELD_TYPES):
			iYield = gc.getTerrainInfo(self.iTerrain).getYield(k)
			if (iYield != 0):
				szYield = (u"%s: %i" % (gc.getYieldInfo(k).getDescription().upper(), iYield))

				screen.appendListBoxString(panelName, u"<font=3>" + szYield + (u"%c" % gc.getYieldInfo(k).getChar()) + u"</font>", WidgetTypes.WIDGET_GENERAL, 0, 0, CvUtil.FONT_LEFT_JUSTIFY)
#				screen.attachTextGFC(panelName, "", szYield + (u"%c" % gc.getYieldInfo(k).getChar()), FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)

	def placeSpecial(self):

		screen = self.top.getScreen()

		panelName = self.top.getNextWidgetName()
		screen.addPanel( panelName, localText.getText("TXT_KEY_PEDIA_SPECIAL_ABILITIES", ()), "", true, false, self.X_SPECIAL_PANE, self.Y_SPECIAL_PANE, self.W_SPECIAL_PANE, self.H_SPECIAL_PANE, PanelStyles.PANEL_STYLE_BLUE50 )

		listName = self.top.getNextWidgetName()
		screen.attachListBoxGFC( panelName, listName, "", TableStyles.TABLE_STYLE_EMPTY )
		screen.enableSelect(listName, False)

		szSpecialText = CyGameTextMgr().getTerrainHelp(self.iTerrain, True)
		splitText = string.split( szSpecialText, "\n" )
		for special in splitText:
			if len( special ) != 0:
				screen.appendListBoxString( listName, special, WidgetTypes.WIDGET_GENERAL, -1, -1, CvUtil.FONT_LEFT_JUSTIFY )

	def placeText(self):

		screen = self.top.getScreen()

		panelName = self.top.getNextWidgetName()
		screen.addPanel( panelName, localText.getText("TXT_KEY_PEDIA_DESCRIPTION", ()), "", true, true, self.X_TEXT_PANE, self.Y_TEXT_PANE, self.W_TEXT_PANE, self.H_TEXT_PANE, PanelStyles.PANEL_STYLE_BLUE50 )

		szText = gc.getTerrainInfo(self.iTerrain).getCivilopedia()
		screen.attachMultilineText( panelName, "Text", szText, WidgetTypes.WIDGET_GENERAL, -1, -1, CvUtil.FONT_LEFT_JUSTIFY)

	def placeLinks(self):

		self.top.placeLinks()
		self.top.placeTerrains()


	# Will handle the input for this screen...
	def handleInput (self, inputClass):
		return 0

