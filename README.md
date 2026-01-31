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

| CH | Lang | Program |
|---|---|---|
| weather-zh | 中文 | 情绪天气预报 |
| news-en | English | Fictional News Hour |
| haiku-jp | 日本語 | 俳句チャンネル |
| philosophy-fr | Français | Philosophie de Minuit |
| ads-de | Deutsch | Unmögliche Werbung |
| cooking-es | Español | Recetas Imposibles |
| poetry-ru | Русский | Ночная Поэзия |
| tales-ar | العربية | حكايات منتصف الليل |
| meditation-ko | 한국어 | 심야 명상 |
| sports-pt | Português | Esportes Absurdos |
| opera-it | Italiano | Opera dell'Assurdo |
| weather-nl | Nederlands | Emotioneel Weerbericht |
| myth-el | Ελληνικά | Νέοι Μύθοι |
| wisdom-hi | हिन्दी | अर्थहीन ज्ञान |
| news-tr | Türkçe | Olmayan Haberler |
| static | ▒▒▒ | STATIC |

---

## Deploy Your Own Station

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FTheFactoryX%2Fbroadcasting&env=ANTHROPIC_API_KEY,ANTHROPIC_BASE_URL&envDescription=API%20credentials%20for%20broadcasting&project-name=station-0&repository-name=station-0)

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
