# Created by: Saad Shbabir	
# Created on: Sept 27
# Created for: ICS3U
# This program displays the price of a pizza once given its diameter
import ui

def calculateCost(sender):
	diameter = float(view['diameterInput'].text) #sets diameter
	cost = (0.75 + 1 + (0.5*diameter))*1.13 #calculates cost
	if diameter <= 0:
		cost = 0 #if pizza isnt existent cost is set to 0
	view['costOutput'].text = 'cost: ' + '${:,.2f}'.format(cost)
	

view = ui.load_view()
view.present('sheet')
