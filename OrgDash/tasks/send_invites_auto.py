def auto_send_invites(skate_obj):

    from OrgDash.models import Invitation, InviteList
    from django.core.mail import send_mail
    from django.db.models import Q 
    from django.template.loader import render_to_string
    
    group = skate_obj.group_to_invite
    guests = group.members.all()
    inv_list_obj, created = InviteList.objects.get_or_create(event=skate_obj)
    for guest in guests:
        invite_data = {'host': skate_obj.host, 'guest': guest,'event': skate_obj}
        invite = Invitation(**invite_data)
        invite.save()
        inv_list_obj.guests.add(guest)

    for guest in guests:
            subject = "Invitation to " + str(skate_obj.host) + "'s event at " + skate_obj.location
            
            
            all_invites = Invitation.objects.filter(Q(event=skate_obj) & Q (guest=guest))
            for invite in all_invites:
                url = 'www.pickuppuck.com/organize/manage-invites/respond/' + str(invite.pk)
                context = {'guest': guest, 'event':skate_obj, 'url':url}
                html_message = render_to_string('OrgDash/emails/invitation_email.html', context)
            send_mail(subject, 'message',   'pickuphockey1@gmail.com', [guest.email], html_message=html_message)
        





