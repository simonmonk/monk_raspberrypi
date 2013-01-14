#05_03_converters_final
class ScaleConverter:
	
	def __init__(self, units_from, units_to, factor):
		self.units_from = units_from
		self.units_to = units_to
		self.factor = factor
	
	def description(self):
		return 'Convert ' + self.units_from + ' to ' + self.units_to

	def convert(self, value):
		return value * self.factor

class ScaleAndOffsetConverter(ScaleConverter):
	
	def __init__(self, units_from, units_to, factor, offset):
		ScaleConverter.__init__(self, units_from, units_to, factor)
		self.offset = offset
		
	def convert(self, value):
		return value * self.factor + self.offset
