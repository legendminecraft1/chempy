from kivymd.app import MDApp 
from kivy.properties import ObjectProperty
from chempy import balance_stoichiometry
import arabic_reshaper
import bidi.algorithm
import webbrowser
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import ScreenManager , Screen 

from through import the
from gh import a

class MainWindow (Screen):
	texti=bidi.algorithm.get_display(arabic_reshaper.reshape('اكتب الرمز الذي يحتوي على أرقام وحرف إي في قائمة المكونات'))
	texti1=bidi.algorithm.get_display(arabic_reshaper.reshape('اكتب معادلة كيميائية غير موزونة'))
	texti2=bidi.algorithm.get_display(arabic_reshaper.reshape('اكتب رمز أي عنصر كيميائي لتحصل على توزيعه الإلكتروني'))
	texti3=bidi.algorithm.get_display(arabic_reshaper.reshape('كيمياء جابر بن حيان'))
	texti4=bidi.algorithm.get_display(arabic_reshaper.reshape('شروح مادة الكيمياء'))
	def copy1(self):
		label = ObjectProperty()
		Clipboard.copy(self.label.text)
	def copy2(self):
		lbl = ObjectProperty()
		Clipboard.copy(self.lbl.text)
	def copy3(self):
		label2 = ObjectProperty()
		Clipboard.copy(self.label2.text)
	def lessons(self):
		webbrowser.open('https://youtube.com/@omarchemical94')
	def search_word(self):
		input = ObjectProperty()
		lbl = ObjectProperty()
		word_meaning = a
		lop = list(word_meaning.keys())
		if self.input.text :
			try :
				self.lbl.text = bidi.algorithm.get_display(arabic_reshaper.reshape(word_meaning.get(lop[lop.index(self.input.text)])))
			except :
				self.lbl.text = bidi.algorithm.get_display(arabic_reshaper.reshape('لم يتم إضافة هذا المضاف الغذائي بعد'))
	def elect(self):
		inp = ObjectProperty()
		label = ObjectProperty()
		try:
			reactants, products = self.inp.text.split('=')
			reactants = reactants.strip()
			products = products.strip()
			balanced_reaction = balance_stoichiometry(reactants.split('+'), products.split('+'))
			balanced_equation = ''
			for reactant, coefficient in balanced_reaction[0].items():
				balanced_equation += f"{coefficient}{reactant} + "
			balanced_equation = balanced_equation[:-3] + " = "
			for product, coefficient in balanced_reaction[1].items():
				balanced_equation += f"{coefficient}{product} + "
			balanced_equation = balanced_equation[:-3]
			self.label.text = balanced_equation
		except :
			self.label.text = bidi.algorithm.get_display(arabic_reshaper.reshape(''))
	def weight (self):
		inp2 = ObjectProperty()
		label2 = ObjectProperty()
		wordMeaning = the
		lkey = list(wordMeaning.keys())
		if self.inp2.text :
			try :
				self.label2.text = wordMeaning.get(lkey[lkey.index(self.inp2.text)])
			except :
				self.label2.text = bidi.algorithm.get_display(arabic_reshaper.reshape(''))

				
class WindowManager (ScreenManager):
	pass

class Face (MDApp):
	def build (self ):
		pass
Face().run()