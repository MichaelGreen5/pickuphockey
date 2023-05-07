def auto_finalize_rosters(skate_obj):
    from OrgDash.models import DarkTeam, LightTeam
    from django.core.mail import send_mail
    from django.template.loader import render_to_string
    #TODO need to have html email rendered and sent
    dark_team = DarkTeam.objects.get(event=skate_obj)
    light_team = LightTeam.objects.get(event=skate_obj)
    dark_team_members = dark_team.team.all()
    light_team_members = light_team.team.all()
    
    player_emails = [player.email for player in light_team_members] +[player.email for player in dark_team_members]
    event_host = skate_obj.host
   
   
   
    context = { 'event':skate_obj, 'light_team_members':light_team_members, 'dark_team_members':dark_team_members}
    html_content = render_to_string('pickupsports\OrgDash\templates\OrgDash\Skates\roster_email.html', {
    context
    })

        
        
    subject = "Rosters for" + event_host.first_name + "'s event at " + skate_obj.location
    message = "message"
    recipient_list = player_emails
    recipient_list.append(skate_obj.host.email)
    
    send_mail(subject, message,  'pickuphockey1@gmail.com', recipient_list, html_message= html_content)
