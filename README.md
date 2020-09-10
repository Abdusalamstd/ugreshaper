# ugreshaper
### Text reshaper for ug-language. بۇ تېكىستنى ئەسلىگە كەلتۈرۈش بولىقى
#### Ishlitish Usuli
```python
Windows:          pip install ugreshaper
Ubuntu18:         pip3 install ugreshaper

from ugreshaper import ugreshaper
re = ugreshaper()
reshaped_text = re.reshape( text )
```
#### Qachilap bolup:
```python
from googletrans import Translator

from ugreshaper import ugreshaper

tr = Translator(service_urls=['translate.google.cn'])
txt = tr.translate('Hello world. This is a text reshaper package',dest='ug',src='en')
txt = txt.text   # Original text
print(txt) #asli text
re = ugreshaper()
ans = re.reshape(txt) # Reshaped text
print(ans) #pichimlanghan text
```
Sample:
![Code](/code.png)   
![Answear](/ans.png)
