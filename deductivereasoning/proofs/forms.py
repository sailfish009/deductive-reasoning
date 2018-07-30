from django import forms


class MajorSubmissionForm(forms.Form):
    is_universal_major = forms.BooleanField(required=False)
    subject_major = forms.CharField(
        max_length=255,
        label='Major subject',
    )
    is_affirmative_major = forms.BooleanField(required=False)
    predicate_major = forms.CharField(
        max_length=255,
        label='Major predicate',
    )
    is_universal_minor = forms.BooleanField(required=False)
    subject_minor = forms.CharField(
        max_length=255,
        label='Major subject',
    )
    is_affirmative_minor = forms.BooleanField(required=False)
    predicate_minor = forms.CharField(
        max_length=255,
        label='Major predicate',
    )
    is_universal_conclusion = forms.BooleanField(required=False)
    subject_conclusion = forms.CharField(
        max_length=255,
        label='Major subject',
    )
    is_affirmative_conclusion = forms.BooleanField(required=False)
    predicate_conclusion = forms.CharField(
        max_length=255,
        label='Major predicate',
    )
