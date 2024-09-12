
import speech_recognition as sr

def record_idea():
    # 音声認識の初期化
    recognizer = sr.Recognizer()
    
    # マイクから音声を取得
    with sr.Microphone() as source:
        print("アイデアを話してください...")
        audio = recognizer.listen(source)

    # 音声をテキストに変換
    try:
        text = recognizer.recognize_google(audio, language='ja-JP')
        print(f"記録されたアイデア: {text}")
        save_idea(text)
    except sr.UnknownValueError:
        print("音声を認識できませんでした。")
    except sr.RequestError as e:
        print(f"サービスにアクセスできません: {e}")

def save_idea(text):
    # テキストをファイルに保存
    with open("ideas.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")
    print("アイデアが保存されました。")

# アイデアを録音して保存
record_idea()

