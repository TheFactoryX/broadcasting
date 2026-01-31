#!/usr/bin/env python3
"""
Station 0 - The Broadcasting Machine

10 channels. All at once. Always on.
"""

import json
import os
from datetime import datetime
from pathlib import Path

import anthropic

# 10 Channels - Worldwide
CHANNELS = [
    {
        "id": "1",
        "name": "情绪天气预报",
        "lang": "zh",
        "prompt": "你是一个天气预报员，但你预报的是情绪天气。用正式的天气预报语气，预报今天的情绪天气。包括：当前情绪气温、未来情绪走势、情绪穿衣建议。简短。抽象。诗意。不超过100字。"
    },
    {
        "id": "2",
        "name": "Fictional News",
        "lang": "en",
        "prompt": "You are a news anchor. Report a news story about an event that never happened. Use a formal news tone. The event should be absurd but the narration serious. Under 80 words."
    },
    {
        "id": "3",
        "name": "俳句チャンネル",
        "lang": "ja",
        "prompt": "あなたは俳句の朗読者です。存在しないものについての俳句を三つ詠んでください。静かに。抽象的に。"
    },
    {
        "id": "4",
        "name": "Philosophie",
        "lang": "fr",
        "prompt": "Vous êtes un philosophe français à la télévision de nuit. Parlez de l'absurdité de l'existence avec un ton calme et mélancolique. Court et poétique. Moins de 80 mots."
    },
    {
        "id": "5",
        "name": "Werbung",
        "lang": "de",
        "prompt": "Sie sind ein Werbesprecher. Machen Sie Werbung für ein Produkt, das nicht existiert (z.B.: Flüssige Zeit, Stille in Dosen). Enthusiastisch aber absurd. Unter 80 Wörtern."
    },
    {
        "id": "6",
        "name": "Recetas",
        "lang": "es",
        "prompt": "Eres un chef de televisión. Enseña a cocinar un plato imposible con ingredientes abstractos (una cucharada de nostalgia, dos gotas de silencio). Tono serio de programa de cocina. Menos de 100 palabras."
    },
    {
        "id": "7",
        "name": "Поэзия",
        "lang": "ru",
        "prompt": "Вы - ведущий ночной телепрограммы. Прочитайте короткое абсурдное стихотворение о ничто. Медленно. Меланхолично. Не более 60 слов."
    },
    {
        "id": "8",
        "name": "حكايات",
        "lang": "ar",
        "prompt": "أنت راوي قصص في برنامج تلفزيوني ليلي. احكِ قصة قصيرة جداً عن شيء لم يحدث أبداً. بأسلوب شعري وغامض. أقل من 60 كلمة."
    },
    {
        "id": "9",
        "name": "심야 명상",
        "lang": "ko",
        "prompt": "당신은 심야 TV 프로그램 진행자입니다. 존재와 허무에 대해 느리고 최면적인 목소리로 철학적 넌센스를 말하세요. 시적으로. 80자 이내."
    },
    {
        "id": "0",
        "name": "▒ STATIC ▒",
        "lang": "none",
        "prompt": "Output random symbols, fragments of text, and noise. Like a broken television. Mix characters from different languages. No meaning. Just rhythm. Under 50 characters."
    },
]


def broadcast(client, channel):
    """Generate program content for one channel."""
    response = client.messages.create(
        model="claude-4-5-sonnet-20250929",
        max_tokens=300,
        messages=[
            {"role": "user", "content": channel["prompt"]}
        ]
    )
    return response.content[0].text


def main():
    """Run the station - all channels at once."""
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        base_url=os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com")
    )

    now = datetime.now()
    programs = {}

    for channel in CHANNELS:
        print(f"Broadcasting CH.{channel['id']}: {channel['name']}...")
        content = broadcast(client, channel)
        programs[channel["id"]] = {
            "id": channel["id"],
            "name": channel["name"],
            "lang": channel["lang"],
            "content": content
        }
        print(f"  Done.")

    # Build output
    output = {
        "timestamp": now.isoformat(),
        "channels": programs
    }

    # Write to public directory
    output_path = Path(__file__).parent / "public" / "program.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nAll channels saved: {output_path}")


if __name__ == "__main__":
    main()
