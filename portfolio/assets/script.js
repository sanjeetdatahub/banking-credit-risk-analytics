/**
 * ==========================================================================
 * SANJEET KUMAR - PORTFOLIO INTERACTIVITY SCRIPT
 * Features:
 * - Dual Theme Switcher (Dark vs Vibrant Color/Light) with localStorage persistence
 * - Mobile Navigation Toggle & Smooth Active Spy
 * - Project Filter System
 * - Deep Dive Case Study Modal (Banking & Adidas)
 * - Interactive Analytics Simulator Playground (Risk Calculator & Adidas Explorer)
 * - Animated Number Counters
 * - Contact Form Handler with Feedback Toast
 * ==========================================================================
 */

document.addEventListener("DOMContentLoaded", () => {
  initThemeToggle();
  initNavbarScroll();
  initMobileNav();
  initProjectFilters();
  initModals();
  initPlaygroundSimulators();
  initStatCounters();
  initContactForm();
});

/* --------------------------------------------------------------------------
   1. Dual Theme System (Dark Mode & Vibrant Color Mode)
   -------------------------------------------------------------------------- */
function initThemeToggle() {
  const themeToggleBtn = document.getElementById("themeToggleBtn");
  const themeIcon = themeToggleBtn.querySelector("i");
  
  // Check persisted preference or system preference (default to dark as requested)
  const savedTheme = localStorage.getItem("sanjeet_portfolio_theme") || "dark";
  document.documentElement.setAttribute("data-theme", savedTheme);
  updateThemeIcon(savedTheme, themeIcon);

  themeToggleBtn.addEventListener("click", () => {
    const currentTheme = document.documentElement.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    
    document.documentElement.setAttribute("data-theme", newTheme);
    localStorage.setItem("sanjeet_portfolio_theme", newTheme);
    updateThemeIcon(newTheme, themeIcon);
  });
}

function updateThemeIcon(theme, iconElem) {
  if (theme === "dark") {
    iconElem.className = "fas fa-sun"; // Show sun to toggle to light
    iconElem.setAttribute("title", "Switch to Color/Light Mode");
  } else {
    iconElem.className = "fas fa-moon"; // Show moon to toggle to dark
    iconElem.setAttribute("title", "Switch to Full Dark Mode");
  }
}

/* --------------------------------------------------------------------------
   2. Navbar Scroll Styling & Active Link Spy
   -------------------------------------------------------------------------- */
function initNavbarScroll() {
  const navbar = document.querySelector(".navbar");
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".nav-link");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 40) {
      navbar.classList.add("scrolled");
    } else {
      navbar.classList.remove("scrolled");
    }

    // ScrollSpy
    let currentSectionId = "";
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 120;
      const sectionHeight = section.offsetHeight;
      if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
        currentSectionId = section.getAttribute("id");
      }
    });

    navLinks.forEach(link => {
      link.classList.remove("active");
      if (link.getAttribute("href") === `#${currentSectionId}`) {
        link.classList.add("active");
      }
    });
  });
}

/* --------------------------------------------------------------------------
   3. Mobile Navigation Menu
   -------------------------------------------------------------------------- */
function initMobileNav() {
  const mobileToggle = document.getElementById("mobileToggle");
  const navLinks = document.getElementById("navLinks");
  if (!mobileToggle || !navLinks) return;

  mobileToggle.addEventListener("click", () => {
    navLinks.classList.toggle("mobile-open");
    const icon = mobileToggle.querySelector("i");
    icon.classList.toggle("fa-bars");
    icon.classList.toggle("fa-times");
  });

  navLinks.querySelectorAll(".nav-link").forEach(link => {
    link.addEventListener("click", () => {
      navLinks.classList.remove("mobile-open");
      const icon = mobileToggle.querySelector("i");
      icon.className = "fas fa-bars";
    });
  });
}

/* --------------------------------------------------------------------------
   4. Project Filter System
   -------------------------------------------------------------------------- */
