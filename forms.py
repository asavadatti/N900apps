from django import newforms as forms

RATING = (
  ('1', '1.'),
  ('2', '2.'),
  ('3', '3.'),
  ('4', '4.'),
  ('5', '5.'),
)

APPNAME = (
  ('AngryBirds','Angry Birds'),
  ('Conky','Conky'),
)

class ReviewForm(forms.Form):
  author = forms.CharField(label='Name')
  review = forms.CharField(label='Review', widget=forms.Textarea())
  rating = forms.CharField(label='Rating', widget=forms.Select(choices=RATING))
  appid = forms.CharField(label='App ID')
  appname = forms.CharField(label='App Name', widget=forms.Select (choices=APPNAME))