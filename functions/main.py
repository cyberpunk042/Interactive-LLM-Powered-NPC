import cv2
from functions.face_detection import save_extracted_face
from functions.find_character import find_character_with_lowest_cosine_score
from functions.audio_generate_side_character import audio_generate_side_character
from functions.audio_generate_background_character import audio_generate_background_character
from functions.webcam_photo_emotion_predictor import webcam_photo_emotion_predictor
from functions.get_name import get_name
from functions.video_generate_background_character import video_generate_background_character
from functions.video_generate_side_character import video_generate_side_character


def main(screen, transcribed_text, player_name, game_name, background_character_mode = False):
    facial_animation_video_path, audio_path, coordinates = '', '', ''

    # Save the screen capture to a file
    #cv2.imwrite('temp/screen.jpg', screen)
    
    cursor_pos = win32api.GetCursorPos()
    x, y = cursor_pos
    capture = screen.copy()
    cropped_capture = capture[max(0, y-50):min(screen.shape[0], y+50), max(0, x-50):min(screen.shape[1], x+50)]
    cv2.imwrite('temp/extracted_focus.jpg', cropped_capture)
    output_path = 'temp/extracted_focus.jpg'

    # Clean up after the task
    #os.remove('temp/screen.jpg')

    coordinates = (x-50, y-50, 100, 100)  # Adjust the coordinates according to the crop size

    # Set desired emotion
    emotion = "Blissful and Fulfilled"
        
    # TODO: Add the NPC / Character files
    characters_folder = os.listdir(f"{game_name}/characters")
    characters = [character for character in characters_folder if os.path.isdir(f"{game_name}/characters/{character}")]

    # Hardcoded character name
    character_name = "cuberpunk042-minion"
    if not background_character_mode:
        print("Character is ", character_name)
        audio_path = audio_generate_side_character(
            transcribed_text, player_name, game_name, character_name, 'temp/extracted_focus.jpg', emotion)
    else:
        print("Character is background character")
        audio_path = audio_generate_background_character(
            transcribed_text, player_name, game_name, 'temp/extracted_focus.jpg', emotion)

    return audio_path, coordinates