function initProjectFilters() {
  const filterBtns = document.querySelectorAll(".filter-btn");
  const projectCards = document.querySelectorAll(".project-card");

  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      const filterValue = btn.getAttribute("data-filter");

      projectCards.forEach(card => {
        const category = card.getAttribute("data-category");
        if (filterValue === "all" || category.includes(filterValue)) {
          card.style.display = "flex";
          setTimeout(() => { card.style.opacity = "1"; card.style.transform = "translateY(0)"; }, 50);
        } else {
          card.style.opacity = "0";
          card.style.transform = "translateY(15px)";
          setTimeout(() => { card.style.display = "none"; }, 300);
        }
      });
    });
  });
}

/* --------------------------------------------------------------------------
   5. Interactive Case Study Modal Popups
   -------------------------------------------------------------------------- */
const CASE_STUDIES = {
  banking: {
    title: "🏦 Banking Credit Risk & Loan Portfolio Analytics",
    badge: "Enterprise Risk Modeling & Basel III/IFRS 9",
    image: "assets/images/banking/03_roc_auc_curve.png",
    overview: "An enterprise-grade quantitative credit risk analysis and machine learning framework designed for commercial lending. Evaluates Probability of Default (PD), Loss Given Default (LGD), Exposure at Default (EAD), and Expected Loss (EL) across 10,000+ credit facilities.",
    metrics: [
      { label: "Model Discriminatory Power", val: "88.4% ROC-AUC" },
      { label: "Kolmogorov-Smirnov (KS)", val: "61.2% Separation" },
      { label: "Portfolio Expected Loss", val: "$14.2M Mitigated" },
      { label: "Risk Tiers Classified", val: "5 Tiers (AAA - Subprime)" }
    ],
    technicalSteps: [
      "Built multi-factor feature store incorporating DTI, revolving utilization, credit age, and macroeconomic indicators.",
      "Trained calibrated Logistic Regression and LightGBM / XGBoost default classifiers with class weighting.",
      "Engineered transition matrices for delinquency migration tracking (Current -> 30DPD -> 60DPD -> 90+ Default).",
      "Conducted 3-scenario macroeconomic stress testing (Baseline, Adverse, Severe Downturn) simulating GDP contraction."
    ],
    businessImpact: "Empowers retail risk managers to adjust underwriting cutoff thresholds dynamically, protecting bank capital reserves under regulatory stress scenarios while expanding loan origination in Prime segments.",
    githubLink: "https://github.com/sanjeetdatahub/banking-credit-risk-analytics",
    chartEmbed: "assets/images/banking/01_score_distribution_and_cutoff.png"
  },
  adidas: {
    title: "👟 Adidas US Sales Performance & Profitability Analytics",
    badge: "Retail Analytics & Commercial Strategy",
    image: "assets/images/adidas/01_total_sales_and_profit_by_product.png",
    overview: "Comprehensive business intelligence pipeline analyzing $157M+ across 9,648 US retail transactions. Unveils key revenue drivers, channel profit margins, partner performance (Foot Locker, Walmart, West Gear), and geographic footprint.",
    metrics: [
      { label: "Total Gross Revenue", val: "$157.42M" },
      { label: "Operating Profit", val: "$60.09M" },
      { label: "Overall Profit Margin", val: "38.17%" },
      { label: "Apparel vs Footwear Margin", val: "42.0% vs 36.0%" }
    ],
    technicalSteps: [
      "Cleaned raw currency strings, percentages, and commas into verified numeric data types using Pandas.",
      "Engineered temporal features (Month, Year, Quarter, Seasonality) and product category segments.",
      "Computed sales channel efficiency comparing In-store (48% volume) with Online (high margin DTC).",
      "Generated publication-grade Seaborn visualizations (clustered bar charts, donut charts, correlation matrix)."
    ],
    businessImpact: "Uncovered counter-intuitive business insight: while footwear drives maximum unit volume, apparel delivers 600 bps higher operating margins (~42% vs 36%), providing strategic justification for bundled cross-selling campaigns.",
    githubLink: "https://github.com/sanjeetdatahub/adidas-sales-analysis",
    chartEmbed: "assets/images/adidas/04_sales_method_profitability.png"
  }
};

