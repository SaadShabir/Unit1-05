import ui

def calculateCost(sender):
	diameter = float(view['diameterInput'].text) #sets diameter
	cost = (0.75 + 1 + (0.5*diameter))*1.13 #calculates cost
	if diameter <= 0:
		cost = 0 #if pizza isnt existent cost is set to 0
	view['costOutput'].text = 'cost: ' + '${:,.2f}'.format(cost)
	

view = ui.load_view()
view.present('sheet')
