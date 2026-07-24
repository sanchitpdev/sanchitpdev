<div align="center">

<img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=22&duration=3000&pause=800&color=39D353&center=true&vCenter=true&width=600&lines=Hi%2C+I'm+Sanchit+Pawar+%F0%9F%91%8B;Java+Backend+Developer;Spring+Boot+%C2%B7+PostgreSQL+%C2%B7+Redis+%C2%B7+Docker;Building+production-grade+APIs" alt="Typing intro" />

<img src="assets/minecraft-graph.svg" width="720" alt="My GitHub contributions as a Minecraft world, built block by block by a pixel miner" />

<sub>⛏ my last year of commits, mined block by block — refreshes itself daily · <b>watch it build: refresh the page</b></sub>

<br><br>

[![About](https://img.shields.io/badge/🧩_About-0d1117?style=for-the-badge)](#-about-me)
[![Projects](https://img.shields.io/badge/🚀_Projects-0d1117?style=for-the-badge)](#-projects)
[![Game](https://img.shields.io/badge/🎮_Play_Me-0d1117?style=for-the-badge)](#-play-tic-tac-toe-against-my-readme)
[![Stats](https://img.shields.io/badge/📊_Stats-0d1117?style=for-the-badge)](#-github-stats)
[![Contact](https://img.shields.io/badge/🤝_Contact-0d1117?style=for-the-badge)](#-lets-connect)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-sanchitpawar-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/sanchitpawar)
[![Email](https://img.shields.io/badge/Email-sanchitp.dev@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:sanchitp.dev@gmail.com)
![Profile Views](https://komarev.com/ghpvc/?username=sanchitpdev&color=39d353&style=flat-square)

</div>

---

## 🧩 About me

- 🔭 Backend developer focused on the **Java & Spring Boot** ecosystem — REST APIs, microservices, and the infrastructure around them.
- ⚙️ I care about the parts of backend most tutorials skip: **failure handling, caching, idempotency, CI/CD, and clean data models**.
- 🎓 **MCA @ Lovely Professional University** (2025–present) · B.Sc Computer Science, SIES College, Mumbai.
- 🏅 Certified: **Java Full Stack (JSpiders)** · HackerRank **[Problem Solving](https://hackerrank.com/certificates/ac1582d85d83)** & **[REST API](https://hackerrank.com/certificates/289140fb22d8)** (Intermediate).
- 📍 Navi Mumbai, India · 💼 Open to **backend / SDE internships and early-career roles**.

## 🛠️ Tech Stack

<div align="center">

[![My Skills](https://skillicons.dev/icons?i=java,spring,hibernate,postgres,redis,docker,githubactions,git,react,ts&perline=10)](https://skillicons.dev)

<sub>Java · Spring Boot · Spring Security · Spring Data JPA · Hibernate · REST APIs · SQL · PostgreSQL · Redis · Mockito · Docker · GitHub Actions · CI/CD</sub>

</div>

## 🚀 Projects

| | Project | What it does | Stack | |
|--|---------|--------------|-------|--|
| 🗺️ | **[JourneyOS](https://github.com/sanchitpdev/journeyos)** | Multi-modal travel planning engine — 7 microservices, delay-aware routing across a 40-city network | `Spring Boot` `PostgreSQL` `Redis` `Docker` | [Repo ↗](https://github.com/sanchitpdev/journeyos) |
| ⌨️ | **TypeDuo** | LLM-backed code-typing trainer — exercises pre-generated into a content bank, zero-latency serving | `Java 21` `Spring Boot 3` `PostgreSQL` | soon |
| 🧠 | **[FluxCards](https://github.com/sanchitpdev/FluxCards)** | Turns any PDF into AI-generated flashcards with spaced repetition | `Spring Boot 3` `Gemini API` `React` | [Live ↗](https://fluxcards-flashcard-engine.vercel.app/) |

<details>
<summary><b>🗺️ JourneyOS — architecture & engineering decisions</b></summary>
<br>

```mermaid
flowchart LR
    U([Traveler]) --> GW[API Gateway]
    GW --> P["NL Parser<br/>Gemini + rule-based fallback"]
    P --> R["Route Aggregator<br/>multi-modal, 40 cities"]
    R --> D["Delay Engine<br/>log-normal model · P95 check"]
    D --> S["Score & Rank"]
    S --> GW
    R <--> C[(Redis cache)]
    R --> DB[(PostgreSQL<br/>Flyway-migrated)]
```

**Engineering decisions that matter:**
- **Delay intelligence, not just routing** — each leg's delay is modeled as a log-normal distribution from mode/duration baselines plus weather and holiday signals; every transfer is validated against the **95th-percentile worst case**, so connections a traveler would realistically miss get dropped before they're recommended.
- **Graceful AI degradation** — Gemini parses free-text trip requests, but a rule-based parser takes over on failure. The system never depends on an LLM being up.
- **7 services, one `docker compose up`** — the whole stack (services, PostgreSQL, Redis, React + TypeScript frontend) boots reproducibly.

</details>

<details>
<summary><b>⌨️ TypeDuo — architecture & engineering decisions</b></summary>
<br>

```mermaid
flowchart LR
    J["Scheduled Job"] --> L["LLM generate<br/>+ validate"]
    L --> B[(Content Bank<br/>PostgreSQL)]
    U([User]) --> A[REST API]
    A --> B
    U -- raw submission --> SC["Server-side Scoring<br/>speed + accuracy recomputed"]
    SC --> RS["Per-user readiness score"]
```

**Engineering decisions that matter:**
- **LLM off the hot path** — a scheduled job generates and validates exercises into a content bank ahead of time, so user requests are served instantly from PostgreSQL instead of waiting seconds on a live LLM call.
- **Cheat-proof scoring** — the server recomputes typing speed and accuracy from each raw submission; clients can't fake results.
- **Java 21 + Spring Boot 3**, stateless JWT auth, Flyway migrations, Docker Compose.

</details>

<details>
<summary><b>🧠 FluxCards — architecture & engineering decisions</b></summary>
<br>

```mermaid
flowchart LR
    PDF([PDF upload]) --> PB["Apache PDFBox<br/>text extraction"]
    PB --> G["Gemini pipeline<br/>card generation"]
    G --> DB[(PostgreSQL<br/>8-table normalized schema)]
    DB --> SR["SM-2 spaced repetition<br/>scheduler"]
    SR --> U([Learner])
    U -.-> AUTH["JWT + refresh rotation<br/>Bucket4j rate limiting"]
    AUTH -.-> DB
```

**Engineering decisions that matter:**
- **JWT with refresh-token rotation** and Bucket4j rate limiting across 15+ REST endpoints — auth built like a production service, not a demo.
- **8-table normalized PostgreSQL schema** with Hibernate/JPA mappings and Flyway-managed migrations.
- **Deployed for real**: backend on Render, React frontend on Vercel — [try it live](https://fluxcards-flashcard-engine.vercel.app/).

</details>

<sub>More on my repos: [url-shortener](https://github.com/sanchitpdev/url-shortener) (Redis cache-aside, AWS ECS) · [order-processing-system](https://github.com/sanchitpdev/order-processing-system) (Kafka, DLQs) · [TaskForge](https://github.com/sanchitpdev/TaskForge) · [StayNest](https://github.com/sanchitpdev/StayNest)</sub>

## 🎮 Play Tic-Tac-Toe against my README

<!-- TTT:START -->
**You are ❌ — click an empty square to play.** A GitHub Action applies your move and the bot (⭕) answers in ~30 seconds.

|     |     |     |
|:---:|:---:|:---:|
| [⬜](https://github.com/sanchitpdev/sanchitpdev/issues/new?title=ttt%7Cmove%7C0&body=Just+press+%27Submit+new+issue%27+and+the+board+updates+in+about+30s.) | [⬜](https://github.com/sanchitpdev/sanchitpdev/issues/new?title=ttt%7Cmove%7C1&body=Just+press+%27Submit+new+issue%27+and+the+board+updates+in+about+30s.) | [⬜](https://github.com/sanchitpdev/sanchitpdev/issues/new?title=ttt%7Cmove%7C2&body=Just+press+%27Submit+new+issue%27+and+the+board+updates+in+about+30s.) |
| [⬜](https://github.com/sanchitpdev/sanchitpdev/issues/new?title=ttt%7Cmove%7C3&body=Just+press+%27Submit+new+issue%27+and+the+board+updates+in+about+30s.) | [⬜](https://github.com/sanchitpdev/sanchitpdev/issues/new?title=ttt%7Cmove%7C4&body=Just+press+%27Submit+new+issue%27+and+the+board+updates+in+about+30s.) | [⬜](https://github.com/sanchitpdev/sanchitpdev/issues/new?title=ttt%7Cmove%7C5&body=Just+press+%27Submit+new+issue%27+and+the+board+updates+in+about+30s.) |
| [⬜](https://github.com/sanchitpdev/sanchitpdev/issues/new?title=ttt%7Cmove%7C6&body=Just+press+%27Submit+new+issue%27+and+the+board+updates+in+about+30s.) | [⬜](https://github.com/sanchitpdev/sanchitpdev/issues/new?title=ttt%7Cmove%7C7&body=Just+press+%27Submit+new+issue%27+and+the+board+updates+in+about+30s.) | [⬜](https://github.com/sanchitpdev/sanchitpdev/issues/new?title=ttt%7Cmove%7C8&body=Just+press+%27Submit+new+issue%27+and+the+board+updates+in+about+30s.) |

🏆 Humans **0** · 🤖 Bot **0** · 🤝 Draws **0**
<!-- TTT:END -->

## 📊 GitHub Stats

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=sanchitpdev&show_icons=true&hide_border=true&theme=tokyonight" height="165" alt="GitHub stats" />
<img src="https://github-readme-streak-stats.herokuapp.com/?user=sanchitpdev&theme=tokyonight&hide_border=true" height="165" alt="Streak stats" />

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=sanchitpdev&layout=compact&hide_border=true&theme=tokyonight" height="140" alt="Top languages" />

</div>

## 🤝 Let's connect

I'm open to backend developer / SDE internships and early-career roles. If you work on backend systems or distributed architecture, I'd love to connect.

[![LinkedIn](https://img.shields.io/badge/Connect_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/sanchitpawar)
[![Email](https://img.shields.io/badge/Say_hello-sanchitp.dev@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sanchitp.dev@gmail.com)

<div align="center">
<sub>⚡ This README mines my commits into a Minecraft world, plays tic-tac-toe, and rebuilds itself daily — <a href="https://github.com/sanchitpdev/sanchitpdev">see how it works</a></sub>
</div>
