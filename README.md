<div align="center">

<img src="assets/binary-portrait.svg" width="480" alt="Sanchit Pawar rendered in binary" />

<img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=22&duration=3000&pause=800&color=39D353&center=true&vCenter=true&width=600&lines=Hi%2C+I'm+Sanchit+Pawar+%F0%9F%91%8B;Java+Backend+Developer;Spring+Boot+%C2%B7+PostgreSQL+%C2%B7+Redis+%C2%B7+Docker;Building+production-grade+APIs" alt="Typing intro" />

[![About](https://img.shields.io/badge/🧩_About-0d1117?style=for-the-badge)](#-about-me)
[![Projects](https://img.shields.io/badge/🚀_Projects-0d1117?style=for-the-badge)](#-featured-projects)
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

## 🚀 Featured Projects

<div align="center">

[![JourneyOS](https://github-readme-stats.vercel.app/api/pin/?username=sanchitpdev&repo=journeyos&theme=tokyonight&hide_border=true)](https://github.com/sanchitpdev/journeyos)
[![FluxCards](https://github-readme-stats.vercel.app/api/pin/?username=sanchitpdev&repo=FluxCards&theme=tokyonight&hide_border=true)](https://github.com/sanchitpdev/FluxCards)

</div>

<details>
<summary><b>🗺️ JourneyOS — Multi-Modal Travel Planning Engine</b> <i>(click to expand)</i></summary>
<br>

**7 Spring Boot microservices** behind an API Gateway running a parse → route → aggregate → score → rank pipeline for end-to-end journey planning across a 40-city network.

- **Delay-intelligence engine**: models per-leg delays as a log-normal distribution from mode/duration baselines plus weather and holiday signals, then validates every transfer against 95th-percentile worst-case delay — connections a traveler would likely miss get dropped.
- **Gemini API** natural-language trip parsing with a rule-based fallback, **Redis** caching, Flyway-migrated **PostgreSQL**, all in one Docker Compose stack with a React + TypeScript frontend.

`Java` · `Spring Boot` · `PostgreSQL` · `Redis` · `Docker` · `React`

</details>

<details>
<summary><b>⌨️ TypeDuo — LLM-Backed Code-Typing Platform</b> <i>(click to expand)</i></summary>
<br>

A code-typing practice platform where a **scheduled job pre-generates and validates exercises into a content bank**, so requests are served instantly instead of waiting on a live LLM call.

- **Server-side scoring** recomputes typing speed and accuracy from each raw submission so results can't be faked, with a per-user readiness score across difficulty levels.
- **Java 21 + Spring Boot 3**, stateless JWT auth, Flyway-migrated PostgreSQL, Docker Compose, React + TypeScript frontend.

`Java 21` · `Spring Boot 3` · `PostgreSQL` · `Docker` · `React`

</details>

<details>
<summary><b>🧠 FluxCards — AI Flashcard Engine</b> <i>(click to expand)</i></summary>
<br>

Turns any uploaded PDF into flashcards: an AI pipeline built on **Apache PDFBox + the Gemini API**, with Flyway-managed schema migrations.

- **JWT auth with refresh-token rotation** and Bucket4j rate limiting across 15+ REST endpoints in a layered service architecture.
- 8-table normalized **PostgreSQL** schema with Hibernate/JPA mappings; backend on Render, React frontend on Vercel.

`Spring Boot 3` · `Gemini API` · `PostgreSQL` · `React` · 🔗 **[Live demo](https://fluxcards-flashcard-engine.vercel.app/)**

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

<img src="https://github-readme-activity-graph.vercel.app/graph?username=sanchitpdev&theme=tokyo-night&hide_border=true&area=true" width="95%" alt="Contribution graph" />

</div>

## 🐍 Contribution Snake

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sanchitpdev/sanchitpdev/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sanchitpdev/sanchitpdev/output/github-contribution-grid-snake.svg" />
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/sanchitpdev/sanchitpdev/output/github-contribution-grid-snake.svg" />
</picture>

</div>

## 🤝 Let's connect

I'm open to backend developer / SDE internships and early-career roles. If you work on backend systems or distributed architecture, I'd love to connect.

[![LinkedIn](https://img.shields.io/badge/Connect_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/sanchitpawar)
[![Email](https://img.shields.io/badge/Say_hello-sanchitp.dev@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sanchitp.dev@gmail.com)

<div align="center">
<sub>⚡ This README plays games, renders me in binary, and updates itself — <a href="https://github.com/sanchitpdev/sanchitpdev">see how it works</a></sub>
</div>
