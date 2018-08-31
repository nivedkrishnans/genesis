from django.db import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import os.path

lasyaSizeLimit = 1024
videoExtensions = ['.mp4', '.avi', '.mov', '.mkv']


def fileSizeText(value):
    if (value < 1024.0):
        size = value + " bytes"
    elif (value < 1048576.0):
        size = (value/1024.0) + " KB"
    elif (value < 1073741824.0):
        size = (value/1048576.0) + " MB"
    else :
        size = (value/1073741824.0) + " GB"
    return size

def lasya_file_validation(value):
    extension = os.path.splitext( value.name)[1]
    filesize= value.size
    if ((filesize > lasyaSizeLimit) | (extension not in videoExtensions)):
        if filesize > lasyaSizeLimit:
            raise ValidationError("The maximum file size that can be uploaded is " + fileSizeText(lasyaSizeLimit) + ". Uploaded file size is " + fileSizeText(filesize) + ".")
        if extension not in videoExtensions:
            extensions = ""
            for i in videoExtensions:
                extensions = extensions + i + " "
            raise ValidationError("Unknown filetype. The supported file types are " + extensions + " .")
    else:
        return value


class PhoneNumberField():
    phone_regex = r'^\+91\d{10}$|^0\d{10}$|^\d{10}$'
    message = "Please enter a valid 10 digit phone number, prefixed by either 0, +91, or nothing"
    error_messages = {
        'required': 'This field is required',
        'invalid': message
    }

    def get_field(as_regexField=False, *args, **kwargs):
        if as_regexField:
            return forms.RegexField(regex=PhoneNumberField.phone_regex, help_text=PhoneNumberField.message, error_messages=PhoneNumberField.error_messages, *args, **kwargs)
        else:
            return models.CharField(validators=[RegexValidator(regex=PhoneNumberField.phone_regex,
                                                               message=PhoneNumberField.message)], max_length=15, blank=True)
