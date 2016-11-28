from collections import OrderedDict


class ChoiceConst(object):
    pass


class Choices(object):
    '''
    Helps to create choice within django models
    Create a `Choices` instance by scpecifying choices as parameters:
    the parameter are 2-tuples, the first value is the choice's constant name
    within the model and the second value is the choice's value
    choice value.
    SOME_CHOICES = Choices(
        ('OPENED', 'opened'),
        ('CLOSED', 'closed'),
    )
    '''
    def __init__(self, *choices):
        self.choices = choices

    def get_const(self):
        choice_const = ChoiceConst()
        for key, value in self.choices:
            setattr(choice_const, key, value)
        return choice_const

    def get_choices(self):
        return [(value, value) for _, value in self.choices]

# NOTE: think about implementing a version with numerical value of the choice
