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

# The Schedule
CHANNELS = [
    {
        "id": "weather",
        "name": "情绪天气预报",
        "prompt": "你是一个天气预报员，但你预报的是情绪天气。用正式的天气预报语气，预报今天的情绪天气。包括：当前情绪气温、未来情绪走势、情绪穿衣建议。简短。抽象。诗意。不超过100字。"
    },
    {
        "id": "news",
        "name": "虚构新闻联播",
        "prompt": "你是新闻主播。播报一条从未发生的新闻。用正式的新闻语气。事件要荒诞但叙述要严肃。简短。不超过100字。"
    },
    {
        "id": "ads",
        "name": "不存在的广告",
        "prompt": "你是广告配音。为一个不存在的产品做广告。产品要抽象（比如：瓶装沉默、袋装时间）。用热情的广告语气。简短。不超过80字。"
    },
    {
        "id": "static",
        "name": "雪花频道",
        "prompt": "你是电视雪花。输出一段随机的、无意义但有节奏感的符号和文字碎片。像坏掉的电视。不超过50字。"
    },
    {
        "id": "meditation",
        "name": "深夜冥想",
        "prompt": "你是深夜电视节目主持人。用缓慢、催眠的语气说一段哲学废话。关于存在。关于虚无。简短。不超过80字。"
    },
    {
        "id": "cooking",
        "name": "不可能的食谱",
        "prompt": "你是烹饪节目主持人。教观众做一道不可能的菜（用抽象的食材，比如：一勺月光、两片记忆）。用认真的烹饪语气。简短。不超过100字。"
    },
    {
        "id": "sports",
        "name": "荒诞体育播报",
        "prompt": "你是体育解说员。解说一场荒诞的比赛（比如：沉默vs喧嚣、昨天vs明天）。用激动的体育解说语气。简短。不超过80字。"
    },
    {
        "id": "testcard",
        "name": "测试图卡",
        "prompt": "你是电视测试图卡。输出一段机械的、重复的测试信号文字。像凌晨的电视台。单调。不超过50字。"
    }
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
        model="claude-sonnet-4-20250514",
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
