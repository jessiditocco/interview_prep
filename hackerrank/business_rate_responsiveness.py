def business_responsiveness_rate(biz_owner_id, all_messages):
    #TODO: COMPLETE ME

    recieved = 0
    responded = 0

    senders = set()

    for message in all_messages:
        if message["recipient"] == biz_owner_id:
            if message["sender"] not in senders:
                recieved += 1
                senders.add(message["sender"])

        if message["sender"] == biz_owner_id and message["recipient"] in senders:
            responded += 1

    if responded == 0:
        return 0

    return int(round(float(responded) / float(recieved) * 100))





print business_responsiveness_rate(234, [
    {"sender": 1, "recipient": 42, "conversation_id": 1}, 
    {"sender": 42, "recipient": 1, "conversation_id": 1},
    {"sender": 2, "recipient": 42, "conversation_id": 2},
    {"sender": 2, "recipient": 42, "conversation_id": 2},
    {"sender": 3, "recipient": 88, "conversation_id": 3},
    {"sender": 3, "recipient": 42, "conversation_id": 4}]
    )