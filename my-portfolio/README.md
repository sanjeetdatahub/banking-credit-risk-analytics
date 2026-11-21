# 🌐 Sanjeet Kumar — Data Analyst Portfolio (Next.js Application)

A high-performance, modular **Next.js 14 (App Router) + TypeScript** portfolio and data science analytics showcase for **Sanjeet Kumar**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sanjeet%20Kumar-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sanjeetdatahub/)
[![GitHub](https://img.shields.io/badge/GitHub-sanjeetdatahub-181717?logo=github&logoColor=white)](https://github.com/sanjeetdatahub)
[![Framework](https://img.shields.io/badge/Framework-Next.js%2014%20App%20Router-black?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/Language-TypeScript-3178C6?logo=typescript)](https://www.typescriptlang.org/)

---

## 🌟 Architectural Features

1. **Next.js App Router Architecture**:
   - Single-page fluid portfolio with dedicated sub-routes for deep dives:
     - `/`: Main executive portfolio dashboard.
     - `/projects/banking`: Dedicated Banking Credit Risk analytics case study.
     - `/projects/adidas`: Dedicated Adidas US Sales commercial case study.
     - `/simulator`: Standalone full-page Live Analytics Playground.
2. **Component Isolation & Separation of Concerns**:
   - Every domain section has its own dedicated directory in `src/components/sections/` (`hero`, `about`, `skills`, `projects`, `simulator`, `experience`, `contact`).
   - CSS Modules for scoped, collision-free styling.
   - Decoupled datasets stored in `src/data/` (`siteConfig.ts`, `projectsData.ts`, `caseStudiesData.ts`, `skillsData.ts`, `timelineData.ts`).
3. **Shared Mathematical Utilities**:
   - `src/lib/analytics/creditRiskEngine.ts`: Empirical logistic Probability of Default ($PD$), Basel regulatory Expected Loss ($EL$), and risk tiering.
   - `src/lib/analytics/adidasRetailEngine.ts`: Dynamic retail channel pricing and operating margin calculations.
   - `src/utils/formatters.ts`: Formatted currency, percentages, and numbers.
4. **Dual-Theme System (Dark & Light)**:
   - Deep Cyber Dark Mode (`#0A0F1D`) & Vibrant Color/Light Mode (`#F8FAFC`).
   - Anti-FOUC (Flash of Unstyled Content) detection script in `layout.tsx`.
   - Context-managed state with `localStorage` memory.
5. **Interactive UI & Simulators**:
   - Real-time slider recalculations for borrower default risk and retail scenarios.
   - Animated count-up statistics with `IntersectionObserver`.
   - Project category filtering with smooth transitions.
   - Accessible modal window with ESC key dismiss and background lock.
   - Interactive contact form with validation and animated feedback toast.
6. **Ultra-Responsive for All Devices**:
   - Tailored breakpoints for mobile (320px–480px), tablet (768px–992px), and high-resolution monitors.

---

## 📂 Directory Structure

```text
my-portfolio/
├── public/
│   └── assets/
│       ├── sanjeet_resume.pdf
│       └── images/
│           ├── sanjeet-photo.jpg
│           ├── banking/
│           └── adidas/
├── src/
│   ├── app/
│   │   ├── layout.tsx              # Root HTML, fonts, metadata & providers
│   │   ├── page.tsx                # Main single-page dashboard
│   │   ├── globals.css             # Dual-theme design tokens & reset
│   │   ├── simulator/page.tsx      # Standalone simulator page
│   │   └── projects/
│   │       ├── banking/page.tsx    # Standalone Banking deep dive
│   │       └── adidas/page.tsx     # Standalone Adidas deep dive
│   ├── components/
│   │   ├── common/                 # Navbar, Footer, ThemeToggle, CaseStudyModal, Icons
│   │   └── sections/               # Hero, About, Skills, Projects, Simulator, Timeline, Contact
│   ├── context/
│   │   ├── ThemeContext.tsx        # Persistent theme state
│   │   └── ModalContext.tsx        # Case study modal state
│   ├── data/                       # Content repositories (projects, case studies, skills)
│   ├── lib/
│   │   └── analytics/              # Pure math calculation engines (PD, EL, Margin)
│   ├── utils/
│   │   └── formatters.ts           # Currency and number formatting
│   └── types/                      # Strict TypeScript interfaces
├── package.json
├── tsconfig.json
└── next.config.mjs
```

---

## 🚀 Getting Started

### 1. Prerequisites
Install Node.js (v18.17+ or v20 LTS recommended):
```bash
# On macOS via Homebrew:
brew install node
```

### 2. Install Dependencies
```bash
cd "/Users/sanjeetkumar/Desktop/My Portfolio/my-portfolio"
npm install
```

### 3. Run Development Server
```bash
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

### 4. Build for Production
```bash
npm run build
npm start
```
