#05_02_converter_offset_bad
class ScaleAndOffsetConverter:
	
	def __init__(self, units_from, units_to, factor, offset):
		self.units_from = units_from
		self.units_to = units_to
		self.factor = factor
		self.offset = offset
	
	def description(self):
		return 'Convert ' + self.units_from + ' to ' + self.units_to

	def convert(self, value):
		return value * self.factor + self.offset

c2 = ScaleAndOffsetConverter('C', 'F', 1.8, 32)
print(c2.description())
print('converting 20C')
print(str(c2.convert(20)) + c2.units_to)
