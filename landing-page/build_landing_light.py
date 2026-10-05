# build_landing_light.py
# Generates the high-end, Apple/Precision Light theme landing page for LEXUR Software Solutions,
# embedding the complete 16-partner carousel from assets/partners_section.html.

import os

# Read the partners section directly from assets
partners_file = r"f:\LEXUR CORP\landing-page\assets\partners_section.html"
with open(partners_file, "r", encoding="utf-8") as f:
    partners_html = f.read()

html_template = f'''<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LEXUR SOFTWARE SOLUTIONS — Soluciones de Software de Clase Mundial</title>
  <meta name="description" content="Diseñamos y desarrollamos soluciones de software de calidad, plataformas digitales y arquitecturas cloud para fintech, salud, logística, retail y energía.">
  <link rel="icon" type="image/png" href="./assets/lexur_brand_icon_clean.png">
  
  <!-- Premium Fonts: Plus Jakarta Sans, Inter & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- GSAP & Plugins -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              blue: '#2563EB',
              blueLight: '#3B82F6',
              purple: '#7C3AED',
              purpleLight: '#8B5CF6',
              charcoal: '#14100A',
              cream: '#FAF7F2',
              creamAlt: '#F4EFE6',
              sandBorder: '#E2D8C6',
              sandBorderDark: '#C9BC9C'
            }}
          }},
          fontFamily: {{
            sans: ['"Inter"', '"Plus Jakarta Sans"', 'sans-serif'],
            display: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          }}
        }}
      }}
    }}
  </script>

  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: #FAF7F2;
      color: #14100A;
      font-family: 'Inter', sans-serif;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    ::selection {{
      background-color: #2563EB;
      color: #FFFFFF;
    }}

    /* Continuous Marquee Animation for Partners */
    @keyframes lexurMarquee {{
      0% {{ transform: translate3d(0, 0, 0); }}
      100% {{ transform: translate3d(-50%, 0, 0); }}
    }}

    .partners-marquee-track {{
      display: flex;
      width: max-content;
      animation: lexurMarquee 42s linear infinite;
      will-change: transform;
    }}

    .partners-marquee-track:hover {{
      animation-play-state: paused;
    }}

    .partners-marquee-track.is-paused {{
      animation-play-state: paused !important;
    }}

    /* Apple Light Glass Pills */
    .glass-pill {{
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(20px) saturate(180%);
      -webkit-backdrop-filter: blur(20px) saturate(180%);
      border: 1px solid #E2D8C6;
      box-shadow: 0 4px 20px -4px rgba(20, 16, 10, 0.06);
    }}

    .card-light {{
      background: #FFFFFF;
      border: 1px solid #E2D8C6;
      border-radius: 20px;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 4px 18px -4px rgba(20, 16, 10, 0.04);
    }}

    .card-light:hover {{
      border-color: #2563EB;
      transform: translateY(-3px);
      box-shadow: 0 16px 36px -8px rgba(37, 99, 235, 0.12);
    }}

    /* Buttons */
    .btn-charcoal {{
      background: #14100A;
      color: #FFFFFF;
      font-weight: 600;
      border-radius: 9999px;
      transition: all 0.2s ease;
      box-shadow: 0 2px 10px rgba(20, 16, 10, 0.15);
    }}
    .btn-charcoal:hover {{
      background: #000000;
      transform: translateY(-1px);
      box-shadow: 0 4px 16px rgba(20, 16, 10, 0.25);
    }}

    .btn-sand {{
      background: #FFFFFF;
      color: #14100A;
      border: 1px solid #E2D8C6;
      font-weight: 600;
      border-radius: 9999px;
      transition: all 0.2s ease;
    }}
    .btn-sand:hover {{
      background: #F4EFE6;
      border-color: #C9BC9C;
      transform: translateY(-1px);
    }}

    .btn-blue-primary {{
      background: #2563EB;
      color: #FFFFFF;
      font-weight: 600;
      border-radius: 9999px;
      transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);
    }}
    .btn-blue-primary:hover {{
      background: #1D4ED8;
      transform: translateY(-1px);
      box-shadow: 0 6px 20px rgba(37, 99, 235, 0.45);
    }}

    /* Squircle Icon Boxes */
    .squircle-box {{
      width: 52px;
      height: 52px;
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.25s ease;
    }}
    .card-light:hover .squircle-box {{
      transform: scale(1.06);
    }}

    /* Terminal Syntax Highlighting */
    .terminal-light {{
      background: #10141D;
      color: #E2E8F0;
      border-radius: 18px;
      border: 1px solid rgba(255, 255, 255, 0.1);
      box-shadow: 0 20px 40px -15px rgba(20, 16, 10, 0.3);
    }}

    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: #FAF7F2;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #DDD2BD;
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #2563EB;
    }}
  </style>
</head>
<body class="selection:bg-brand-blue selection:text-white relative">

  <!-- ================= TOP FLOATING NAVBAR ================= -->
  <header class="fixed top-5 inset-x-0 z-50 flex justify-center px-4 pointer-events-none">
    <nav class="pointer-events-auto glass-pill px-5 sm:px-7 py-2.5 flex items-center justify-between gap-6 max-w-5xl w-full">
      
      <!-- Brand Logo -->
      <a href="#hero" class="flex items-center gap-3 group">
        <div class="relative w-8 h-8 flex items-center justify-center">
          <img src="./assets/lexur_brand_icon_clean.png" alt="LEXUR Icon" class="w-7 h-auto object-contain transition-transform duration-300 group-hover:scale-110">
        </div>
        <div class="flex flex-col text-left">
          <span class="font-display font-extrabold text-base tracking-wide text-brand-charcoal leading-none">LEXUR</span>
          <span class="font-mono text-[9px] uppercase tracking-widest text-neutral-500 font-semibold mt-0.5">Software Solutions</span>
        </div>
      </a>

      <!-- Desktop Links -->
      <div class="hidden lg:flex items-center gap-7 text-xs font-semibold text-neutral-700">
        <a href="#hero" data-i18n="navHome" class="hover:text-brand-blue transition-colors">Inicio</a>
        <a href="#partners" data-i18n="navPartners" class="hover:text-brand-blue transition-colors">Partners</a>
        <a href="#why-lexur" data-i18n="navWhy" class="hover:text-brand-blue transition-colors">Por Qué LEXUR</a>
        <a href="#how-it-works" data-i18n="navProcess" class="hover:text-brand-blue transition-colors">Metodología</a>
        <a href="#services" data-i18n="navServices" class="hover:text-brand-blue transition-colors">Servicios</a>
        <a href="#sectors" data-i18n="navSectors" class="hover:text-brand-blue transition-colors">Rubros</a>
        <a href="#facilities" data-i18n="navFacilities" class="hover:text-brand-blue transition-colors">Sedes</a>
      </div>

      <!-- Actions -->
      <div class="flex items-center gap-3">
        <!-- Language Switcher -->
        <div class="flex items-center bg-[#F2EDE2] border border-[#DDD2BD] rounded-full p-0.5 text-[10px] font-mono font-bold tracking-wider" role="group">
          <button id="langBtnEs" onclick="setLanguage('es')" class="px-2.5 py-1 rounded-full transition-all bg-brand-charcoal text-white font-bold">ES</button>
          <button id="langBtnEn" onclick="setLanguage('en')" class="px-2.5 py-1 rounded-full transition-all text-neutral-600 hover:text-black font-bold">EN</button>
        </div>

        <!-- CTA Button -->
        <button onclick="openProjectDrawer()" data-i18n="navCta" class="btn-blue-primary text-xs font-bold px-5 py-2.5 whitespace-nowrap">
          Iniciar Proyecto
        </button>

        <!-- Mobile Menu Toggle -->
        <button onclick="toggleMobileMenu()" class="lg:hidden w-8 h-8 rounded-full flex items-center justify-center text-neutral-700 hover:text-black bg-[#F2EDE2]" aria-label="Abrir Menú">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
        </button>
      </div>
    </nav>
  </header>

  <!-- Mobile Drawer -->
  <div id="mobileMenu" class="fixed inset-0 z-40 bg-[#FAF7F2]/95 backdrop-blur-2xl hidden flex-col justify-center px-8 text-center transition-all">
    <div class="flex flex-col gap-6 text-lg font-semibold text-brand-charcoal">
      <a href="#hero" onclick="toggleMobileMenu()" data-i18n="navHome">Inicio</a>
      <a href="#partners" onclick="toggleMobileMenu()" data-i18n="navPartners">Partners</a>
      <a href="#why-lexur" onclick="toggleMobileMenu()" data-i18n="navWhy">Por Qué LEXUR</a>
      <a href="#how-it-works" onclick="toggleMobileMenu()" data-i18n="navProcess">Metodología</a>
      <a href="#services" onclick="toggleMobileMenu()" data-i18n="navServices">Servicios</a>
      <a href="#sectors" onclick="toggleMobileMenu()" data-i18n="navSectors">Rubros</a>
      <a href="#facilities" onclick="toggleMobileMenu()" data-i18n="navFacilities">Sedes</a>
      <div class="pt-4">
        <button onclick="toggleMobileMenu(); openProjectDrawer();" data-i18n="navCta" class="btn-blue-primary text-sm font-bold px-8 py-3.5 w-full">
          Iniciar Proyecto
        </button>
      </div>
    </div>
  </div>

  <main class="relative z-10">

    <!-- ========================================================================= -->
    <!-- 1. HERO SECTION (LUMINOUS, BALANCED, ZERO EMPTY VOIDS)                    -->
    <!-- ========================================================================= -->
    <section id="hero" class="relative pt-32 sm:pt-40 pb-16 overflow-hidden">
      
      <!-- Subtle Decorative Wave Lines in Background -->
      <div class="absolute inset-0 pointer-events-none z-0 opacity-40">
        <svg class="w-full h-full" viewBox="0 0 1440 800" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
          <path d="M-100 350 C 300 200, 600 500, 1100 250 C 1300 150, 1500 300, 1600 280" stroke="#E2D7C3" stroke-width="1.5" stroke-dasharray="4 6"/>
          <path d="M-50 500 C 400 350, 700 650, 1200 400 C 1400 300, 1550 450, 1650 420" stroke="#DDD2BD" stroke-width="1.2"/>
        </svg>
      </div>

      <div class="relative z-10 max-w-5xl mx-auto px-6 text-center flex flex-col items-center">
        
        <!-- Status Pill Badge -->
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white border border-[#E2D8C6] shadow-xs mb-6 text-xs font-semibold text-neutral-700">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span class="text-brand-blue font-bold">LEXUR CORE v4.8</span>
          <span class="text-neutral-400">•</span>
          <span data-i18n="heroBadge">Ingeniería de Software Multirubro</span>
          <span class="text-brand-blue ml-1 font-bold">→</span>
        </div>

        <!-- Clean, Balanced Headline (2 Lines, Apple Precision) -->
        <h1 class="text-4xl sm:text-6xl md:text-7xl font-display font-extrabold tracking-tight text-brand-charcoal max-w-4xl leading-[1.08] mb-6">
          <span data-i18n="heroTitlePart1">Software de Calidad que Impulsa</span><br>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600" data-i18n="heroTitlePart2">Industrias Globales.</span>
        </h1>

        <!-- Subtitle with Refined Leading -->
        <p class="text-base sm:text-lg md:text-xl text-neutral-600 max-w-2xl font-normal leading-relaxed mb-8" data-i18n="heroSubtitle">
          En LEXUR diseñamos y construimos plataformas digitales de alto impacto, arquitecturas en la nube y sistemas críticos para fintech, salud, logística, retail y energía.
        </p>

        <!-- High-Contrast Dual Action Buttons -->
        <div class="flex flex-wrap items-center justify-center gap-4 mb-12">
          <button onclick="openProjectDrawer()" data-i18n="heroCtaConsult" class="btn-sand px-7 py-3.5 text-xs sm:text-sm font-bold flex items-center gap-2">
            <span>Agendar Consulta Técnica</span>
          </button>

          <button onclick="openProjectDrawer()" data-i18n="heroCtaStart" class="btn-blue-primary px-8 py-3.5 text-xs sm:text-sm font-bold flex items-center gap-2">
            <span data-i18n="heroCtaStartText">Iniciar Proyecto</span>
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
          </button>
        </div>

        <!-- Interactive Architecture Blueprint & Live Metrics Stage -->
        <div class="w-full max-w-4xl card-light p-6 sm:p-8 text-left shadow-lg relative group">
          <div class="flex flex-wrap items-center justify-between gap-4 pb-4 mb-5 border-b border-[#E2D8C6]">
            <div class="flex items-center gap-3">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
              <span class="font-mono text-xs font-bold text-neutral-800 tracking-wider">ECOSISTEMA DE ARQUITECTURA DISTRIBUIDA</span>
            </div>
            <div class="flex items-center gap-2 text-xs font-mono text-neutral-600">
              <span class="px-2.5 py-1 rounded-md bg-[#FAF7F2] border border-[#E2D8C6] font-semibold text-brand-blue">Go 1.24 + Rust</span>
              <span class="px-2.5 py-1 rounded-md bg-[#FAF7F2] border border-[#E2D8C6] font-semibold text-purple-700">Zero-Trust</span>
              <span class="px-2.5 py-1 rounded-md bg-[#FAF7F2] border border-[#E2D8C6] font-semibold text-emerald-700">P99 &lt; 1.2ms</span>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="p-4 rounded-xl bg-[#FAF7F2] border border-[#E2D8C6]/60">
              <span class="text-[11px] font-mono text-neutral-500 font-semibold uppercase block mb-1">Capacidad Transaccional</span>
              <span class="text-2xl font-display font-black text-brand-charcoal">148,290 req/s</span>
              <p class="text-xs text-neutral-600 mt-1">Throughput sostenido sin degradación de memoria.</p>
            </div>

            <div class="p-4 rounded-xl bg-[#FAF7F2] border border-[#E2D8C6]/60">
              <span class="text-[11px] font-mono text-neutral-500 font-semibold uppercase block mb-1">Disponibilidad en Producción</span>
              <span class="text-2xl font-display font-black text-brand-blue">99.999% SLA</span>
              <p class="text-xs text-neutral-600 mt-1">Conmutación por error multirregión en caliente.</p>
            </div>

            <div class="p-4 rounded-xl bg-[#FAF7F2] border border-[#E2D8C6]/60">
              <span class="text-[11px] font-mono text-neutral-500 font-semibold uppercase block mb-1">Cumplimiento Normativo</span>
              <span class="text-2xl font-display font-black text-emerald-600">PCI + HIPAA</span>
              <p class="text-xs text-neutral-600 mt-1">Cifrado de grado militar en tránsito y reposo.</p>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 2. ENTERPRISE PARTNERS CAROUSEL (DIRECTLY EMBEDDED FROM ASSETS)           -->
    <!-- ========================================================================= -->
    {partners_html}

    <!-- ========================================================================= -->
    <!-- 3. WHY LEXUR SECTION (3 CLEAN BENTO CARDS WITH COLOR SQUIRCLES)           -->
    <!-- ========================================================================= -->
    <section id="why-lexur" class="py-24 sm:py-32 relative bg-white border-b border-[#EAE2D2]">
      <div class="max-w-5xl mx-auto px-6">
        
        <!-- Header -->
        <div class="flex flex-col items-center text-center mb-16">
          <div class="inline-flex items-center px-3 py-1 rounded-full bg-[#FAF7F2] border border-[#E2D8C6] text-[10px] font-mono font-bold tracking-widest uppercase text-brand-blue mb-3">
            <span data-i18n="whyTag">POR QUÉ LEXUR</span>
          </div>

          <h2 class="text-3xl sm:text-4xl md:text-5xl font-display font-extrabold text-brand-charcoal tracking-tight max-w-2xl mb-3 leading-tight" data-i18n="whyTitle">
            Ingeniería de Precisión. Cero Deuda Técnica.
          </h2>

          <p class="text-neutral-600 max-w-xl text-sm sm:text-base leading-relaxed" data-i18n="whySubtitle">
            Tres razones arquitectónicas por las que líderes globales eligen a LEXUR sobre el desarrollo de software convencional.
          </p>
        </div>

        <!-- 3 Feature Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          
          <!-- Card 1: Performance -->
          <div class="card-light p-8 flex flex-col justify-between">
            <div>
              <div class="squircle-box bg-blue-50 border border-blue-200 text-brand-blue mb-6">
                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
                </svg>
              </div>

              <h3 class="text-lg font-display font-bold text-brand-charcoal mb-2" data-i18n="whyCard1Title">
                Respuesta Inmediata. En Cada Transacción.
              </h3>

              <p class="text-neutral-600 text-xs sm:text-sm leading-relaxed mb-6" data-i18n="whyCard1Desc">
                Sistemas reactivos en Go y Rust que procesan más de 100,000 transacciones por segundo con latencias P99 sub-milisegundo sostenidas.
              </p>
            </div>

            <div class="pt-4 border-t border-[#EAE2D2] flex items-center justify-between text-xs font-mono text-neutral-500 font-semibold">
              <span class="text-brand-blue font-bold">P99 &lt; 1.5ms</span>
              <span>100% Non-Blocking</span>
            </div>
          </div>

          <!-- Card 2: Industry Specialized -->
          <div class="card-light p-8 flex flex-col justify-between">
            <div>
              <div class="squircle-box bg-purple-50 border border-purple-200 text-purple-700 mb-6">
                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <line x1="2" y1="12" x2="22" y2="12"></line>
                  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                </svg>
              </div>

              <h3 class="text-lg font-display font-bold text-brand-charcoal mb-2" data-i18n="whyCard2Title">
                Software que Entiende Tu Industria.
              </h3>

              <p class="text-neutral-600 text-xs sm:text-sm leading-relaxed mb-6" data-i18n="whyCard2Desc">
                Diseñamos software nativo para cumplir normativas bancarias (PCI-DSS), salud (HIPAA) y sincronización logística en tiempo real offline-first.
              </p>
            </div>

            <div class="pt-4 border-t border-[#EAE2D2] flex items-center justify-between text-xs font-mono text-neutral-500 font-semibold">
              <span class="text-purple-700 font-bold">5 Rubros Clave</span>
              <span>Regulación Rigurosa</span>
            </div>
          </div>

          <!-- Card 3: Elastic Scale -->
          <div class="card-light p-8 flex flex-col justify-between">
            <div>
              <div class="squircle-box bg-emerald-50 border border-emerald-200 text-emerald-700 mb-6">
                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
                  <polyline points="17 6 23 6 23 12"></polyline>
                </svg>
              </div>

              <h3 class="text-lg font-display font-bold text-brand-charcoal mb-2" data-i18n="whyCard3Title">
                Escala Sin Romper tu Presupuesto.
              </h3>

              <p class="text-neutral-600 text-xs sm:text-sm leading-relaxed mb-6" data-i18n="whyCard3Desc">
                Infraestructura Cloud-Native en Kubernetes que escala automáticamente de 1,000 a millones de usuarios concurrentes sin desperdiciar recursos.
              </p>
            </div>

            <div class="pt-4 border-t border-[#EAE2D2] flex items-center justify-between text-xs font-mono text-neutral-500 font-semibold">
              <span class="text-emerald-700 font-bold">99.99% SLA</span>
              <span>-35% Costos Cloud</span>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 4. HOW IT WORKS SECTION (4 STEPS + INTERACTIVE IDE TERMINAL)               -->
    <!-- ========================================================================= -->
    <section id="how-it-works" class="py-24 sm:py-32 relative bg-[#FAF7F2] border-b border-[#EAE2D2]">
      <div class="max-w-5xl mx-auto px-6">
        
        <!-- Header -->
        <div class="flex flex-col items-center text-center mb-16">
          <div class="inline-flex items-center px-3 py-1 rounded-full bg-white border border-[#E2D8C6] text-[10px] font-mono font-bold tracking-widest uppercase text-neutral-600 mb-3">
            <span data-i18n="howTag">CÓMO TRABAJAMOS</span>
          </div>

          <h2 class="text-3xl sm:text-4xl md:text-5xl font-display font-extrabold text-brand-charcoal tracking-tight max-w-2xl mb-3 leading-tight" data-i18n="howTitle">
            De la Visión a Producción en 4 Fases Claras
          </h2>

          <p class="text-neutral-600 max-w-xl text-sm sm:text-base leading-relaxed" data-i18n="howSubtitle">
            Desde el diagnóstico arquitectónico hasta la escala global — con entregas ágiles y visibilidad total.
          </p>
        </div>

        <!-- 2-Column Split: Steps on Left, IDE Card on Right -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
          
          <!-- Column Left: The 4 Steps -->
          <div class="lg:col-span-6 flex flex-col gap-6">
            
            <!-- Step 1 -->
            <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-[#E2D8C6] shadow-xs">
              <div class="w-8 h-8 rounded-lg bg-blue-50 text-brand-blue font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5 border border-blue-200">
                01
              </div>
              <div>
                <h4 class="text-base font-display font-bold text-brand-charcoal mb-1" data-i18n="step1Title">
                  Diagnóstico & Blueprint de Arquitectura
                </h4>
                <p class="text-neutral-600 text-xs sm:text-sm leading-relaxed" data-i18n="step1Desc">
                  Mapeamos tus procesos y requerimientos específicos de tu rubro. Definimos el stack técnico, modelos de datos ACID y vectores de seguridad antes de escribir código.
                </p>
              </div>
            </div>

            <!-- Step 2 -->
            <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-[#E2D8C6] shadow-xs">
              <div class="w-8 h-8 rounded-lg bg-indigo-50 text-indigo-700 font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5 border border-indigo-200">
                02
              </div>
              <div>
                <h4 class="text-base font-display font-bold text-brand-charcoal mb-1" data-i18n="step2Title">
                  Desarrollo Modular & Sprints Quincenales
                </h4>
                <p class="text-neutral-600 text-xs sm:text-sm leading-relaxed" data-i18n="step2Desc">
                  Ingeniería ágil en Go, React, Flutter o Rust. Entregas quincenales de software funcional con pipelines CI/CD automatizados y cobertura de pruebas >85%.
                </p>
              </div>
            </div>

            <!-- Step 3 -->
            <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-[#E2D8C6] shadow-xs">
              <div class="w-8 h-8 rounded-lg bg-purple-50 text-purple-700 font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5 border border-purple-200">
                03
              </div>
              <div>
                <h4 class="text-base font-display font-bold text-brand-charcoal mb-1" data-i18n="step3Title">
                  Auditoría Zero-Trust & Pruebas de Carga
                </h4>
                <p class="text-neutral-600 text-xs sm:text-sm leading-relaxed" data-i18n="step3Desc">
                  Simulamos picos de tráfico masivo y estrés de infraestructura. Evaluamos vulnerabilidades con escáneres estáticos y aseguramos cumplimiento normativo.
                </p>
              </div>
            </div>

            <!-- Step 4 -->
            <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-[#E2D8C6] shadow-xs">
              <div class="w-8 h-8 rounded-lg bg-emerald-50 text-emerald-700 font-mono font-bold text-xs flex items-center justify-center shrink-0 mt-0.5 border border-emerald-200">
                04
              </div>
              <div>
                <h4 class="text-base font-display font-bold text-brand-charcoal mb-1" data-i18n="step4Title">
                  Despliegue Zero-Downtime & Telemetría 24/7
                </h4>
                <p class="text-neutral-600 text-xs sm:text-sm leading-relaxed" data-i18n="step4Desc">
                  Lanzamiento suave con despliegues Canary en Kubernetes. Monitoreo continuo de telemetría y soporte técnico con SLA garantizado del 99.99%.
                </p>
              </div>
            </div>

          </div>

          <!-- Column Right: The Floating Code Terminal -->
          <div class="lg:col-span-6 relative">
            <div class="terminal-light rounded-2xl p-6 text-left shadow-2xl relative">
              
              <!-- Window Dots -->
              <div class="flex items-center justify-between pb-4 mb-4 border-b border-white/10">
                <div class="flex items-center gap-1.5">
                  <span class="w-2.5 h-2.5 rounded-full bg-[#FF5F56]"></span>
                  <span class="w-2.5 h-2.5 rounded-full bg-[#FFBD2E]"></span>
                  <span class="w-2.5 h-2.5 rounded-full bg-[#27C93F]"></span>
                </div>
                <div class="text-[11px] font-mono text-slate-400 font-semibold">
                  lexur_service.go
                </div>
              </div>

              <!-- Code Content -->
              <div class="font-mono text-xs text-slate-300 leading-relaxed space-y-1.5 overflow-x-auto py-1">
                <div class="text-slate-500 text-[11px]">// 01 - Inicialización de Clúster Multirubro</div>
                <div><span class="text-purple-400 font-semibold">package</span> main</div>
                <div class="pt-1"><span class="text-blue-400 font-semibold">import</span> <span class="text-emerald-400">"github.com/lexur/core"</span></div>
                <div class="pt-1"><span class="text-purple-400 font-semibold">func</span> <span class="text-yellow-300 font-semibold">DeploySolution</span>() *core.Mesh {{</div>
                <div class="pl-4 text-slate-400">spec := core.NewArchitecture(&core.Config{{</div>
                <div class="pl-8 text-blue-300">Sectors:    []string{{<span class="text-emerald-400">"fintech"</span>, <span class="text-emerald-400">"health"</span>, <span class="text-emerald-400">"logistics"</span>}},</div>
                <div class="pl-8 text-blue-300">ZeroTrust:  <span class="text-purple-400 font-semibold">true</span>,</div>
                <div class="pl-8 text-blue-300">LatencyP99: <span class="text-emerald-400">"1.2ms"</span>,</div>
                <div class="pl-4 text-slate-400">}})</div>
                <div class="pl-4 text-purple-400 font-semibold">return <span class="text-white">spec.Initialize()</span></div>
                <div>}}</div>
              </div>

              <!-- Action Bar at Bottom -->
              <div class="mt-5 pt-3.5 border-t border-white/10 flex items-center justify-between text-xs font-mono">
                <div class="flex items-center gap-2 text-emerald-400">
                  <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                  <span>Compilación lista</span>
                </div>

                <button onclick="copyTerminalCode()" id="copyCodeBtn" class="px-3 py-1 rounded-md bg-white/10 hover:bg-white/20 text-slate-300 hover:text-white transition-colors" title="Copiar código">
                  Copiar
                </button>
              </div>

            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 5. SERVICES SECTION (6 CARDS + GSAP POPUP MODALS)                         -->
    <!-- ========================================================================= -->
    <section id="services" class="py-24 sm:py-32 relative bg-white border-b border-[#EAE2D2]">
      <div class="max-w-5xl mx-auto px-6">
        
        <!-- Header -->
        <div class="flex flex-col items-center text-center mb-16">
          <div class="inline-flex items-center px-3 py-1 rounded-full bg-[#FAF7F2] border border-[#E2D8C6] text-[10px] font-mono font-bold tracking-widest uppercase text-brand-blue mb-3">
            <span data-i18n="servicesTag">SERVICIOS DE INGENIERÍA</span>
          </div>

          <h2 class="text-3xl sm:text-4xl md:text-5xl font-display font-extrabold text-brand-charcoal tracking-tight max-w-2xl mb-3 leading-tight" data-i18n="servicesTitle">
            Soluciones de Software Construidas para Tu Industria
          </h2>

          <p class="text-neutral-600 max-w-xl text-sm sm:text-base leading-relaxed" data-i18n="servicesSubtitle">
            Desarrollo de extremo a extremo con los más rigurosos estándares técnicos. Haz clic en cualquier tarjeta para abrir la ficha técnica y entregables.
          </p>
        </div>

        <!-- 6 Services Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          
          <!-- Service 1 -->
          <div class="card-light p-7 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="font-mono text-xs font-bold text-brand-blue">01 · CORE PLATFORMS</span>
                <span class="w-2 h-2 rounded-full bg-blue-500"></span>
              </div>
              <h3 class="text-lg font-display font-bold text-brand-charcoal mb-2" data-i18n="srv1Title">Desarrollo de Software a Medida</h3>
              <p class="text-neutral-600 text-xs leading-relaxed mb-5" data-i18n="srv1Desc">
                Arquitectura de software modular, APIs REST/gRPC de alta densidad y bases de datos ACID con tipado estricto y testing automatizado.
              </p>
            </div>
            <div>
              <div class="flex flex-wrap gap-1.5 mb-5">
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">Go</span>
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">Rust</span>
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">PostgreSQL</span>
              </div>
              <button onclick="openServiceModal('software')" data-i18n="btnExploreArch" class="w-full py-2.5 rounded-xl bg-[#FAF7F2] hover:bg-brand-blue hover:text-white text-xs font-bold font-mono text-neutral-800 transition-all flex items-center justify-center gap-1.5 border border-[#E2D8C6] hover:border-brand-blue">
                <span>Explorar Arquitectura</span>
                <span>↗</span>
              </button>
            </div>
          </div>

          <!-- Service 2 -->
          <div class="card-light p-7 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="font-mono text-xs font-bold text-indigo-700">02 · CLOUD MESH</span>
                <span class="w-2 h-2 rounded-full bg-indigo-500"></span>
              </div>
              <h3 class="text-lg font-display font-bold text-brand-charcoal mb-2" data-i18n="srv2Title">Arquitectura Cloud & DevOps</h3>
              <p class="text-neutral-600 text-xs leading-relaxed mb-5" data-i18n="srv2Desc">
                Infraestructura como código (Terraform), clústeres elásticos en Kubernetes y despliegues Zero-Downtime con tolerancia a fallos.
              </p>
            </div>
            <div>
              <div class="flex flex-wrap gap-1.5 mb-5">
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">Kubernetes</span>
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">AWS</span>
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">Terraform</span>
              </div>
              <button onclick="openServiceModal('cloud')" data-i18n="btnExploreArch" class="w-full py-2.5 rounded-xl bg-[#FAF7F2] hover:bg-brand-blue hover:text-white text-xs font-bold font-mono text-neutral-800 transition-all flex items-center justify-center gap-1.5 border border-[#E2D8C6] hover:border-brand-blue">
                <span>Explorar Arquitectura</span>
                <span>↗</span>
              </button>
            </div>
          </div>

          <!-- Service 3 -->
          <div class="card-light p-7 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="font-mono text-xs font-bold text-purple-700">03 · NEURAL SYSTEMS</span>
                <span class="w-2 h-2 rounded-full bg-purple-500"></span>
              </div>
              <h3 class="text-lg font-display font-bold text-brand-charcoal mb-2" data-i18n="srv3Title">IA Cognitiva & Pipelines RAG</h3>
              <p class="text-neutral-600 text-xs leading-relaxed mb-5" data-i18n="srv3Desc">
                Integración de modelos LLM y visión computacional con bases de datos vectoriales privadas y pipelines de inferencia acelerada local.
              </p>
            </div>
            <div>
              <div class="flex flex-wrap gap-1.5 mb-5">
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">PyTorch</span>
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">vLLM</span>
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">Milvus</span>
              </div>
              <button onclick="openServiceModal('ai')" data-i18n="btnExploreArch" class="w-full py-2.5 rounded-xl bg-[#FAF7F2] hover:bg-brand-blue hover:text-white text-xs font-bold font-mono text-neutral-800 transition-all flex items-center justify-center gap-1.5 border border-[#E2D8C6] hover:border-brand-blue">
                <span>Explorar Arquitectura</span>
                <span>↗</span>
              </button>
            </div>
          </div>

          <!-- Service 4 -->
          <div class="card-light p-7 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="font-mono text-xs font-bold text-cyan-700">04 · MULTIPLATAFORMA</span>
                <span class="w-2 h-2 rounded-full bg-cyan-500"></span>
              </div>
              <h3 class="text-lg font-display font-bold text-brand-charcoal mb-2" data-i18n="srv4Title">Apps Móviles & Web Plataformas</h3>
              <p class="text-neutral-600 text-xs leading-relaxed mb-5" data-i18n="srv4Desc">
                Aplicaciones fluidas desarrolladas en Flutter, React y Swift nativo, sincronizadas en tiempo real con arquitecturas offline-first.
              </p>
            </div>
            <div>
              <div class="flex flex-wrap gap-1.5 mb-5">
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">Flutter</span>
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">Next.js</span>
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">SwiftUI</span>
              </div>
              <button onclick="openServiceModal('mobile')" data-i18n="btnExploreArch" class="w-full py-2.5 rounded-xl bg-[#FAF7F2] hover:bg-brand-blue hover:text-white text-xs font-bold font-mono text-neutral-800 transition-all flex items-center justify-center gap-1.5 border border-[#E2D8C6] hover:border-brand-blue">
                <span>Explorar Arquitectura</span>
                <span>↗</span>
              </button>
            </div>
          </div>

          <!-- Service 5 -->
          <div class="card-light p-7 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="font-mono text-xs font-bold text-emerald-700">05 · ZERO-TRUST</span>
                <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
              </div>
              <h3 class="text-lg font-display font-bold text-brand-charcoal mb-2" data-i18n="srv5Title">Ciberseguridad Defensiva & SOC2</h3>
              <p class="text-neutral-600 text-xs leading-relaxed mb-5" data-i18n="srv5Desc">
                Blindaje criptográfico en tránsito y reposo, gestión de secretos en Hardware KMS, escaneo de vulnerabilidades y cumplimiento PCI / HIPAA.
              </p>
            </div>
            <div>
              <div class="flex flex-wrap gap-1.5 mb-5">
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">Vault</span>
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">mTLS</span>
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">OAuth2</span>
              </div>
              <button onclick="openServiceModal('security')" data-i18n="btnExploreArch" class="w-full py-2.5 rounded-xl bg-[#FAF7F2] hover:bg-brand-blue hover:text-white text-xs font-bold font-mono text-neutral-800 transition-all flex items-center justify-center gap-1.5 border border-[#E2D8C6] hover:border-brand-blue">
                <span>Explorar Arquitectura</span>
                <span>↗</span>
              </button>
            </div>
          </div>

          <!-- Service 6 -->
          <div class="card-light p-7 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="font-mono text-xs font-bold text-amber-700">06 · HIGH-FREQUENCY</span>
                <span class="w-2 h-2 rounded-full bg-amber-500"></span>
              </div>
              <h3 class="text-lg font-display font-bold text-brand-charcoal mb-2" data-i18n="srv6Title">Modernización Legacy & Refactor</h3>
              <p class="text-neutral-600 text-xs leading-relaxed mb-5" data-i18n="srv6Desc">
                Desacoplamiento de monolitos antiguos a microservicios autónomos sin suspender operaciones (Strangler Pattern) y refactorización.
              </p>
            </div>
            <div>
              <div class="flex flex-wrap gap-1.5 mb-5">
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">Kafka</span>
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">Redis</span>
                <span class="px-2 py-0.5 rounded bg-[#FAF7F2] text-[10px] font-mono font-semibold text-neutral-700 border border-[#E2D8C6]">CockroachDB</span>
              </div>
              <button onclick="openServiceModal('modernization')" data-i18n="btnExploreArch" class="w-full py-2.5 rounded-xl bg-[#FAF7F2] hover:bg-brand-blue hover:text-white text-xs font-bold font-mono text-neutral-800 transition-all flex items-center justify-center gap-1.5 border border-[#E2D8C6] hover:border-brand-blue">
                <span>Explorar Arquitectura</span>
                <span>↗</span>
              </button>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 6. SECTORS MATRIX SECTION (INTERACTIVE VERTICALS)                          -->
    <!-- ========================================================================= -->
    <section id="sectors" class="py-24 sm:py-32 relative bg-[#FAF7F2] border-b border-[#EAE2D2]">
      <div class="max-w-5xl mx-auto px-6">
        
        <div class="flex flex-col items-center text-center mb-16">
          <div class="inline-flex items-center px-3 py-1 rounded-full bg-white border border-[#E2D8C6] text-[10px] font-mono font-bold tracking-widest uppercase text-brand-blue mb-3">
            <span data-i18n="sectorsTag">ESPECIALIZACIÓN SECTORIAL</span>
          </div>

          <h2 class="text-3xl sm:text-4xl md:text-5xl font-display font-extrabold text-brand-charcoal tracking-tight max-w-2xl mb-3 leading-tight" data-i18n="sectorsTitle">
            Software Hecho a la Medida de Tu Industria
          </h2>

          <p class="text-neutral-600 max-w-xl text-sm sm:text-base leading-relaxed" data-i18n="sectorsSubtitle">
            Conocimiento técnico y normativo profundo para resolver los cuellos de botella específicos de cada sector.
          </p>
        </div>

        <!-- Sector Selector Pills -->
        <div class="flex flex-wrap items-center justify-center gap-2 mb-10">
          <button id="sectorBtn_fintech" onclick="switchSector('fintech')" class="px-5 py-2.5 rounded-full font-mono text-xs font-bold transition-all bg-brand-charcoal text-white shadow-sm">
            01 · Fintech & Pagos
          </button>
          <button id="sectorBtn_health" onclick="switchSector('health')" class="px-5 py-2.5 rounded-full font-mono text-xs font-bold transition-all bg-white border border-[#E2D8C6] text-neutral-700 hover:text-black">
            02 · Healthtech & Salud
          </button>
          <button id="sectorBtn_logistics" onclick="switchSector('logistics')" class="px-5 py-2.5 rounded-full font-mono text-xs font-bold transition-all bg-white border border-[#E2D8C6] text-neutral-700 hover:text-black">
            03 · Cadena de Suministro
          </button>
          <button id="sectorBtn_retail" onclick="switchSector('retail')" class="px-5 py-2.5 rounded-full font-mono text-xs font-bold transition-all bg-white border border-[#E2D8C6] text-neutral-700 hover:text-black">
            04 · Smart Retail
          </button>
          <button id="sectorBtn_energy" onclick="switchSector('energy')" class="px-5 py-2.5 rounded-full font-mono text-xs font-bold transition-all bg-white border border-[#E2D8C6] text-neutral-700 hover:text-black">
            05 · Industria & IoT
          </button>
        </div>

        <!-- Dynamic Card -->
        <div id="sectorContentCard" class="card-light p-8 sm:p-10 transition-all bg-white">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            
            <div class="lg:col-span-7">
              <span id="sectorTag" class="text-xs font-mono font-bold text-brand-blue tracking-wider uppercase mb-2 block">
                FINANZAS & CRIPTOGRAFÍA ACID
              </span>
              <h3 id="sectorHeading" class="text-2xl font-display font-extrabold text-brand-charcoal mb-3">
                Ecosistemas Financieros y Pagos de Alta Frecuencia
              </h3>
              <p id="sectorDescription" class="text-neutral-600 text-sm leading-relaxed mb-6">
                Desarrollamos pasarelas de pago resilientes, sistemas de billeteras virtuales (wallets), conciliación contable autónoma y motores de detección de anomalías en milisegundos con total cumplimiento PCI-DSS.
              </p>

              <div id="sectorBlueprintList" class="space-y-2.5 font-mono text-xs text-neutral-700 font-semibold">
                <div class="flex items-center gap-2"><span class="text-brand-blue font-bold">01</span><span>API Gateway Distribuido (Kong / Envoy)</span></div>
                <div class="flex items-center gap-2"><span class="text-brand-blue font-bold">02</span><span>Microservicios Event-Driven (Apache Kafka + Go)</span></div>
                <div class="flex items-center gap-2"><span class="text-brand-blue font-bold">03</span><span>Base de Datos ACID Multi-Región (PostgreSQL + CockroachDB)</span></div>
                <div class="flex items-center gap-2"><span class="text-brand-blue font-bold">04</span><span>Bóveda Criptográfica HSM & Tokens Efímeros</span></div>
              </div>
            </div>

            <!-- Stats Column -->
            <div class="lg:col-span-5 bg-[#FAF7F2] p-6 rounded-xl border border-[#E2D8C6] flex flex-col gap-5">
              <div>
                <div class="text-[11px] font-mono text-neutral-500 uppercase tracking-wider mb-1 font-semibold">Disponibilidad Medida</div>
                <div id="sectorStat1" class="text-3xl font-display font-black text-brand-charcoal">99.999%</div>
              </div>
              <div>
                <div class="text-[11px] font-mono text-neutral-500 uppercase tracking-wider mb-1 font-semibold">Latencia P99 de API</div>
                <div id="sectorStat2" class="text-3xl font-display font-black text-brand-blue">&lt; 15 ms</div>
              </div>
              <div>
                <div class="text-[11px] font-mono text-neutral-500 uppercase tracking-wider mb-1 font-semibold">Estándar de Cumplimiento</div>
                <div id="sectorStat3" class="text-xl font-mono font-bold text-emerald-600">PCI-DSS L1</div>
              </div>
              <button onclick="openProjectDrawerWithSector()" class="w-full py-3 rounded-lg bg-brand-charcoal text-white text-xs font-bold hover:bg-black transition-colors">
                Consultar Solución para este Rubro →
              </button>
            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 7. GLOBAL HUBS SECTION (HEADQUARTERS CAMPUS SHOWCASE)                     -->
    <!-- ========================================================================= -->
    <section id="facilities" class="py-24 sm:py-32 relative bg-white border-b border-[#EAE2D2]">
      <div class="max-w-5xl mx-auto px-6">
        
        <div class="flex flex-col items-center text-center mb-16">
          <div class="inline-flex items-center px-3 py-1 rounded-full bg-[#FAF7F2] border border-[#E2D8C6] text-[10px] font-mono font-bold tracking-widest uppercase text-brand-blue mb-3">
            <span data-i18n="facilitiesTag">SEDES GLOBALES & HUBS</span>
          </div>

          <h2 class="text-3xl sm:text-4xl md:text-5xl font-display font-extrabold text-brand-charcoal tracking-tight max-w-2xl mb-3 leading-tight" data-i18n="facilitiesTitle">
            Infraestructura Física para Talento de Clase Mundial
          </h2>

          <p class="text-neutral-600 max-w-xl text-sm sm:text-base leading-relaxed" data-i18n="facilitiesSubtitle">
            Nuestros centros de ingeniería albergan laboratorios de cómputo distribuido, salas de simulación de ciberseguridad y espacios colaborativos.
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          
          <!-- Building Photo Container -->
          <div class="lg:col-span-7 card-light p-2 rounded-2xl overflow-hidden group">
            <div class="relative overflow-hidden rounded-xl">
              <img id="headquartersImg" src="./assets/lexur_building_apex.png" alt="Sede Central LEXUR Apex" class="w-full h-[320px] sm:h-[400px] object-cover group-hover:scale-105 transition-transform duration-700">
              <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-transparent to-transparent"></div>
              
              <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between text-xs font-mono text-white">
                <span id="headquartersCaption">Sede Central Apex — Laboratorio de Cómputo Distribuido</span>
                <span class="text-emerald-400 font-bold">● Activa 24/7</span>
              </div>
            </div>
          </div>

          <!-- Locations Details -->
          <div class="lg:col-span-5 flex flex-col gap-3.5">
            
            <div class="card-light p-5 flex items-start gap-4">
              <div class="w-8 h-8 rounded-lg bg-blue-50 text-brand-blue flex items-center justify-center font-mono font-bold text-xs shrink-0 mt-0.5 border border-blue-200">
                SF
              </div>
              <div>
                <h4 class="text-sm font-display font-bold text-brand-charcoal mb-0.5">San Francisco, USA</h4>
                <p class="text-neutral-600 text-xs leading-relaxed">
                  Hub de Arquitectura Cloud, IA Distribuida y Alianzas Estratégicas Globales.
                </p>
              </div>
            </div>

            <div class="card-light p-5 flex items-start gap-4">
              <div class="w-8 h-8 rounded-lg bg-purple-50 text-purple-700 flex items-center justify-center font-mono font-bold text-xs shrink-0 mt-0.5 border border-purple-200">
                MD
              </div>
              <div>
                <h4 class="text-sm font-display font-bold text-brand-charcoal mb-0.5">Madrid, España</h4>
                <p class="text-neutral-600 text-xs leading-relaxed">
                  Centro de Cumplimiento Regulatorio Europeo (GDPR), Ciberseguridad y Fintech.
                </p>
              </div>
            </div>

            <div class="card-light p-5 flex items-start gap-4">
              <div class="w-8 h-8 rounded-lg bg-emerald-50 text-emerald-700 flex items-center justify-center font-mono font-bold text-xs shrink-0 mt-0.5 border border-emerald-200">
                LT
              </div>
              <div>
                <h4 class="text-sm font-display font-bold text-brand-charcoal mb-0.5">LATAM Innovation Lab</h4>
                <p class="text-neutral-600 text-xs leading-relaxed">
                  Núcleo de Ingeniería Ágil, Desarrollo Multiplataforma y Operaciones Nearshore.
                </p>
              </div>
            </div>

          </div>

        </div>

      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 8. FINAL CONVERSION BANNER & FOOTER                                       -->
    <!-- ========================================================================= -->
    <section class="py-24 sm:py-32 relative bg-[#FAF7F2]">
      <div class="max-w-4xl mx-auto px-6 text-center">
        
        <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-white border border-[#E2D8C6] text-[10px] font-mono font-bold tracking-widest uppercase text-brand-blue mb-6 shadow-xs">
          <span>INICIA TU TRANSFORMACIÓN</span>
        </div>

        <h2 class="text-3xl sm:text-5xl font-display font-black text-brand-charcoal tracking-tight mb-5 leading-tight" data-i18n="ctaFinalTitle">
          ¿Listo para Construir Software de Clase Mundial?
        </h2>

        <p class="text-neutral-600 text-base sm:text-lg leading-relaxed mb-8 max-w-xl mx-auto" data-i18n="ctaFinalSubtitle">
          Cuéntanos sobre los desafíos de tu industria. Nuestros ingenieros principales diseñarán una propuesta de arquitectura técnica sin compromiso.
        </p>

        <div class="flex flex-wrap items-center justify-center gap-4">
          <button onclick="openProjectDrawer()" data-i18n="ctaFinalBtnStart" class="btn-blue-primary px-8 py-3.5 text-xs sm:text-sm font-bold flex items-center gap-2">
            <span>Iniciar Consulta de Proyecto</span>
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
          </button>
          
          <a href="#services" data-i18n="ctaFinalBtnServices" class="btn-sand px-7 py-3.5 text-xs sm:text-sm font-bold">
            <span>Explorar Servicios</span>
          </a>
        </div>

      </div>
    </section>

  </main>

  <!-- ========================================================================= -->
  <!-- FOOTER                                                                    -->
  <!-- ========================================================================= -->
  <footer class="py-14 bg-[#14100A] text-slate-300 relative z-10 text-xs">
    <div class="max-w-5xl mx-auto px-6">
      
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 pb-10 border-b border-white/10">
        
        <div class="md:col-span-5">
          <div class="flex items-center gap-2.5 mb-3">
            <img src="./assets/lexur_brand_icon_clean.png" alt="LEXUR Icon" class="w-6 h-auto object-contain brightness-150">
            <span class="font-display font-extrabold text-base tracking-wide text-white">LEXUR</span>
          </div>
          <p class="text-slate-400 text-xs leading-relaxed max-w-sm mb-3">
            Ingeniería de software de alta calidad y arquitecturas de misión crítica para empresas e industrias globales.
          </p>
          <div class="font-mono text-[10px] text-slate-500">
            © 2026 LEXUR Software Solutions Corp. Todos los derechos reservados.
          </div>
        </div>

        <div class="md:col-span-2">
          <div class="font-mono text-xs font-bold uppercase tracking-wider text-white mb-3">Navegación</div>
          <div class="flex flex-col gap-2">
            <a href="#hero" class="hover:text-white transition-colors">Inicio</a>
            <a href="#partners" class="hover:text-white transition-colors">Partners</a>
            <a href="#why-lexur" class="hover:text-white transition-colors">Por Qué LEXUR</a>
            <a href="#how-it-works" class="hover:text-white transition-colors">Metodología</a>
            <a href="#services" class="hover:text-white transition-colors">Servicios</a>
          </div>
        </div>

        <div class="md:col-span-2">
          <div class="font-mono text-xs font-bold uppercase tracking-wider text-white mb-3">Servicios</div>
          <div class="flex flex-col gap-2">
            <a href="#services" onclick="openServiceModal('software')" class="hover:text-white transition-colors">Core Systems</a>
            <a href="#services" onclick="openServiceModal('cloud')" class="hover:text-white transition-colors">Cloud & DevOps</a>
            <a href="#services" onclick="openServiceModal('ai')" class="hover:text-white transition-colors">IA Aplicada</a>
            <a href="#services" onclick="openServiceModal('security')" class="hover:text-white transition-colors">Ciberseguridad</a>
          </div>
        </div>

        <div class="md:col-span-3">
          <div class="font-mono text-xs font-bold uppercase tracking-wider text-white mb-3">Contacto Global</div>
          <div class="flex flex-col gap-1.5">
            <span class="text-slate-200">consultoria@lexur.io</span>
            <span class="text-slate-400">+1 (415) 890-5398 · San Francisco</span>
            <span class="text-slate-400">+34 91 901 8420 · Madrid</span>
          </div>
        </div>

      </div>

      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-3 font-mono text-[10px] text-slate-500">
        <div>
          ISO 27001 Certified · SOC 2 Type II Audited · PCI-DSS Compliant
        </div>
        <div class="flex items-center gap-5">
          <a href="#" class="hover:text-white transition-colors">Términos del Servicio</a>
          <a href="#" class="hover:text-white transition-colors">Privacidad</a>
          <a href="#" class="hover:text-white transition-colors">SLA de Ingeniería</a>
        </div>
      </div>

    </div>
  </footer>

  <!-- Floating Partner Telemetry Toast -->
  <div id="partnerToast" class="fixed bottom-6 right-6 z-[100] transform translate-y-20 opacity-0 transition-all duration-300 pointer-events-none">
    <div class="bg-white border border-[#E2D8C6] shadow-2xl rounded-2xl p-4 flex items-center gap-3.5 text-xs max-w-sm">
      <div class="w-9 h-9 rounded-xl bg-blue-50 text-brand-blue flex items-center justify-center font-bold text-sm shrink-0 border border-blue-200">
        ✓
      </div>
      <div>
        <div id="toastPartnerName" class="font-bold text-brand-charcoal text-xs">Partner</div>
        <div id="toastPartnerDesc" class="text-neutral-500 text-[11px] leading-snug">Integración verificada en clústeres de producción.</div>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- GSAP SERVICE POP-UP MODAL                                                 -->
  <!-- ========================================================================= -->
  <div id="serviceModal" class="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-black/80 backdrop-blur-md hidden">
    <div id="serviceModalCard" class="bg-white rounded-3xl max-w-xl w-full p-6 sm:p-8 relative border border-[#E2D8C6] shadow-2xl">
      
      <!-- Close Button -->
      <button onclick="closeServiceModal()" class="absolute top-5 right-5 w-8 h-8 rounded-full bg-[#FAF7F2] hover:bg-[#EAE2D2] flex items-center justify-center text-neutral-700 transition-colors" aria-label="Cerrar ventana">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>

      <!-- Category Tag -->
      <span id="modalCategory" class="text-xs font-mono font-bold text-brand-blue tracking-wider uppercase mb-1.5 block">
        01 · CORE PLATFORMS & BACKENDS
      </span>

      <!-- Title -->
      <h3 id="modalTitle" class="text-2xl font-display font-extrabold text-brand-charcoal mb-3">
        Desarrollo de Software a Medida
      </h3>

      <!-- Description -->
      <p id="modalDescription" class="text-neutral-600 text-xs sm:text-sm leading-relaxed mb-5">
        Ingeniería de software de nivel empresarial diseñada con los más altos estándares de rendimiento y fiabilidad.
      </p>

      <!-- Deliverables List -->
      <div class="mb-5 bg-[#FAF7F2] p-4 rounded-xl border border-[#E2D8C6]">
        <h4 class="text-[11px] font-mono font-bold uppercase text-neutral-600 tracking-wider mb-2.5">Entregables de Ingeniería & SLA</h4>
        <ul id="modalDeliverablesList" class="space-y-1.5 text-xs text-neutral-800 font-mono">
          <!-- Dynamic -->
        </ul>
      </div>

      <!-- Stack Pills -->
      <div class="mb-5">
        <h4 class="text-[11px] font-mono font-bold uppercase text-neutral-600 tracking-wider mb-2">Stack Tecnológico Implementado</h4>
        <div id="modalStackTags" class="flex flex-wrap gap-1.5">
          <!-- Dynamic -->
        </div>
      </div>

      <!-- Modal CTA -->
      <div class="flex items-center gap-3 pt-3 border-t border-[#EAE2D2]">
        <button onclick="closeServiceModal(); openProjectDrawer();" class="btn-blue-primary px-5 py-2.5 text-xs font-bold flex-1 text-center">
          Cotizar Solución con este Stack
        </button>
        <button onclick="closeServiceModal()" class="px-4 py-2.5 rounded-full text-xs font-bold text-neutral-500 hover:text-black transition-colors">
          Cerrar
        </button>
      </div>

    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- PROJECT CONSULTATION SLIDE-OUT DRAWER                                     -->
  <!-- ========================================================================= -->
  <div id="projectDrawer" class="fixed inset-0 z-[100] overflow-hidden hidden pointer-events-none">
    <div id="drawerBackdrop" onclick="closeProjectDrawer()" class="absolute inset-0 bg-black/75 backdrop-blur-sm pointer-events-auto"></div>

    <div class="absolute inset-y-0 right-0 max-w-full flex pointer-events-auto">
      <div id="drawerPanel" class="w-full max-w-md sm:max-w-lg bg-white border-l border-[#E2D8C6] p-6 sm:p-8 flex flex-col justify-between overflow-y-auto shadow-2xl relative z-10">
        
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between pb-5 border-b border-[#EAE2D2] mb-5">
            <div>
              <h3 class="text-xl font-display font-extrabold text-brand-charcoal">Consulta de Proyecto</h3>
              <p class="text-neutral-500 text-xs mt-0.5">Conecta directamente con nuestros arquitectos</p>
            </div>
            <button onclick="closeProjectDrawer()" class="w-8 h-8 rounded-full bg-[#FAF7F2] hover:bg-[#EAE2D2] flex items-center justify-center text-neutral-700" aria-label="Cerrar panel">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
          </div>

          <!-- Form -->
          <form id="consultationForm" onsubmit="handleFormSubmit(event)" class="space-y-3.5 text-xs font-mono">
            <div>
              <label class="block text-neutral-600 mb-1 font-semibold">Nombre Completo *</label>
              <input type="text" required placeholder="Alex Mercer" class="w-full bg-[#FAF7F2] border border-[#E2D8C6] rounded-xl px-3.5 py-2.5 text-neutral-900 placeholder-neutral-400 focus:outline-none focus:border-brand-blue">
            </div>

            <div>
              <label class="block text-neutral-600 mb-1 font-semibold">Correo Corporativo *</label>
              <input type="email" required placeholder="alex@empresa.com" class="w-full bg-[#FAF7F2] border border-[#E2D8C6] rounded-xl px-3.5 py-2.5 text-neutral-900 placeholder-neutral-400 focus:outline-none focus:border-brand-blue">
            </div>

            <div>
              <label class="block text-neutral-600 mb-1 font-semibold">Rubro de la Empresa</label>
              <select id="formSectorInput" class="w-full bg-[#FAF7F2] border border-[#E2D8C6] rounded-xl px-3.5 py-2.5 text-neutral-900 focus:outline-none focus:border-brand-blue">
                <option value="Fintech & Finanzas">Fintech & Finanzas</option>
                <option value="Healthtech & Salud">Healthtech & Salud</option>
                <option value="Logística & Transporte">Logística & Transporte</option>
                <option value="Retail & E-Commerce">Retail & E-Commerce</option>
                <option value="Industria & IoT">Industria & IoT</option>
                <option value="Otro Rubro">Otro Rubro</option>
              </select>
            </div>

            <div>
              <label class="block text-neutral-600 mb-1 font-semibold">Presupuesto Estimado</label>
              <select class="w-full bg-[#FAF7F2] border border-[#E2D8C6] rounded-xl px-3.5 py-2.5 text-neutral-900 focus:outline-none focus:border-brand-blue">
                <option value="15k-30k">$15,000 — $30,000 USD</option>
                <option value="30k-75k">$30,000 — $75,000 USD</option>
                <option value="75k+">$75,000+ USD (Enterprise)</option>
              </select>
            </div>

            <div>
              <label class="block text-neutral-600 mb-1 font-semibold">Descripción del Desafío</label>
              <textarea rows="3" placeholder="Necesitamos una plataforma de microservicios en Go capaz de soportar 50,000 usuarios concurrentes..." class="w-full bg-[#FAF7F2] border border-[#E2D8C6] rounded-xl px-3.5 py-2.5 text-neutral-900 placeholder-neutral-400 focus:outline-none focus:border-brand-blue resize-none"></textarea>
            </div>

            <div class="pt-2">
              <button type="submit" id="submitConsultationBtn" class="btn-blue-primary w-full py-3.5 text-xs font-bold text-center">
                Enviar Solicitud de Arquitectura →
              </button>
            </div>
          </form>

          <div id="formSuccessMessage" class="hidden mt-4 p-3.5 rounded-xl bg-emerald-50 border border-emerald-300 text-emerald-800 text-xs font-mono">
            ✓ Solicitud recibida. Un arquitecto principal de LEXUR te responderá en menos de 4 horas hábiles.
          </div>
        </div>

        <div class="pt-4 border-t border-[#EAE2D2] text-[10px] font-mono text-neutral-500">
          Acuerdo de Confidencialidad (NDA) disponible previo al inicio.
        </div>

      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT LOGIC                                                          -->
  <!-- ========================================================================= -->
  <script>
    // 1. Carousel Marquee Controls
    let isCarouselPaused = false;
    function toggleCarouselPlay() {{
      const track = document.getElementById('partnersTrack');
      const text = document.getElementById('carouselPlayText');
      const icon = document.getElementById('carouselPlayIcon');
      if (!track) return;

      isCarouselPaused = !isCarouselPaused;
      if (isCarouselPaused) {{
        track.classList.add('is-paused');
        if (text) text.textContent = 'REANUDAR';
        if (icon) icon.className = 'w-2 h-2 rounded-xs bg-emerald-600';
      }} else {{
        track.classList.remove('is-paused');
        if (text) text.textContent = 'PAUSAR';
        if (icon) icon.className = 'w-2 h-2 rounded-xs bg-neutral-600';
      }}
    }}

    function nudgeCarousel(direction) {{
      const container = document.getElementById('partnersCarouselContainer');
      if (container) {{
        container.scrollBy({{ left: direction * 280, behavior: 'smooth' }});
      }}
    }}

    function showPartnerDetail(name, role) {{
      alert(`${{name}}\\nEcosistema: ${{role}}\\nIntegración activa verificada en clústeres de producción.`);
    }}

    // 2. Sector Switcher
    const sectorData = {{
      fintech: {{
        tag: "FINANZAS & CRIPTOGRAFÍA ACID",
        title: "Ecosistemas Financieros y Pagos de Alta Frecuencia",
        desc: "Desarrollamos pasarelas de pago resilientes, sistemas de billeteras virtuales (wallets), conciliación contable autónoma y motores de detección de anomalías en milisegundos con total cumplimiento PCI-DSS.",
        stat1: "99.999%",
        stat2: "< 15 ms",
        stat3: "PCI-DSS L1",
        blueprints: [
          "01 · API Gateway Distribuido (Kong / Envoy)",
          "02 · Microservicios Event-Driven (Apache Kafka + Go)",
          "03 · Base de Datos ACID Multi-Región (PostgreSQL + CockroachDB)",
          "04 · Bóveda Criptográfica HSM & Tokens Efímeros"
        ]
      }},
      health: {{
        tag: "HEALTHTECH & INTEROPERABILIDAD HL7/FHIR",
        title: "Sistemas Hospitalarios y Plataformas Clínicas",
        desc: "Arquitecturas seguras para telemedicina, gestión de historiales médicos interoperables (FHIR), cifrado de datos de pacientes bajo estricto cumplimiento HIPAA y análisis predictivo asistido por IA.",
        stat1: "100%",
        stat2: "< 28 ms",
        stat3: "HIPAA Compliant",
        blueprints: [
          "01 · Gateway de Ingesta Interoperable HL7/FHIR",
          "02 · Cifrado Asimétrico Zero-Knowledge para Registros Médicos",
          "03 · Sistema de Notificaciones de Emergencia con Failover",
          "04 · Auditoría Inmutable de Acceso Clínico"
        ]
      }},
      logistics: {{
        tag: "CADENA DE SUMINISTRO & TELEMETRÍA IOT",
        title: "Rastreo Autónomo y Optimización de Rutas",
        desc: "Plataformas de visibilidad integral de flotas en tiempo real, ruteo dinámico con inteligencia espacial, control automatizado de inventarios y despacho inteligente con sincronización offline-first.",
        stat1: "+500K",
        stat2: "< 80 ms",
        stat3: "Offline-First",
        blueprints: [
          "01 · Broker de Mensajería MQTT para Dispositivos IoT",
          "02 · Algoritmos de Despacho y Ruteo Dinámico en Tiempo Real",
          "03 · Bases Geoespaciales PostGIS de Alta Velocidad",
          "04 · App de Conductor Nativa con Soporte 100% Offline"
        ]
      }},
      retail: {{
        tag: "COMERCIO MASIVO & ALTA CONCURRENCIA",
        title: "Comercio Electrónico y Checkout Instantáneo",
        desc: "Infraestructuras para millones de sesiones concurrentes durante campañas de alta demanda, motores de recomendación personalizados por IA, checkout en un solo clic y gestión de inventario en tiempo real.",
        stat1: "120K",
        stat2: "< 12 ms",
        stat3: "Zero Downtime",
        blueprints: [
          "01 · Frontend en Next.js Edge Cache con Vercel / Cloudflare",
          "02 · Carrito de Compras en Redis Cluster Distribuido",
          "03 · Motor de Recomendaciones Vectoriales en Tiempo Real",
          "04 · Pasarelas de Pago Multi-Adquirente con Reintentos Inteligentes"
        ]
      }},
      energy: {{
        tag: "INDUSTRIA 4.0 & TELEMETRÍA SCADA",
        title: "Automatización Industrial y Monitoreo de Redes",
        desc: "Dashboards web de control industrial y telemetría de sensores en milisegundos, algoritmos de mantenimiento predictivo y alertas tempranas para operaciones críticas de infraestructura.",
        stat1: "1.2M",
        stat2: "< 5 ms",
        stat3: "Zero-Latency",
        blueprints: [
          "01 · Ingesta de Series de Tiempo (TimescaleDB / InfluxDB)",
          "02 · WebSockets Bidireccionales para Monitoreo en Tiempo Real",
          "03 · Modelo de Detección de Falla Predictiva en Borde (Edge)",
          "04 · Protocolo Industrial OPC-UA / Modbus Conectado a la Nube"
        ]
      }}
    }};

    let activeSectorKey = 'fintech';

    function switchSector(key) {{
      activeSectorKey = key;
      const data = sectorData[key];
      if (!data) return;

      ['fintech', 'health', 'logistics', 'retail', 'energy'].forEach(k => {{
        const btn = document.getElementById(`sectorBtn_${{k}}`);
        if (k === key) {{
          btn.className = "px-5 py-2.5 rounded-full font-mono text-xs font-bold transition-all bg-brand-charcoal text-white shadow-sm";
        }} else {{
          btn.className = "px-5 py-2.5 rounded-full font-mono text-xs font-bold transition-all bg-white border border-[#E2D8C6] text-neutral-700 hover:text-black";
        }}
      }});

      const card = document.getElementById('sectorContentCard');
      gsap.to(card, {{
        opacity: 0.4,
        duration: 0.15,
        onComplete: () => {{
          document.getElementById('sectorTag').textContent = data.tag;
          document.getElementById('sectorHeading').textContent = data.title;
          document.getElementById('sectorDescription').textContent = data.desc;
          document.getElementById('sectorStat1').textContent = data.stat1;
          document.getElementById('sectorStat2').textContent = data.stat2;
          document.getElementById('sectorStat3').textContent = data.stat3;

          const listEl = document.getElementById('sectorBlueprintList');
          listEl.innerHTML = data.blueprints.map(bp => {{
            const parts = bp.split(' · ');
            return `<div class="flex items-center gap-2"><span class="text-brand-blue font-bold">${{parts[0]}}</span><span>${{parts[1]}}</span></div>`;
          }}).join('');

          gsap.to(card, {{ opacity: 1, duration: 0.25 }});
        }}
      }});
    }}

    function openProjectDrawerWithSector() {{
      openProjectDrawer();
      const select = document.getElementById('formSectorInput');
      if (select) {{
        if (activeSectorKey === 'fintech') select.value = "Fintech & Finanzas";
        if (activeSectorKey === 'health') select.value = "Healthtech & Salud";
        if (activeSectorKey === 'logistics') select.value = "Logística & Transporte";
        if (activeSectorKey === 'retail') select.value = "Retail & E-Commerce";
        if (activeSectorKey === 'energy') select.value = "Industria & IoT";
      }}
    }}

    // 3. Services Modal Popup (GSAP)
    const servicesDirectory = {{
      software: {{
        category: "01 · CORE PLATFORMS & BACKENDS",
        title: "Desarrollo de Software a Medida",
        desc: "Ingeniería de software de nivel empresarial. Diseñamos la arquitectura lógica, bases de datos optimizadas y APIs de alta densidad para soportar operaciones sin interrupciones. Cada línea de código es tipada estrictamente y sujeta a suites automatizadas de pruebas unitarias y de integración.",
        stack: ["TypeScript", "Go (Golang)", "Rust", "Next.js", "PostgreSQL", "Docker"],
        deliverables: [
          "✓ Arquitectura de software modular desacoplada y documentada en OpenAPI",
          "✓ Cobertura de pruebas automatizadas superior al 85% con pipelines CI/CD",
          "✓ Tiempos de respuesta de API P99 inferiores a 25ms bajo alta concurrencia",
          "✓ Transferencia completa de código fuente, propiedad intelectual y manuales de operación"
        ]
      }},
      cloud: {{
        category: "02 · DISTRIBUTED CLOUD MESH",
        title: "Soluciones Cloud & DevOps de Misión Crítica",
        desc: "Aprovechamos la infraestructura global de AWS, Google Cloud y Azure mediante contenedores y orquestación con Kubernetes. Implementamos infraestructura como código (Terraform / Pulumi) garantizando replicación instantánea y tolerancia a fallos zonales.",
        stack: ["Kubernetes", "AWS EKS", "Google Cloud Run", "Terraform", "ArgoCD", "Prometheus"],
        deliverables: [
          "✓ Despliegues 'Zero-Downtime' con estrategias Blue/Green o Canary",
          "✓ Monitoreo en tiempo real con alertas proactivas antes de que ocurra una degradación",
          "✓ Reducción media de costos de nube de entre 25% y 40% mediante auto-escalado eficiente",
          "✓ Respaldo automatizado y plan de recuperación ante desastres (RPO < 5min, RTO < 15min)"
        ]
      }},
      security: {{
        category: "03 · ZERO-TRUST & CYBERSECURITY",
        title: "Seguridad y Confianza Blindada",
        desc: "Incorporamos ciberseguridad desde el primer boceto de arquitectura. Implementamos el principio de privilegio mínimo (Zero-Trust), cifrado simétrico y asimétrico de última generación y auditorías de seguridad constantes para prevenir cualquier filtración de datos sensibles.",
        stack: ["HashiCorp Vault", "WAF Cloudflare", "Trivy Scanner", "SonarQube", "OAuth2 / OIDC", "mTLS"],
        deliverables: [
          "✓ Blindaje criptográfico para datos en tránsito (TLS 1.3) y en reposo (AES-256)",
          "✓ Escaneo de dependencias en cada Pull Request para eliminar CVEs antes de producción",
          "✓ Asesoría y preparación técnica para certificaciones SOC 2 Tipo II, ISO 27001 y PCI-DSS",
          "✓ Reporte formal de pruebas de penetración (pentest) ejecutadas por ingenieros certificados"
        ]
      }},
      ai: {{
        category: "04 · APPLIED NEURAL SYSTEMS",
        title: "Innovación & IA Escalable",
        desc: "Integramos capacidades de inteligencia artificial generativa y predictiva en los flujos medulares de tu empresa. Implementamos arquitecturas RAG que consultan tu documentación interna de forma segura y privada, sin compartir tus secretos industriales con terceros.",
        stack: ["Python 3.12", "PyTorch", "Milvus / Pinecone", "FastAPI", "Ollama / vLLM", "LangGraph"],
        deliverables: [
          "✓ Agentes inteligentes capaces de ejecutar acciones y procesar datos no estructurados",
          "✓ Respuestas fundamentadas en tus propias bases de datos con cita de fuentes verificable",
          "✓ Aceleración de inferencia con TensorRT y reducción de costos por token",
          "✓ Panel de auditoría de respuestas y alineamiento de seguridad para prevenir alucinaciones"
        ]
      }},
      fintech: {{
        category: "05 · TRANSACTIONAL ENGINES",
        title: "Sistemas de Alta Concurrencia & Finanzas",
        desc: "Construimos motores transaccionales que gestionan millones de operaciones sin pérdida de integridad ni inconsistencias de saldo. Utilizamos técnicas de particionamiento horizontal, memoria compartida y colas distribuidas para lograr latencias ultra-bajas.",
        stack: ["Go", "Apache Kafka", "Redis Cluster", "CockroachDB", "gRPC", "Docker"],
        deliverables: [
          "✓ Integración directa con pasarelas de pago y redes interbancarias",
          "✓ Garantía matemática ACID de no duplicidad de cobros ni transacciones huérfanas",
          "✓ Motor de conciliación contable capaz de cruzar millones de registros en minutos",
          "✓ Trazabilidad forense inmutable de cada transacción financiera"
        ]
      }},
      uiux: {{
        category: "06 · PRECISION HUMAN INTERFACES",
        title: "Experiencia Digital & UI/UX de Precisión",
        desc: "Creamos interfaces fluidas, limpias y altamente ergonómicas inspiradas en la estética y rendimiento de Apple y Tesla. Evitamos adornos innecesarios para enfocarnos en la claridad del dato, tipografía nítida y microinteracciones de 60/120 FPS que elevan la percepción de valor de tu producto.",
        stack: ["Figma Design System", "Tailwind CSS v4", "GSAP 3", "React / Next.js", "SwiftUI", "Flutter"],
        deliverables: [
          "✓ Design System completo con design tokens multiplataforma listos para producción",
          "✓ Prototipos interactivos testeados con usuarios reales antes de iniciar el código",
          "✓ Rendimiento de Core Web Vitals perfecto (LCP < 1.2s, CLS 0, INP excelente)",
          "✓ Cumplimiento estricto de accesibilidad WCAG 2.2 nivel AA"
        ]
      }}
    }};

    function openServiceModal(key) {{
      const data = servicesDirectory[key];
      if (!data) return;

      document.getElementById('modalCategory').textContent = data.category;
      document.getElementById('modalTitle').textContent = data.title;
      document.getElementById('modalDescription').textContent = data.desc;

      const stackContainer = document.getElementById('modalStackTags');
      stackContainer.innerHTML = data.stack.map(s => 
        `<span class="px-2.5 py-1 rounded-md bg-blue-50 text-brand-blue font-mono text-xs font-semibold border border-blue-200">${{s}}</span>`
      ).join('');

      const deliverablesContainer = document.getElementById('modalDeliverablesList');
      deliverablesContainer.innerHTML = data.deliverables.map(d => 
        `<li class="leading-relaxed">${{d}}</li>`
      ).join('');

      const modal = document.getElementById('serviceModal');
      const card = document.getElementById('serviceModalCard');

      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
      gsap.fromTo(card, 
        {{ scale: 0.94, y: 20 }}, 
        {{ scale: 1, y: 0, duration: 0.25, ease: "power2.out" }}
      );
    }}

    function closeServiceModal() {{
      const modal = document.getElementById('serviceModal');
      const card = document.getElementById('serviceModalCard');

      gsap.to(card, {{ scale: 0.94, y: 15, duration: 0.15, onComplete: () => {{
        modal.classList.add('hidden');
        document.body.style.overflow = '';
      }} }});
    }}

    // 4. Drawer Handling
    function openProjectDrawer() {{
      const drawer = document.getElementById('projectDrawer');
      const panel = document.getElementById('drawerPanel');

      drawer.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
      gsap.fromTo(panel, {{ x: 500 }}, {{ x: 0, duration: 0.25, ease: "power2.out" }});
    }}

    function closeProjectDrawer() {{
      const drawer = document.getElementById('projectDrawer');
      const panel = document.getElementById('drawerPanel');

      gsap.to(panel, {{ x: 500, duration: 0.2, ease: "power2.in", onComplete: () => {{
        drawer.classList.add('hidden');
        document.body.style.overflow = '';
      }} }});
    }}

    function handleFormSubmit(e) {{
      e.preventDefault();
      const btn = document.getElementById('submitConsultationBtn');
      btn.innerHTML = `<span class="animate-pulse">Transmitiendo requerimientos...</span>`;
      btn.disabled = true;

      setTimeout(() => {{
        document.getElementById('consultationForm').reset();
        document.getElementById('formSuccessMessage').classList.remove('hidden');
        btn.innerHTML = `✓ Solicitud Registrada`;
        setTimeout(() => {{
          closeProjectDrawer();
          btn.innerHTML = `Enviar Solicitud de Arquitectura →`;
          btn.disabled = false;
          document.getElementById('formSuccessMessage').classList.add('hidden');
        }}, 2000);
      }}, 800);
    }}

    function toggleMobileMenu() {{
      const menu = document.getElementById('mobileMenu');
      if (menu.classList.contains('hidden')) {{
        menu.classList.remove('hidden');
        menu.classList.add('flex');
        gsap.fromTo(menu, {{ opacity: 0, y: -15 }}, {{ opacity: 1, y: 0, duration: 0.2 }});
      }} else {{
        gsap.to(menu, {{
          opacity: 0,
          y: -15,
          duration: 0.15,
          onComplete: () => {{
            menu.classList.add('hidden');
            menu.classList.remove('flex');
          }}
        }});
      }}
    }}

    function copyTerminalCode() {{
      const code = `package main\\n\\nimport "github.com/lexur/core"\\n\\nfunc DeploySolution() *core.Mesh {{\\n  spec := core.NewArchitecture(&core.Config{{\\n    Sectors:    []string{{"fintech", "health", "logistics"}},\\n    ZeroTrust:  true,\\n    LatencyP99: "1.2ms",\\n  }})\\n  return spec.Initialize()\\n}}`;
      navigator.clipboard.writeText(code).then(() => {{
        const btn = document.getElementById('copyCodeBtn');
        const original = btn.innerHTML;
        btn.innerHTML = `<span class="text-emerald-400 font-bold">✓ Copiado</span>`;
        setTimeout(() => btn.innerHTML = original, 1600);
      }});
    }}

    // 5. Bilingual i18n
    const i18nData = {{
      es: {{
        navHome: "Inicio",
        navPartners: "Partners",
        navWhy: "Por Qué LEXUR",
        navProcess: "Metodología",
        navServices: "Servicios",
        navSectors: "Rubros",
        navFacilities: "Sedes",
        navCta: "Iniciar Proyecto",
        heroBadge: "Ingeniería de Software Multirubro",
        heroTitlePart1: "Software de Calidad que Impulsa",
        heroTitlePart2: "Industrias Globales.",
        heroSubtitle: "En LEXUR diseñamos y construimos plataformas digitales de alto impacto, arquitecturas en la nube y sistemas críticos para fintech, salud, logística, retail y energía.",
        heroCtaConsult: "Agendar Consulta Técnica",
        heroCtaStartText: "Iniciar Proyecto",
        whyTag: "POR QUÉ LEXUR",
        whyTitle: "Ingeniería de Precisión. Cero Deuda Técnica.",
        whySubtitle: "Tres razones arquitectónicas por las que líderes globales eligen a LEXUR sobre el desarrollo de software convencional.",
        whyCard1Title: "Respuesta Inmediata. En Cada Transacción.",
        whyCard1Desc: "Sistemas reactivos en Go y Rust que procesan más de 100,000 transacciones por segundo con latencias P99 sub-milisegundo sostenidas.",
        whyCard2Title: "Software que Entiende Tu Industria.",
        whyCard2Desc: "Diseñamos software nativo para cumplir normativas bancarias (PCI-DSS), salud (HIPAA) y sincronización logística en tiempo real offline-first.",
        whyCard3Title: "Escala Sin Romper tu Presupuesto.",
        whyCard3Desc: "Infraestructura Cloud-Native en Kubernetes que escala automáticamente de 1,000 a millones de usuarios concurrentes sin desperdiciar recursos.",
        howTag: "CÓMO TRABAJAMOS",
        howTitle: "De la Visión a Producción en 4 Fases Claras",
        howSubtitle: "Desde el diagnóstico arquitectónico hasta la escala global — con entregas ágiles y visibilidad total.",
        step1Title: "Diagnóstico & Blueprint de Arquitectura",
        step1Desc: "Mapeamos tus procesos y requerimientos específicos de tu rubro. Definimos el stack técnico, modelos de datos ACID y vectores de seguridad antes de escribir código.",
        step2Title: "Desarrollo Modular & Sprints Quincenales",
        step2Desc: "Ingeniería ágil en Go, React, Flutter o Rust. Entregas quincenales de software funcional con pipelines CI/CD automatizados y cobertura de pruebas >85%.",
        step3Title: "Auditoría Zero-Trust & Pruebas de Carga",
        step3Desc: "Simulamos picos de tráfico masivo y estrés de infraestructura. Evaluamos vulnerabilidades con escáneres estáticos y aseguramos cumplimiento normativo.",
        step4Title: "Despliegue Zero-Downtime & Telemetría 24/7",
        step4Desc: "Lanzamiento suave con despliegues Canary en Kubernetes. Monitoreo continuo de telemetría y soporte técnico con SLA garantizado del 99.99%.",
        servicesTag: "SERVICIOS DE INGENIERÍA",
        servicesTitle: "Soluciones de Software Construidas para Tu Industria",
        servicesSubtitle: "Desarrollo de extremo a extremo con los más rigurosos estándares técnicos. Haz clic en cualquier tarjeta para abrir la ficha técnica y entregables.",
        btnExploreArch: "Explorar Arquitectura",
        sectorsTag: "ESPECIALIZACIÓN SECTORIAL",
        sectorsTitle: "Software Hecho a la Medida de Tu Industria",
        sectorsSubtitle: "Conocimiento técnico y normativo profundo para resolver los cuellos de botella específicos de cada sector.",
        facilitiesTag: "SEDES GLOBALES & HUBS",
        facilitiesTitle: "Infraestructura Física para Talento de Clase Mundial",
        facilitiesSubtitle: "Nuestros centros de ingeniería albergan laboratorios de cómputo distribuido, salas de simulación de ciberseguridad y espacios colaborativos.",
        ctaFinalTitle: "¿Listo para Construir Software de Clase Mundial?",
        ctaFinalSubtitle: "Cuéntanos sobre los desafíos de tu industria. Nuestros ingenieros principales diseñarán una propuesta de arquitectura técnica sin compromiso.",
        ctaFinalBtnStart: "Iniciar Consulta de Proyecto",
        ctaFinalBtnServices: "Explorar Servicios"
      }},
      en: {{
        navHome: "Home",
        navPartners: "Partners",
        navWhy: "Why LEXUR",
        navProcess: "Methodology",
        navServices: "Services",
        navSectors: "Industries",
        navFacilities: "Hubs",
        navCta: "Start Project",
        heroBadge: "Multi-Industry Software Engineering",
        heroTitlePart1: "Quality Software Driving",
        heroTitlePart2: "Global Industries.",
        heroSubtitle: "At LEXUR we architect and build high-impact digital platforms, cloud infrastructure, and mission-critical systems for fintech, healthcare, logistics, retail, and energy.",
        heroCtaConsult: "Book Technical Consultation",
        heroCtaStartText: "Start Project",
        whyTag: "WHY LEXUR",
        whyTitle: "Precision Engineering. Zero Technical Debt.",
        whySubtitle: "Three architectural reasons global leaders choose LEXUR over conventional software agencies.",
        whyCard1Title: "Instant Response. Every Time.",
        whyCard1Desc: "Reactive systems in Go and Rust processing 100,000+ req/s with sub-millisecond P99 latency budgets. Zero bottlenecks or unexpected downtime.",
        whyCard2Title: "Software Tailored to Your Industry.",
        whyCard2Desc: "Native architectures built to satisfy banking compliance (PCI-DSS), healthcare standards (HIPAA), and offline-first real-time supply chain sync.",
        whyCard3Title: "Scale Without Breaking Your Budget.",
        whyCard3Desc: "Cloud-Native Kubernetes infrastructure that automatically scales from 1,000 to millions of concurrent users without wasting resources.",
        howTag: "HOW IT WORKS",
        howTitle: "From Vision to Production in 4 Clear Steps",
        howSubtitle: "From initial architecture diagnostics to global scaling — agile, predictable, and fully visible.",
        step1Title: "Diagnostics & Architecture Blueprint",
        step1Desc: "We map your industry requirements, ACID data models, and zero-trust security postures before writing a single line of code.",
        step2Title: "Modular Engineering & Bi-Weekly Sprints",
        step2Desc: "Agile sprints in Go, React, Flutter, or Rust. Bi-weekly functional deployments with automated CI/CD pipelines and >85% unit test coverage.",
        step3Title: "Zero-Trust Auditing & Stress Testing",
        step3Desc: "Massive traffic stress simulations, penetration testing, and automated security code scans prior to production sign-off.",
        step4Title: "Zero-Downtime Deployment & 24/7 Telemetry",
        step4Desc: "Smooth canary deployments on Kubernetes with continuous distributed telemetry and guaranteed 99.99% enterprise SLA.",
        servicesTag: "ENGINEERING SERVICES",
        servicesTitle: "Software Solutions Built for Your Industry",
        servicesSubtitle: "End-to-end development with the most rigorous engineering standards. Click any tile to inspect technical deliverables.",
        btnExploreArch: "Explore Architecture",
        sectorsTag: "INDUSTRY SPECIALIZATION",
        sectorsTitle: "Custom Software for High-Impact Verticals",
        sectorsSubtitle: "Deep domain expertise and compliance knowledge to solve critical operational bottlenecks.",
        facilitiesTag: "GLOBAL HUBS & CAMPUS",
        facilitiesTitle: "Physical Infrastructure for World-Class Talent",
        facilitiesSubtitle: "Our engineering centers house distributed computing labs, cybersecurity war rooms, and high-performance collaboration spaces.",
        ctaFinalTitle: "Ready to Build World-Class Software?",
        ctaFinalSubtitle: "Tell us about your industry challenges. Our principal architects will design a tailored technical proposal with zero commitment.",
        ctaFinalBtnStart: "Start Project Consultation",
        ctaFinalBtnServices: "Explore Services"
      }}
    }};

    let currentLang = 'es';

    function setLanguage(lang) {{
      currentLang = lang;
      const dict = i18nData[lang];
      if (!dict) return;

      document.querySelectorAll('[data-i18n]').forEach(el => {{
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {{
          el.textContent = dict[key];
        }}
      }});

      const btnEs = document.getElementById('langBtnEs');
      const btnEn = document.getElementById('langBtnEn');

      if (lang === 'es') {{
        btnEs.className = "px-2.5 py-1 rounded-full transition-all bg-brand-charcoal text-white font-bold";
        btnEn.className = "px-2.5 py-1 rounded-full transition-all text-neutral-600 hover:text-black font-bold";
      }} else {{
        btnEn.className = "px-2.5 py-1 rounded-full transition-all bg-brand-charcoal text-white font-bold";
        btnEs.className = "px-2.5 py-1 rounded-full transition-all text-neutral-600 hover:text-black font-bold";
      }}
    }}

    // Hash deep linking
    window.addEventListener('load', () => {{
      const hash = window.location.hash;
      if (hash.startsWith('#service-')) {{
        const key = hash.replace('#service-', '');
        if (servicesDirectory[key]) openServiceModal(key);
      }} else if (hash === '#consultoria') {{
        const drawer = document.getElementById('projectDrawer');
        const p = document.getElementById('drawerPanel');
        drawer.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
        if (p) gsap.set(p, {{ x: 0 }});
      }}
    }});
  </script>
</body>
</html>'''

with open(r"f:\LEXUR CORP\landing-page\index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Generated index.html successfully with luxury Apple light aesthetic and full partners marquee carousel!")
