import json

SEND_TO_ALL_PEER = 'send_message_to_all_peer'
SEND_TO_ALL_EDGE = 'send_message_to_all_edge'

PASS_TO_CLIENT_APP = 'pass_message_to_client_application'

# 独自に拡張したENHANCEDメッセージの処理や生成を担当する
class MyProtocolMessageHandler:
    def __init__(self):
        print('mpmh __init__')
        print('Initializing MyProtocolMessageHandler...')

    def handle_message(self, msg, api):
        #とりあえず受け取ったメッセージを自分がCoreノードならブロードキャスト、Edgeならコンソールに出力することでメッセっぽいものをデモ
        print('mpmh handle_meaage')
        msg = json.loads(msg)
        
        my_api = api('api_type', None)
        print('my_api:', my_api)
        if my_api == 'server_core_api':
            print('Bloadcasting ...', json.dumps(msg))
            # TODO: よく考えるとEdgeから受信した場合にしか他のCoreにブロードキャストしないようにすれば重複チェックもいらない...
            api(SEND_TO_ALL_PEER, json.dumps(msg))
            api(SEND_TO_ALL_EDGE, json.dumps(msg))
        else:
            print('MyProtocolMessageHandler received ', msg)
            api(PASS_TO_CLIENT_APP, msg)

        return