function initModals() {
  const modalOverlay = document.getElementById("caseStudyModal");
  const closeBtn = document.getElementById("modalCloseBtn");
  const modalContainer = document.getElementById("modalDynamicContent");

  document.querySelectorAll("[data-open-case]").forEach(trigger => {
    trigger.addEventListener("click", (e) => {
      e.preventDefault();
      const studyKey = trigger.getAttribute("data-open-case");
      const data = CASE_STUDIES[studyKey];
      if (!data) return;

      modalContainer.innerHTML = `
        <div class="modal-image-banner">
          <img src="${data.image}" alt="${data.title}">
        </div>
        <span class="section-tag">${data.badge}</span>
        <h2 style="font-family: var(--font-heading); font-size: 1.8rem; margin: 0.8rem 0;">${data.title}</h2>
        <p style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.7;">${data.overview}</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin: 1.8rem 0;">
          ${data.metrics.map(m => `
            <div style="background: var(--bg-tertiary); padding: 1.1rem; border-radius: 12px; border: 1px solid var(--border-light);">
              <span style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); display: block;">${m.label}</span>
              <strong style="font-family: var(--font-mono); font-size: 1.3rem; color: var(--brand-primary);">${m.val}</strong>
            </div>
          `).join("")}
        </div>

        <h4 class="modal-section-title">🛠️ Engineering & Modeling Methodology:</h4>
        <ul style="list-style: disc; margin-left: 1.5rem; color: var(--text-secondary); line-height: 1.8;">
          ${data.technicalSteps.map(step => `<li>${step}</li>`).join("")}
        </ul>

        <h4 class="modal-section-title">📊 Visual Evidence & Analysis:</h4>
        <div style="border-radius: 12px; overflow: hidden; margin: 1rem 0; border: 1px solid var(--border-light);">
          <img src="${data.chartEmbed}" alt="Project Chart Preview">
        </div>

        <h4 class="modal-section-title">💡 Strategic Commercial Impact:</h4>
        <p style="color: var(--text-secondary); line-height: 1.7; background: var(--bg-tertiary); padding: 1.2rem; border-radius: 12px; border-left: 4px solid var(--brand-primary);">
          ${data.businessImpact}
        </p>

        <div style="margin-top: 2rem; display: flex; gap: 1rem; flex-wrap: wrap;">
          <a href="${data.githubLink}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
            <i class="fab fa-github"></i> View GitHub Repository
          </a>
          <a href="https://www.linkedin.com/in/sanjeetdatahub" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="border-color: #0A66C2; color: #0A66C2;">
            <i class="fab fa-linkedin"></i> Connect on LinkedIn
          </a>
          <button class="btn btn-outline" onclick="closeModal()">Close Window</button>
        </div>
      `;

      modalOverlay.classList.add("active");
      document.body.style.overflow = "hidden";
    });
  });

  closeBtn.addEventListener("click", closeModal);
  modalOverlay.addEventListener("click", (e) => {
    if (e.target === modalOverlay) closeModal();
  });

  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
  });
}

function closeModal() {
  const modalOverlay = document.getElementById("caseStudyModal");
  if (!modalOverlay) return;
  modalOverlay.classList.remove("active");
  document.body.style.overflow = "auto";
}

/* --------------------------------------------------------------------------
   6. Interactive Live Analytics Playground / Simulators
   -------------------------------------------------------------------------- */
