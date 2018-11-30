from django.db import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import os.path
import ast

lasyaSizeLimit = 419430400
prosceniumSizeLimit = 1073741824
battleofbandsSizeLimit = 419430400
videoExtensions = ['.mp4', '.avi', '.mov', '.mkv']
audioVideoExtensions = ['.mp3', '.aac', '.wav', '.mp4', '.avi', '.mov', '.mkv']
articleExtensions=['.doc','.docx','.pdf','.txt']

def videoFileSupportMessage(size):
    extensions = ""
    for i in videoExtensions:
        extensions = extensions + i + ", "
    if len(videoExtensions):
        extensions = extensions[0:(len(extensions)-2)]
    temp = "Video File (Maximum file size: " + fileSizeText(size) + ". Supported file types: "+ extensions+ ")"
    return temp

def articleFileSupportMessage():
    extensions = ""
    for i in articleExtensions:
        extensions = extensions + i + ", "
    if len(articleExtensions):
        extensions = extensions[0:(len(extensions)-2)]
    temp = "Supported file types: "+ extensions
    return temp


def sciencejournalism_file_validation(value):
    extension = os.path.splitext( value.name)[1]
    filesize= value.size
    if  (extension not in articleExtensions):
        extensions = ""
        for i in articleExtensions:
            extensions = extensions + i + ", "
        raise ValidationError("Invalid file type. The supported file types are " + extensions + " .")
    else:
        return value

def audioVideoFileSupportMessage(size):
    extensions = ""
    for i in audioVideoExtensions:
        extensions = extensions + i + ", "
    if len(audioVideoExtensions):
        extensions = extensions[0:(len(extensions)-2)]
    temp = "Audio/Video File (Maximum file size: " + fileSizeText(size) + ". Supported file types: "+ extensions+ ")"
    return temp

def fileSizeText(value):
    if (value < 1024.0):
        size = str(round(value,2)) + " Bytes"
    elif (value < 1048576.0):
        size = str(round(value/1024.0,2)) + " KB"
    elif (value < 1073741824.0):
        size = str(round(value/1048576.0,2)) + " MB"
    else :
        size = str(round(value/1073741824.0,2)) + " GB"
    return size

def lasya_file_validation(value):
    extension = os.path.splitext( value.name)[1]
    filesize= value.size
    if ((filesize > lasyaSizeLimit) & (extension not in videoExtensions)):
        extensions = ""
        for i in videoExtensions:
            extensions = extensions + i + ", "
        raise ValidationError("Invalid file size and file type. The maximum file size that can be uploaded is " + fileSizeText(lasyaSizeLimit) + ". Uploaded file size is " + fileSizeText(filesize) + ".  The supported file types are " + extensions + " .")
    elif filesize > lasyaSizeLimit:
        raise ValidationError("The maximum file size that can be uploaded is " + fileSizeText(lasyaSizeLimit) + ". Uploaded file size is " + fileSizeText(filesize) + ".")
    elif extension not in videoExtensions:
        extensions = ""
        for i in videoExtensions:
            extensions = extensions + i + ", "
        raise ValidationError("Unsupported filetype. The supported file types are " + extensions + " .")
    else:
        return value

def proscenium_file_validation(value):
    extension = os.path.splitext( value.name)[1]
    filesize= value.size
    if ((filesize > prosceniumSizeLimit) & (extension not in videoExtensions)):
        extensions = ""
        for i in videoExtensions:
            extensions = extensions + i + ", "
        raise ValidationError("Invalid file size and file type. The maximum file size that can be uploaded is " + fileSizeText(prosceniumSizeLimit) + ". Uploaded file size is " + fileSizeText(filesize) + ".  The supported file types are " + extensions + " .")
    elif filesize > prosceniumSizeLimit:
        raise ValidationError("The maximum file size that can be uploaded is " + fileSizeText(prosceniumSizeLimit) + ". Uploaded file size is " + fileSizeText(filesize) + ".")
    elif extension not in videoExtensions:
        extensions = ""
        for i in videoExtensions:
            extensions = extensions + i + ", "
        raise ValidationError("Unsupported filetype. The supported file types are " + extensions + " .")
    else:
        return value


def battleofbands_file_validation(value):
    extension = os.path.splitext( value.name)[1]
    filesize= value.size
    if ((filesize > battleofbandsSizeLimit) & (extension not in audioVideoExtensions)):
        extensions = ""
        for i in audioVideoExtensions:
            extensions = extensions + i + ", "
        raise ValidationError("Invalid file size and file type. The maximum file size that can be uploaded is " + fileSizeText(battleofbandsSizeLimit) + ". Uploaded file size is " + fileSizeText(filesize) + ".  The supported file types are " + extensions + " .")
    elif filesize > prosceniumSizeLimit:
        raise ValidationError("The maximum file size that can be uploaded is " + fileSizeText(battleofbandsSizeLimit) + ". Uploaded file size is " + fileSizeText(filesize) + ".")
    elif extension not in audioVideoExtensions:
        extensions = ""
        for i in audioVideoExtensions:
            extensions = extensions + i + ", "
        raise ValidationError("Unsupported filetype. The supported file types are " + extensions + " .")
    else:
        return value


def footprints_file_validation(value):
    extension = os.path.splitext( value.name)[1]
    filesize= value.size
    if ((filesize > footprintsSizeLimit) & (extension not in videoExtensions)):
        extensions = ""
        for i in videoExtensions:
            extensions = extensions + i + ", "
        raise ValidationError("Invalid file size and file type. The maximum file size that can be uploaded is " + fileSizeText(footprintsSizeLimit) + ". Uploaded file size is " + fileSizeText(filesize) + ".  The supported file types are " + extensions + " .")
    elif filesize > footprintsSizeLimit:
        raise ValidationError("The maximum file size that can be uploaded is " + fileSizeText(footprintsSizeLimit) + ". Uploaded file size is " + fileSizeText(filesize) + ".")
    elif extension not in videoExtensions:
        extensions = ""
        for i in videoExtensions:
            extensions = extensions + i + ", "
        raise ValidationError("Unknown filetype. The supported file types are " + extensions + " .")
    else:
        return value

#thanks to pravega18
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
