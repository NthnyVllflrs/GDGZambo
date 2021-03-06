import requests

from django import forms

from cloudinary.forms import CloudinaryFileField   

from .models import Member, Volunteer

class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = (
			'photo', 'firstname', 'lastname', 'email', 'description', 'position',
			'expertise', 'facebook', 'twitter', 'instagram', 'website',
		)

		widgets = {
			'description': forms.Textarea(attrs={'rows': 3, 'cols': 20, 'id': 'member-description',}),
			'expertise': forms.Textarea(attrs={'rows': 3, 'cols': 20, 'id': 'member-expertise',}),
			'facebook': forms.TextInput(attrs={'id': 'member-facebook',}),
			'twitter': forms.TextInput(attrs={'id': 'member-twitter',}),
			'instagram': forms.TextInput(attrs={'id': 'member-instagram',}),
			'website': forms.URLInput(attrs={'id': 'member-website',}),
		}

	photo = CloudinaryFileField( 
		options = { 'crop': 'scale', 'width': 720, 'height': 720,
	})

	def clean_photo(self):
		return self.cleaned_data['photo'] or None

	def clean_facebook(self):
		facebook_username = self.cleaned_data['facebook']
		if facebook_username:
			request = requests.get('https://www.facebook.com/' + str(facebook_username))
			if request.status_code != 200:
				raise forms.ValidationError("Invalid Facebook Username")
		return facebook_username

	def clean_twitter(self):
		twitter_username = self.cleaned_data['twitter']
		if twitter_username:
			request = requests.get('https://www.twitter.com/' + str(twitter_username))
			if request.status_code != 200:
				raise forms.ValidationError("Invalid Twitter Username")
		return twitter_username

	def clean_instagram(self):
		instagram_username = self.cleaned_data['instagram']
		if instagram_username:
			request = requests.get('https://www.instagram.com/' + str(instagram_username))
			if request.status_code != 200:
				raise forms.ValidationError("Invalid Instagram Username")
		return instagram_username


class VolunteerForm(forms.ModelForm):
	photo = CloudinaryFileField( 
		options = { 'crop': 'scale', 'width': 720, 'height': 720,},
		required=False,
	)
	
	class Meta:
		model = Volunteer
		fields = (
			'photo', 'firstname', 'lastname', 'email', 'description',
			'expertise', 'facebook', 'twitter', 'instagram', 'website',
		)
		widgets = {
		'firstname': forms.TextInput(attrs={'id': 'volunteer-firstname'}),
		'lastname': forms.TextInput(attrs={'id': 'volunteer-lastname'}),
		'email': forms.EmailInput(attrs={'id': 'volunteer-email'}),
		'description': forms.Textarea(attrs={'rows': 3, 'cols': 20, 'id': 'volunteer-description',}),
		'expertise': forms.Textarea(attrs={'rows': 3, 'cols': 20, 'id': 'volunteer-expertise',}),
		'facebook': forms.TextInput(attrs={'id': 'volunteer-facebook',}),
		'twitter': forms.TextInput(attrs={'id': 'volunteer-twitter',}),
		'instagram': forms.TextInput(attrs={'id': 'volunteer-instagram',}),
		'website': forms.URLInput(attrs={'id': 'volunteer-website',}),}

	def clean_photo(self):
		return self.cleaned_data['photo'] or None

	def clean_facebook(self):
		facebook_username = self.cleaned_data['facebook']
		if facebook_username:
			request = requests.get('https://www.facebook.com/' + str(facebook_username))
			if request.status_code != 200:
				raise forms.ValidationError("Invalid Facebook Username")
		return facebook_username

	def clean_twitter(self):
		twitter_username = self.cleaned_data['twitter']
		if twitter_username:
			request = requests.get('https://www.twitter.com/' + str(twitter_username))
			if request.status_code != 200:
				raise forms.ValidationError("Invalid Twitter Username")
		return twitter_username

	def clean_instagram(self):
		instagram_username = self.cleaned_data['instagram']
		if instagram_username:
			request = requests.get('https://www.instagram.com/' + str(instagram_username))
			if request.status_code != 200:
				raise forms.ValidationError("Invalid Instagram Username")
		return instagram_username