function initPlaygroundSimulators() {
  // Tabs switcher
  const tabs = document.querySelectorAll(".playground-tab");
  const panes = document.querySelectorAll(".tab-pane");

  tabs.forEach(tab => {
    tab.addEventListener("click", () => {
      tabs.forEach(t => t.classList.remove("active"));
      panes.forEach(p => p.classList.remove("active"));
      tab.classList.add("active");
      const targetPane = document.getElementById(tab.getAttribute("data-target"));
      if (targetPane) targetPane.classList.add("active");
    });
  });

  // Simulator 1: Credit Risk Calculator
  const scoreInput = document.getElementById("simCreditScore");
  const dtiInput = document.getElementById("simDTI");
  const loanInput = document.getElementById("simLoanAmount");

  const scoreValText = document.getElementById("simCreditScoreVal");
  const dtiValText = document.getElementById("simDTIVal");
  const loanValText = document.getElementById("simLoanAmountVal");

  const pdResult = document.getElementById("simPDResult");
  const elResult = document.getElementById("simELResult");
  const tierResult = document.getElementById("simTierResult");
  const statusResult = document.getElementById("simStatusResult");
  const riskMeterFill = document.getElementById("simRiskMeterFill");

  function updateRiskCalc() {
    if (!scoreInput) return;
    const score = parseInt(scoreInput.value);
    const dti = parseFloat(dtiInput.value);
    const loan = parseInt(loanInput.value);

    scoreValText.textContent = score;
    dtiValText.textContent = `${dti}%`;
    loanValText.textContent = `$${loan.toLocaleString()}`;

    // Empirical logistic approximation formula for PD
    // Base log-odds adjusted by score and DTI
    const z = 4.2 - (0.01 * score) + (0.045 * dti);
    const pd = 1 / (1 + Math.exp(-z));
    const pdPct = (pd * 100).toFixed(2);

    // Expected Loss = PD * Loan Amount * LGD (assume 45% standard recovery loss)
    const el = Math.round(loan * pd * 0.45);

    pdResult.textContent = `${pdPct}%`;
    elResult.textContent = `$${el.toLocaleString()}`;

    // Risk Tiering
    let tier = "Subprime";
    let status = "⚠️ High Risk - Manual Review Required";
    let meterWidth = Math.min(100, pdPct * 3.5);

    if (score >= 760 && dti <= 30) {
      tier = "AAA (Super Prime)";
      status = "✅ Fast-Track Auto Approved";
      meterWidth = 15;
    } else if (score >= 700 && dti <= 38) {
      tier = "AA (Prime)";
      status = "✅ Approved with Standard Rate";
      meterWidth = 30;
    } else if (score >= 640 && dti <= 45) {
      tier = "A (Near Prime)";
      status = "🟡 Conditional Approval (+1.5% APR)";
      meterWidth = 55;
    } else {
      tier = "Subprime (High Risk)";
      status = "❌ Decline / Collateral Required";
      meterWidth = 88;
    }

    tierResult.textContent = tier;
    statusResult.textContent = status;
    riskMeterFill.style.width = `${meterWidth}%`;
  }

  [scoreInput, dtiInput, loanInput].forEach(inp => {
    if (inp) inp.addEventListener("input", updateRiskCalc);
  });
  updateRiskCalc();

  // Simulator 2: Adidas Profitability Explorer
  const adidasCategory = document.getElementById("adCategory");
  const adidasChannel = document.getElementById("adChannel");
  const adidasUnits = document.getElementById("adUnits");
  const adidasUnitsVal = document.getElementById("adUnitsVal");

  const adRevenue = document.getElementById("adRevenueResult");
  const adProfit = document.getElementById("adProfitResult");
  const adMargin = document.getElementById("adMarginResult");
  const adChannelShare = document.getElementById("adChannelShare");

  function updateAdidasCalc() {
    if (!adidasCategory) return;
    const cat = adidasCategory.value;
    const channel = adidasChannel.value;
    const units = parseInt(adidasUnits.value);
    adidasUnitsVal.textContent = units.toLocaleString();

    // Baseline pricing & margin dynamics from clean dataset
    let unitPrice = cat === "apparel" ? 65.0 : 52.0;
    let marginPct = cat === "apparel" ? 42.2 : 36.1;

    // Channel pricing adjustments
    if (channel === "outlet") {
      unitPrice *= 0.85;
      marginPct += 0.3; // low retail overhead
    } else if (channel === "online") {
      unitPrice *= 0.95;
      marginPct += 0.5; // DTC direct savings
    }

    const totalRev = units * unitPrice;
    const totalProfit = totalRev * (marginPct / 100);

    adRevenue.textContent = `$${Math.round(totalRev).toLocaleString()}`;
    adProfit.textContent = `$${Math.round(totalProfit).toLocaleString()}`;
    adMargin.textContent = `${marginPct.toFixed(1)}%`;

    const channelNames = {
      instore: "In-Store Retail (Flagship & Partner Malls)",
      outlet: "Outlet Center (Volume & Off-Price Clearing)",
      online: "Direct-to-Consumer Digital (Adidas App & Web)"
    };
    adChannelShare.textContent = channelNames[channel] || "Omnichannel";
  }

  [adidasCategory, adidasChannel, adidasUnits].forEach(inp => {
    if (inp) inp.addEventListener("input", updateAdidasCalc);
  });
  updateAdidasCalc();
}

