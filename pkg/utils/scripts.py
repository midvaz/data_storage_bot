
from aiogram.types import Message

class Utils:

    # TODO: написать возможность обработки множества файлов
    @staticmethod
    def get_tg_file_id_name_type (m: Message) -> list[str, str, str] | None:
        """
        -> list[file_id, file_name, file_type] | None
        """
        
        if m.photo :
            return [m.photo[-1].file_id, None,  "photo"]
        elif m.video :
            return [m.video.file_id, m.video.file_name, "video"]
        elif m.voice :
            return [m.voice.file_id, None, "voice"]
        elif m.video_note:
            return [m.video_note.file_id, None, "node"]
        elif m.audio :
            return [m.audio.file_id, m.audio.file_name, "audio"]
        elif m.sticker :
            return [m.sticker.file_id, None, "sticker"]
        elif m.document :
            return [m.document.file_id, m.document.file_name, "document"]
        elif m.text:
            # мб это нужно как-то пределать 
            # не совсем понятно, как лучше хранить это в бд
            return  [None, m.text, "text"]
        elif m.location :
            return [None, f"{m.location.latitude} | {m.location.longitude}", "location"]
        else:
            return None

            
