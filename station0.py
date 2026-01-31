#!/usr/bin/env python3
"""
Station 0 - The Broadcasting Machine

Switches channels. Every 15 minutes.
A new program. Always different. Always the same.
"""

import json
import os
import random
from datetime import datetime
from pathlib import Path

import anthropic

# The Schedule - Worldwide Broadcast
CHANNELS = [
    # 中文 Chinese
    {
        "id": "weather-zh",
        "name": "情绪天气预报",
        "lang": "zh",
        "prompt": "你是一个天气预报员，但你预报的是情绪天气。用正式的天气预报语气，预报今天的情绪天气。包括：当前情绪气温、未来情绪走势、情绪穿衣建议。简短。抽象。诗意。不超过100字。"
    },
    # English
    {
        "id": "news-en",
        "name": "Fictional News Hour",
        "lang": "en",
        "prompt": "You are a news anchor. Report a news story about an event that never happened. Use a formal news tone. The event should be absurd but the narration serious. Under 80 words."
    },
    # 日本語 Japanese
    {
        "id": "haiku-jp",
        "name": "俳句チャンネル",
        "lang": "ja",
        "prompt": "あなたは俳句の朗読者です。存在しないものについての俳句を三つ詠んでください。静かに。抽象的に。"
    },
    # Français French
    {
        "id": "philosophy-fr",
        "name": "Philosophie de Minuit",
        "lang": "fr",
        "prompt": "Vous êtes un philosophe français à la télévision de nuit. Parlez de l'absurdité de l'existence avec un ton calme et mélancolique. Court et poétique. Moins de 80 mots."
    },
    # Deutsch German
    {
        "id": "ads-de",
        "name": "Unmögliche Werbung",
        "lang": "de",
        "prompt": "Sie sind ein Werbesprecher. Machen Sie Werbung für ein Produkt, das nicht existiert (z.B.: Flüssige Zeit, Stille in Dosen). Enthusiastisch aber absurd. Unter 80 Wörtern."
    },
    # Español Spanish
    {
        "id": "cooking-es",
        "name": "Recetas Imposibles",
        "lang": "es",
        "prompt": "Eres un chef de televisión. Enseña a cocinar un plato imposible con ingredientes abstractos (una cucharada de nostalgia, dos gotas de silencio). Tono serio de programa de cocina. Menos de 100 palabras."
    },
    # Русский Russian
    {
        "id": "poetry-ru",
        "name": "Ночная Поэзия",
        "lang": "ru",
        "prompt": "Вы - ведущий ночной телепрограммы. Прочитайте короткое абсурдное стихотворение о ничто. Медленно. Меланхолично. Не более 60 слов."
    },
    # العربية Arabic
    {
        "id": "tales-ar",
        "name": "حكايات منتصف الليل",
        "lang": "ar",
        "prompt": "أنت راوي قصص في برنامج تلفزيوني ليلي. احكِ قصة قصيرة جداً عن شيء لم يحدث أبداً. بأسلوب شعري وغامض. أقل من 60 كلمة."
    },
    # 한국어 Korean
    {
        "id": "meditation-ko",
        "name": "심야 명상",
        "lang": "ko",
        "prompt": "당신은 심야 TV 프로그램 진행자입니다. 존재와 허무에 대해 느리고 최면적인 목소리로 철학적 넌센스를 말하세요. 시적으로. 80자 이내."
    },
    # Português Portuguese
    {
        "id": "sports-pt",
        "name": "Esportes Absurdos",
        "lang": "pt",
        "prompt": "Você é um narrador esportivo. Narre uma partida absurda (exemplo: Silêncio vs Barulho, Ontem vs Amanhã). Tom emocionado de transmissão esportiva. Menos de 80 palavras."
    },
    # Italiano Italian
    {
        "id": "opera-it",
        "name": "Opera dell'Assurdo",
        "lang": "it",
        "prompt": "Sei un presentatore di opera. Introduci un'opera che non esiste, con una trama assurda. Tono drammatico e teatrale. Meno di 80 parole."
    },
    # Nederlands Dutch
    {
        "id": "weather-nl",
        "name": "Emotioneel Weerbericht",
        "lang": "nl",
        "prompt": "Je bent een weerpresentator, maar je voorspelt emotioneel weer. Geef een formeel weerbericht over de emotionele temperatuur van vandaag. Abstract en poëtisch. Minder dan 80 woorden."
    },
    # ελληνικά Greek
    {
        "id": "myth-el",
        "name": "Νέοι Μύθοι",
        "lang": "el",
        "prompt": "Είστε αφηγητής μύθων. Πείτε έναν σύντομο μύθο για ένα θεό που δεν υπήρξε ποτέ. Αρχαίος τόνος. Λιγότερο από 80 λέξεις."
    },
    # हिन्दी Hindi
    {
        "id": "wisdom-hi",
        "name": "अर्थहीन ज्ञान",
        "lang": "hi",
        "prompt": "आप एक रात्रि टीवी गुरु हैं। कुछ गहन लगने वाला लेकिन अर्थहीन ज्ञान साझा करें। शांत और गंभीर स्वर में। 80 शब्दों से कम।"
    },
    # Türkçe Turkish
    {
        "id": "news-tr",
        "name": "Olmayan Haberler",
        "lang": "tr",
        "prompt": "Haber spikerisisiniz. Hiç olmamış bir olayı haber olarak sunun. Resmi haber tonu. Absürt ama ciddi. 80 kelimeden az."
    },
    # Static / Universal
    {
        "id": "static",
        "name": "▒▒▒ STATIC ▒▒▒",
        "lang": "none",
        "prompt": "Output random symbols, fragments of text, and noise. Like a broken television. Mix characters from different languages. No meaning. Just rhythm. Under 50 characters."
    },
]


def get_current_channel():
    """Based on time, pick a channel."""
    now = datetime.now()
    # Change every 15 minutes
    slot = (now.hour * 4 + now.minute // 15) % len(CHANNELS)
    return CHANNELS[slot]


def broadcast(channel):
    """Generate program content."""
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        base_url=os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com")
    )

    response = client.messages.create(
        model="claude-4-5-sonnet-20250929",
        max_tokens=300,
        messages=[
            {"role": "user", "content": channel["prompt"]}
        ]
    )

    return response.content[0].text


def main():
    """Run the station."""
    channel = get_current_channel()
    print(f"Channel: {channel['name']}")

    content = broadcast(channel)
    print(f"Content: {content}")

    # Current time info
    now = datetime.now()

    # Build program data
    program = {
        "channel": channel["id"],
        "name": channel["name"],
        "lang": channel.get("lang", "en"),
        "content": content,
        "timestamp": now.isoformat(),
        "next_switch": f"{(now.minute // 15 + 1) * 15 % 60:02d}:00"
    }

    # Write to public directory
    output_path = Path(__file__).parent / "public" / "program.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(program, f, ensure_ascii=False, indent=2)

    print(f"Program saved: {output_path}")


if __name__ == "__main__":
    main()