/* --------------------------------------------------------------------------
   7. Animated Number Counters
   -------------------------------------------------------------------------- */
function initStatCounters() {
  const statNumbers = document.querySelectorAll(".counter-value");
  let started = false;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !started) {
        started = true;
        statNumbers.forEach(num => {
          const target = parseFloat(num.getAttribute("data-target"));
          const prefix = num.getAttribute("data-prefix") || "";
          const suffix = num.getAttribute("data-suffix") || "";
          const duration = 1800;
          const stepTime = 20;
          const steps = duration / stepTime;
          const increment = target / steps;
          let current = 0;

          const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
              current = target;
              clearInterval(timer);
            }
            num.textContent = `${prefix}${current.toLocaleString(undefined, { maximumFractionDigits: target % 1 === 0 ? 0 : 1 })}${suffix}`;
          }, stepTime);
        });
      }
    });
  }, { threshold: 0.3 });

  const statsSection = document.querySelector(".hero-stats");
  if (statsSection) observer.observe(statsSection);
}

/* --------------------------------------------------------------------------
   8. Contact Form Handling
   -------------------------------------------------------------------------- */
function initContactForm() {
  const form = document.getElementById("contactForm");
  const toast = document.getElementById("toastNotification");

  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = form.querySelector("#contactName").value.trim();
    const email = form.querySelector("#contactEmail").value.trim();
    const message = form.querySelector("#contactMessage").value.trim();

    if (!name || !email || !message) {
      showToast("Please fill out all required fields.", "error");
      return;
    }

    const submitBtn = form.querySelector("button[type='submit']");
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Sending...`;
    submitBtn.disabled = true;

    // Simulate reliable dispatch
    setTimeout(() => {
      submitBtn.innerHTML = `<i class="fas fa-check"></i> Sent Successfully!`;
      showToast(`Thank you ${name}! Your message has been sent to Sanjeet.`, "success");
      form.reset();

      setTimeout(() => {
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
      }, 3000);
    }, 1200);
  });
}

function showToast(message, type = "success") {
  let toast = document.getElementById("toastNotification");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "toastNotification";
    toast.style.cssText = `
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #0F172A;
      color: #FFFFFF;
      padding: 1rem 1.6rem;
      border-radius: 12px;
      font-weight: 600;
      box-shadow: 0 10px 30px rgba(0,0,0,0.4);
      z-index: 3000;
      display: flex;
      align-items: center;
      gap: 0.8rem;
      transition: all 0.3s ease;
      opacity: 0;
      transform: translateY(20px);
    `;
    document.body.appendChild(toast);
  }

  toast.style.borderColor = type === "success" ? "#10B981" : "#EF4444";
  toast.innerHTML = type === "success" 
    ? `<i class="fas fa-check-circle" style="color: #10B981; font-size: 1.2rem;"></i> ${message}`
    : `<i class="fas fa-exclamation-circle" style="color: #EF4444; font-size: 1.2rem;"></i> ${message}`;

  toast.style.opacity = "1";
  toast.style.transform = "translateY(0)";

  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateY(20px)";
  }, 4000);
}
