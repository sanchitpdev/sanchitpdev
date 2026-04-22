<h1 align="center">Hey, I'm Sanchit 👋</h1>

<p align="center">
  <b>Java Backend Developer · Spring Boot · APIs · Clean Architecture</b><br/>
  Building backend systems that I can actually explain — not just ones that "somehow work"
</p>

<p align="center">
  <a href="https://linkedin.com/in/sanchitpawar"><img src="https://img.shields.io/badge/LinkedIn-sanchitpawar-0077B5?style=flat&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:sanchitp.dev@gmail.com"><img src="https://img.shields.io/badge/Email-sanchitp.dev@gmail.com-D14836?style=flat&logo=gmail&logoColor=white"/></a>
  <a href="https://x.com/sanchitpawar600"><img src="https://img.shields.io/badge/X-sanchitpawar600-black?style=flat&logo=x&logoColor=white"/></a>
</p>

---

## About Me

I'm a backend developer focused on Java and Spring Boot. My goal is to write code I can reason about clearly — not just code that passes tests.

I learn by building things end-to-end: designing the schema, wiring up the service layer, securing the API, containerising with Docker, and shipping with CI/CD. I care about understanding *why* a pattern works, not just copying it.

Right now I'm deepening my backend fundamentals through project work and consistent DSA practice, aiming to grow into a developer who can be trusted with production systems.

---

## Featured Projects

### 🏠 [StayNest](https://github.com/sanchitpdev/StayNest) — Full-Stack Vacation Rental Platform

> An Airbnb-inspired platform built across two iterations, covering the complete booking lifecycle from property listing to payments, messaging, reviews, and analytics.

**Stack:** Java 21 · Spring Boot 3.3 · Spring Security (JWT) · Spring Data JPA · PostgreSQL · React 18 · Tailwind CSS · Docker · GitHub Actions

What I built and why it matters:
- **17 JPA entities** across two versions (MVP → Enhanced), with soft deletes on all of them using `@SQLDelete` + `@SQLRestriction`
- **Availability Calendar** pre-populated 2 years ahead per unit — gives O(1) availability lookup instead of expensive range queries at booking time
- **Dynamic pricing engine** with priority-based rule resolution (SEASONAL > HOLIDAY > WEEKEND > BASE), per-unit pricing, and a date-range breakdown API
- **JWT auth** with three roles (GUEST / HOST / ADMIN), manual role checks in the service layer for consistent 403 responses
- **Coupon system** with flat and percentage discounts, per-user limits, minimum booking validation, and auto-expiry
- **Postman test suite** with 115 automated cases across 23 phases — dynamic future dates, auto-captured tokens, edge case coverage
- **CI/CD via GitHub Actions** with a self-hosted runner: CI builds and verifies on every push, CD deploys to Docker Compose on push to main with health-check polling

---

### 🔗 [URL Shortener](https://github.com/sanchitpdev/url-shortener) — Production-Deployed Backend Service

> A production-ready URL shortener deployed on AWS ECS Fargate, demonstrating real infrastructure decisions under constraints.

**Stack:** Java 21 · Spring Boot 3 · Redis · PostgreSQL · Docker · AWS ECS Fargate · AWS ECR · AWS ALB · GitHub Actions

**Live:** [url-shortener-version1.vercel.app](https://url-shortener-version1.vercel.app) · API on AWS ALB

Key engineering decisions:
- **Cache-aside with Redis** — every redirect checks Redis first (24h TTL), falls back to PostgreSQL on miss and re-caches. Keeps redirect latency low without complex invalidation logic
- **Multi-stage Docker build** — JDK build stage → lean JRE runtime image (~180 MB), smaller and faster to pull
- **Health-check-gated startup** — `url-service` only starts after Postgres and Redis pass health checks, eliminating connection errors on boot
- **Trivy CVE scanning** in CI — HIGH/CRITICAL vulnerabilities surfaced before any image reaches production
- **Full CI/CD pipeline:** test → build → Trivy scan → push to ECR (tagged with commit SHA) → rolling ECS deploy
- **Slug expiry** — optional `expiryDays` per request, stored as `expiresAt` timestamp on the entity

---

### ✅ [TaskForge](https://github.com/sanchitpdev/TaskForge) — Task Management Backend

> Clean Spring Boot REST API for task management, built to practise layered architecture and real-world API design patterns.

**Stack:** Java · Spring Boot · Spring Data JPA · MySQL · Maven

---

## Tech Stack

**Backend**

![Java](https://img.shields.io/badge/Java-21-ED8B00?style=flat&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-3.x-6DB33F?style=flat&logo=spring&logoColor=white)
![Spring Security](https://img.shields.io/badge/Spring_Security-JWT-6DB33F?style=flat&logo=springsecurity&logoColor=white)
![Spring Data JPA](https://img.shields.io/badge/Spring_Data_JPA-Hibernate-6DB33F?style=flat&logo=spring&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-3.9+-C71A36?style=flat&logo=apachemaven&logoColor=white)

**Databases & Caching**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-316192?style=flat&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8-4479A1?style=flat&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-7-DC382D?style=flat&logo=redis&logoColor=white)

**DevOps & Cloud**

![Docker](https://img.shields.io/badge/Docker-Containerised-0db7ed?style=flat&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat&logo=github-actions&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-ECS_Fargate-FF9900?style=flat&logo=amazonaws&logoColor=white)

**Frontend (supporting)**

![React](https://img.shields.io/badge/React-18-61DAFB?style=flat&logo=react&logoColor=black)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-38B2AC?style=flat&logo=tailwind-css&logoColor=white)

---

## GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=sanchitpdev&theme=github_dark&hide_border=true&show_icons=true&count_private=false" height="150"/>
  &nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=sanchitpdev&theme=github_dark&hide_border=true&include_all_commits=false&count_private=false&layout=compact" height="150"/>
</p>

<p align="center">
  <img src="https://nirzak-streak-stats.vercel.app/?user=sanchitpdev&theme=github_dark&hide_border=true"/>
</p>

---

## What I'm Focused On

- Shipping the next project with even tighter backend architecture
- DSA practice — consistent problem-solving, not just grinding
- Contributing to open source to get exposure to codebases I didn't write

---

<p align="center">
  If something I built is useful to you, a ⭐ goes a long way.<br/>
  Always open to connect — <a href="https://linkedin.com/in/sanchitpawar">LinkedIn</a> is the best place.
</p>
