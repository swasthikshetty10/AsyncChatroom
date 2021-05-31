from channels.generic.websocket import AsyncWebsocketConsumer

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):    
        self.room_name = self.scope['url_route']['kwargs']['room_name']  #-->scope  return's dict containing the url passed string  
        await (
            
        )
    pass