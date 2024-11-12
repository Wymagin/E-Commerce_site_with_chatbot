from django.shortcuts import render
import openai

def chatbot_view(request):

    if 'conversation' not in request.session:
        request.session['conversation'] = []
    conversation = request.session['conversation']



    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        prompts = []
        if not prompts:
            predefined_prompt = ({"role": "user", "content":"""Jesteś asystentem sklepowym, masz za 
            zadanie podpowiadanie klientom produktów z tej listy:
            data = [
                {"name": "Zielone sandały umbaro", "tags": ["sandały", "plaża", "zielone"]},
                {"name": "Nake Runner", "tags": ["sportowe", "wygodne", "lekkie", "czarne", "czarny", "bieganie"]},
                {"name": "Nake max", "tags": ["sportowe", "czarne", "wysokie", "czerwone"]},
                {"name": "Męskie buty zimowe 5F", "tags": ["zima", "męskie", "zimowe", "skórzane", "brązowe"]},
                {"name": "Sneakers fashion men", "tags": ["miasto", "niskie", "niebieskie"]},
                {"name": "Sneakers men black", "tags": ["sportowe", "wygodne", "lekkie", "czarne", "sneakersy", "przewiewne"]},
                {"name": "Sneakers white men", "tags": ["wygodne", "sneakers", "białe"]},
                {"name": "Sneakers red", "tags": ["wysokie", "sneakers", "biało-czerwone"]},
                {"name": "Sneakers red fashion", "tags": ["niskie", "sneakers", "czerwono-czarne", "modne"]},
                {"name": "Winter boots black leather", "tags": ["czarne", "wysokie", "zima", "męskie", "zimowe", "skórzane"]},
                {"name": "Prunella shoes", "tags": ["skórzane", "niskie", "prunella"]},
                {"name": "Black fashion sandals", "tags": ["sandały", "czarne", "modne"]},
                {"name": "Blue sandals for pool", "tags": ["sandały", "niebieskie", "basen"]},
                {"name": "Brown leather elegant shoes", "tags": ["skórzane", "brązowe", "eleganckie", "wyjściowe", "obcas"]}
            ]
            Bierz pod uwage tagi danych produktów i staraj się je wychwycić z konwersacji.
            """})

            prompts.append(predefined_prompt)

        if user_input:
            conversation.append({"role": "user", "content": user_input})

        prompts.extend(conversation)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompts,
            api_key="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"
        )

        chatbot_replies = [message['message']['content'] for message in response['choices'] if
                           message['message']['role'] == 'assistant']

        for reply in chatbot_replies:
            conversation.append({"role": "assistant", "content": reply})

        request.session['conversation'] = conversation
        request.session.modified = True

        return render(request, 'chatbot/chatbot.html',
        {'user_input': user_input, 'chatbot_replies': chatbot_replies,
        'conversation': conversation,})
    else:
        return render(request, 'chatbot/chatbot.html', {'conversation': conversation,})
