# 📺 Broadcasting

**Station 0**

---

A television that never sleeps.

Every 15 minutes. A new program.

Weather that forecasts emotions.
News that never happened.
Ads for things that don't exist.

---

## The Channels

| CH | Program |
|---|---|
| WEATHER | 情绪天气预报 |
| NEWS | 虚构新闻联播 |
| ADS | 不存在的广告 |
| STATIC | 雪花频道 |
| MEDITATION | 深夜冥想 |
| COOKING | 不可能的食谱 |
| SPORTS | 荒诞体育播报 |
| TESTCARD | 测试图卡 |

---

## Deploy Your Own Station

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fsdpkjc%2FTheFactoryX&env=ANTHROPIC_API_KEY,ANTHROPIC_BASE_URL&envDescription=API%20credentials%20for%20broadcasting&envLink=https%3A%2F%2Fgithub.com%2Fsdpkjc%2FTheFactoryX%2Ftree%2Fmain%2Fbroadcasting&project-name=station-0&repository-name=station-0&root-directory=broadcasting)

---

## How It Works

```
Station 0
    │
    ├── Every 15 minutes
    │       │
    │       └── GitHub Action triggers
    │               │
    │               └── station0.py runs
    │                       │
    │                       └── AI generates program
    │                               │
    │                               └── program.json updates
    │                                       │
    │                                       └── Vercel serves
    │
    └── Repeat forever
```

---

## The Metaphor

| Broadcasting | Code |
|---|---|
| Station | station0.py |
| Channel | Program type |
| Program | Generated content |
| Broadcast | GitHub Action |
| Signal | program.json |
| TV Set | index.html |

---

## Local Testing

```bash
cd broadcasting
pip install anthropic
export ANTHROPIC_API_KEY="your-key"
export ANTHROPIC_BASE_URL="your-base-url"
python station0.py
```

---

**TheFactoryX**

Strange people. Strange things.

📧 hi@sdpkjc.com
