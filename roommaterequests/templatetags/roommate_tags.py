from django import template


register = template.Library()

@register.filter
def has_request_from(receiver_user, sender_user):
    """
    Returns True if sender_user has an 'Accepted' RoommateRequest sent to receiver_user.
    """
    request = receiver_user.received_roommate_requests.filter(sender=sender_user).first()
    return request and request.status == 'Accepted'
