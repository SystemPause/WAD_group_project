from django import template

register = template.Library()

@register.inclusion_tag('language_swap/profile_cards.html')
def get_cards_list(userDetails, status, media=None, user=None):
    return {'details': userDetails,  'status' : status, 'media' : media, 'user' : user}
