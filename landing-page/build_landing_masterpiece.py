# build_landing_masterpiece.py
# High-end, pixel-perfect replication of Orbita AI aesthetic & layout,
# tailored strictly for LEXUR Software Solutions (multi-industry software engineering).

html_code = r'''<!DOCTYPE html>
<html lang="es" class="scroll-smooth dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LEXUR SOFTWARE SOLUTIONS — Software de Clase Mundial para Industrias Globales</title>
  <meta name="description" content="Diseñamos y desarrollamos soluciones de software de alta calidad, plataformas digitales y arquitecturas cloud para fintech, salud, logística, retail y energía.">
  <link rel="icon" type="image/png" href="./assets/lexur_brand_icon_clean.png">
  
  <!-- Premium Fonts: Inter & JetBrains Mono (Apple & Orbita AI typography standard) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- GSAP & Plugins -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              blue: '#2563EB',
              blueLight: '#3B82F6',
              blueGlow: '#60A5FA',
              purple: '#7C3AED',
              purpleLight: '#8B5CF6',
              dark: '#0D1117',
              black: '#05070B',
              surface: '#0B0F17'
            }
          },
          fontFamily: {
            sans: ['"Inter"', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          }
        }
      }
    }
  </script>

  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: #05070B;
      color: #F8FAFC;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    ::selection {
      background-color: #2563EB;
      color: #FFFFFF;
    }

    /* Tesla Precision Hardware Cursor */
    @media (pointer: fine) {
      body {
        cursor: none;
      }
      a, button, input, select, textarea, [role="button"] {
        cursor: none;
      }
    }

    #teslaCursorDot {
      position: fixed;
      top: 0;
      left: 0;
      width: 6px;
      height: 6px;
      background: #FFFFFF;
      border-radius: 50%;
      pointer-events: none;
      z-index: 99999;
      transform: translate(-50%, -50%);
      transition: width 0.15s ease, height 0.15s ease, background-color 0.15s ease;
      box-shadow: 0 0 10px rgba(255, 255, 255, 0.8), 0 0 20px rgba(37, 99, 235, 0.6);
    }

    #teslaCursorRing {
      position: fixed;
      top: 0;
      left: 0;
      width: 32px;
      height: 32px;
      border: 1.5px solid rgba(255, 255, 255, 0.35);
      border-radius: 50%;
      pointer-events: none;
      z-index: 99998;
      transform: translate(-50%, -50%);
      backdrop-filter: blur(1px);
    }

    .cursor-hover-active #teslaCursorDot {
      width: 8px;
      height: 8px;
      background: #3B82F6;
      box-shadow: 0 0 14px #3B82F6, 0 0 24px #7C3AED;
    }

    .cursor-hover-active #teslaCursorRing {
      width: 50px;
      height: 50px;
      border-color: rgba(59, 130, 246, 0.6);
      background-color: rgba(37, 99, 235, 0.08);
    }

    /* Ambient Dynamic Spotlight Follower */
    #ambientSpotlight {
      position: fixed;
      top: 0;
      left: 0;
      width: 600px;
      height: 600px;
      border-radius: 50%;
      pointer-events: none;
      z-index: 1;
      transform: translate(-50%, -50%);
      background: radial-gradient(circle, rgba(37, 99, 235, 0.06) 0%, rgba(124, 58, 237, 0.03) 40%, transparent 70%);
      opacity: 0.85;
      mix-blend-mode: screen;
      will-change: transform;
    }

    /* Authentic Orbita AI / Apple Liquid Glass */
    .liquid-glass-card {
      background: rgba(13, 17, 23, 0.7);
      backdrop-filter: blur(28px) saturate(180%);
      -webkit-backdrop-filter: blur(28px) saturate(180%);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 20px;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .liquid-glass-card:hover {
      background: rgba(17, 24, 38, 0.85);
      border-color: rgba(59, 130, 246, 0.3);
      transform: translateY(-3px);
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7), 0 0 30px rgba(37, 99, 235, 0.1);
    }

    .liquid-glass-pill {
      background: rgba(13, 17, 23, 0.75);
      backdrop-filter: blur(24px) saturate(180%);
      -webkit-backdrop-filter: blur(24px) saturate(180%);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 9999px;
    }

    /* Orbita Style Buttons */
    .btn-orbita-primary {
      background: #FFFFFF;
      color: #05070B;
      font-weight: 600;
      border-radius: 9999px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 2px 14px rgba(255, 255, 255, 0.2);
    }
    .btn-orbita-primary:hover {
      background: #F1F5F9;
      transform: translateY(-1px);
      box-shadow: 0 4px 22px rgba(255, 255, 255, 0.35);
    }

    .btn-orbita-secondary {
      background: rgba(255, 255, 255, 0.03);
      color: #E2E8F0;
      border: 1px solid rgba(255, 255, 255, 0.12);
      font-weight: 500;
      border-radius: 9999px;
      transition: all 0.2s ease;
    }
    .btn-orbita-secondary:hover {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.25);
      color: #FFFFFF;
      transform: translateY(-1px);
    }

    /* Glowing Squircle Icon Containers (Orbita AI 1:1) */
    .orbita-squircle {
      width: 52px;
      height: 52px;
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(13, 17, 23, 0.95);
      transition: all 0.3s ease;
    }

    .squircle-blue {
      border: 1.5px solid rgba(59, 130, 246, 0.4);
      box-shadow: 0 0 20px rgba(37, 99, 235, 0.2), inset 0 0 10px rgba(37, 99, 235, 0.1);
      color: #60A5FA;
    }
    .liquid-glass-card:hover .squircle-blue {
      border-color: rgba(96, 165, 250, 0.8);
      box-shadow: 0 0 30px rgba(37, 99, 235, 0.4), inset 0 0 15px rgba(37, 99, 235, 0.2);
      color: #FFFFFF;
    }

    .squircle-purple {
      border: 1.5px solid rgba(139, 92, 246, 0.4);
      box-shadow: 0 0 20px rgba(124, 58, 237, 0.2), inset 0 0 10px rgba(124, 58, 237, 0.1);
      color: #C084FC;
    }
    .liquid-glass-card:hover .squircle-purple {
      border-color: rgba(192, 132, 252, 0.8);
      box-shadow: 0 0 30px rgba(124, 58, 237, 0.4), inset 0 0 15px rgba(124, 58, 237, 0.2);
      color: #FFFFFF;
    }

    .squircle-cyan {
      border: 1.5px solid rgba(6, 182, 212, 0.4);
      box-shadow: 0 0 20px rgba(6, 182, 212, 0.2), inset 0 0 10px rgba(6, 182, 212, 0.1);
      color: #22D3EE;
    }
    .liquid-glass-card:hover .squircle-cyan {
      border-color: rgba(34, 211, 238, 0.8);
      box-shadow: 0 0 30px rgba(6, 182, 212, 0.4), inset 0 0 15px rgba(6, 182, 212, 0.2);
      color: #FFFFFF;
    }

    /* Modal styling */
    .liquid-glass-modal {
      background: rgba(10, 14, 22, 0.96);
      backdrop-filter: blur(40px) saturate(200%);
      -webkit-backdrop-filter: blur(40px) saturate(200%);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 28px;
      box-shadow: 0 30px 80px -20px rgba(0, 0, 0, 0.9);
    }
  </style>
</head>
<body class="bg-[#05070B] text-slate-100 selection:bg-brand-blue selection:text-white relative">

  <!-- Interactive Tesla Hardware Cursor -->
  <div id="teslaCursorDot" class="hidden md:block"></div>
  <div id="teslaCursorRing" class="hidden md:block"></div>

  <!-- Ambient Dynamic Spotlight Follower -->
  <div id="ambientSpotlight"></div>

  <!-- Subtle Constellation Canvas -->
  <canvas id="constellationCanvas" class="fixed inset-0 pointer-events-none z-0 opacity-30"></canvas>

  <!-- ========================================================================= -->
  <!-- FLOATING PILL NAVBAR (ORBITA AI STYLE)                                     -->
  <!-- ========================================================================= -->
  <header class="fixed top-5 inset-x-0 z-50 flex justify-center px-4 pointer-events-none">
    <nav class="pointer-events-auto liquid-glass-pill px-5 sm:px-7 py-2.5 flex items-center justify-between gap-6 max-w-4xl w-full shadow-lg">
      
      <!-- Brand Logo -->
      <a href="#hero" class="flex items-center gap-2.5 group">
        <div class="relative w-7 h-7 flex items-center justify-center">
          <img src="./assets/lexur_brand_icon_clean.png" alt="LEXUR Icon" class="w-6 h-auto object-contain transition-transform duration-300 group-hover:scale-110 filter drop-shadow-[0_0_10px_rgba(37,99,235,0.6)]">
        </div>
        <span class="font-semibold text-base tracking-wide text-white">LEXUR</span>
      </a>

      <!-- Desktop Links -->
      <div class="hidden md:flex items-center gap-6 text-xs font-medium text-slate-300">
        <a href="#hero" data-i18n="navHome" class="hover:text-white transition-colors">Inicio</a>
        <a href="#why-lexur" data-i18n="navWhy" class="hover:text-white transition-colors">Por Qué LEXUR</a>
        <a href="#how-it-works" data-i18n="navProcess" class="hover:text-white transition-colors">Metodología</a>
        <a href="#services" data-i18n="navServices" class="hover:text-white transition-colors">Servicios</a>
        <a href="#sectors" data-i18n="navSectors" class="hover:text-white transition-colors">Rubros</a>
        <a href="#facilities" data-i18n="navFacilities" class="hover:text-white transition-colors">Sedes</a>
      </div>

      <!-- Actions -->
      <div class="flex items-center gap-3">
        <div class="flex items-center bg-[#090D14] rounded-full p-0.5 text-[10px] font-mono font-bold tracking-wider" role="group">
          <button id="langBtnEs" onclick="setLanguage('es')" class="px-2 py-0.5 rounded-full transition-all bg-brand-blue text-white font-bold">ES</button>
          <button id="langBtnEn" onclick="setLanguage('en')" class="px-2 py-0.5 rounded-full transition-all text-slate-400 hover:text-white font-bold">EN</button>
        </div>

        <button onclick="openProjectDrawer()" data-i18n="navCta" class="btn-orbita-primary text-xs font-semibold px-4 py-2 whitespace-nowrap">
          Iniciar Proyecto
        </button>

        <button onclick="toggleMobileMenu()" class="md:hidden w-7 h-7 rounded-full flex items-center justify-center text-slate-300 hover:text-white" aria-label="Abrir Menú">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
        </button>
      </div>
    </nav>
  </header>

  <!-- Mobile Drawer -->
  <div id="mobileMenu" class="fixed inset-0 z-40 bg-black/95 backdrop-blur-2xl hidden flex-col justify-center px-8 text-center transition-all">
    <div class="flex flex-col gap-6 text-base font-semibold text-slate-200">
      <a href="#hero" onclick="toggleMobileMenu()" data-i18n="navHome">Inicio</a>
      <a href="#why-lexur" onclick="toggleMobileMenu()" data-i18n="navWhy">Por Qué LEXUR</a>
      <a href="#how-it-works" onclick="toggleMobileMenu()" data-i18n="navProcess">Metodología</a>
      <a href="#services" onclick="toggleMobileMenu()" data-i18n="navServices">Servicios</a>
      <a href="#sectors" onclick="toggleMobileMenu()" data-i18n="navSectors">Rubros</a>
      <a href="#facilities" onclick="toggleMobileMenu()" data-i18n="navFacilities">Sedes</a>
      <div class="pt-4">
        <button onclick="toggleMobileMenu(); openProjectDrawer();" data-i18n="navCta" class="btn-orbita-primary text-xs font-bold px-6 py-3 w-full">
          Iniciar Proyecto
        </button>
      </div>
    </div>
  </div>

  <main class="relative z-10">

    <!-- ========================================================================= -->
    <!-- 1. HERO SECTION (1:1 FIDELITY TO ORBITA AI AESTHETIC FOR SOFTWARE)         -->
    <!-- ========================================================================= -->
    <section id="hero" class="relative pt-28 sm:pt-36 overflow-hidden flex flex-col items-center justify-center text-center">
      
      <div class="max-w-5xl mx-auto px-6 w-full flex flex-col items-center z-10">
        
        <!-- Small Glowing Pill Badge (Orbita AI style) -->
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full liquid-glass-pill mb-5 text-[11px] font-medium text-slate-300 shadow-sm border border-white/10">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
          <span data-i18n="heroBadge">Ingeniería de Software Multirubro</span>
          <span class="text-slate-500">•</span>
          <span class="text-blue-400 hover:text-blue-300 font-semibold cursor-pointer" onclick="openProjectDrawer()">Explorar Soluciones →</span>
        </div>

        <!-- Clean, Balanced 2-Line Headline (Exact Orbita AI 1:1) -->
        <h1 class="text-3xl sm:text-5xl md:text-6xl font-semibold tracking-[-0.035em] text-white max-w-4xl mx-auto leading-[1.12] mb-5">
          <span data-i18n="heroTitleLine1">Software de Calidad que Impulsa</span><br>
          <span class="text-white" data-i18n="heroTitleLine2">Industrias Globales</span>
        </h1>

        <!-- Subtitle with Refined Leading -->
        <p class="text-sm sm:text-base md:text-lg text-slate-400 max-w-xl font-normal leading-relaxed mb-6" data-i18n="heroSubtitle">
          LEXUR diseña y construye plataformas digitales de alto impacto, arquitecturas cloud y sistemas críticos para fintech, salud, logística, retail y energía.
        </p>

        <!-- High-Contrast Dual Action Buttons (Orbita AI Style) -->
        <div class="flex items-center justify-center gap-3.5 mb-2">
          <button onclick="openProjectDrawer()" data-i18n="heroCtaConsult" class="btn-orbita-secondary px-6 py-2.5 text-xs sm:text-sm">
            Agendar Consulta
          </button>

          <button onclick="openProjectDrawer()" data-i18n="heroCtaStart" class="btn-orbita-primary px-6 py-2.5 text-xs sm:text-sm flex items-center gap-2">
            <span data-i18n="heroCtaStartText">Iniciar Proyecto</span>
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
          </button>
        </div>

      </div>

      <!-- FULL-WIDTH PANORAMIC PLANET HORIZON (ORBITA AI 1:1 REPLICATION) -->
      <div class="relative w-full overflow-hidden -mt-24 sm:-mt-36 md:-mt-48 pointer-events-none">
        <div class="relative w-full h-[520px] sm:h-[680px] md:h-[780px] flex flex-col justify-end items-center">
          
          <!-- Panoramic Earth seen from orbit -->
          <img src="./assets/lexur_hero_orbit.jpg" alt="Global Software Infrastructure" class="absolute inset-0 w-full h-full object-cover object-top filter brightness-105 contrast-110">

          <!-- Top Gradient Fade into Solid Black -->
          <div class="absolute inset-x-0 top-0 h-48 sm:h-64 bg-gradient-to-b from-[#05070B] via-[#05070B]/70 to-transparent"></div>

          <!-- Bottom Gradient Fade into Section 2 -->
          <div class="absolute inset-x-0 bottom-0 h-44 sm:h-60 bg-gradient-to-t from-[#05070B] via-[#05070B]/85 to-transparent"></div>

          <!-- Atmospheric Rim Glow (Luminous Blue & Violet) -->
          <div class="absolute inset-x-0 top-1/3 h-40 bg-radial from-blue-500/30 via-purple-500/15 to-transparent blur-3xl"></div>

          <!-- CLIENTS & SOCIAL PROOF STRIP OVERLAID ON THE HORIZON (Orbita Style) -->
          <div class="relative z-10 w-full max-w-5xl mx-auto px-6 pb-12 sm:pb-20 flex flex-col items-center text-center pointer-events-auto">
            
            <p class="text-[10px] sm:text-xs font-mono tracking-wider uppercase text-slate-400 font-medium mb-6" data-i18n="heroProofText">
              Arquitecturas en producción integradas con estándares globales
            </p>

            <div class="flex flex-wrap items-center justify-center gap-8 sm:gap-14 md:gap-18 opacity-85 hover:opacity-100 transition-opacity">
              
              <!-- Microsoft -->
              <div class="flex items-center gap-2 text-slate-300 hover:text-white transition-colors">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M1 1h10v10H1zM13 1h10v10H13zM1 13h10v10H1zM13 13h10v10H13z"/>
                </svg>
                <span class="font-medium text-xs sm:text-sm tracking-wide">Microsoft</span>
              </div>

              <!-- AWS Cloud -->
              <div class="flex items-center gap-2 text-slate-300 hover:text-white transition-colors">
                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M18.8 14.5c-2.4 1.8-5.9 2.7-9 .9-.4-.2-.8.2-.5.6 2.3 3 6.9 4 10.3 1.5.4-.3.2-.8-.8-3zm1.6-1.5c-.3-.4-1.9-.2-2.8-.1-.3 0-.3-.3-.1-.5 1.5-1.2 3.9-.9 4.3-.3.4.5-.1 3-1.6 4.3-.2.2-.5.1-.4-.2.4-.8.9-2.8.6-3.2zM12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2z"/>
                </svg>
                <span class="font-medium text-xs sm:text-sm tracking-wide">AWS Cloud</span>
              </div>

              <!-- Stripe -->
              <div class="flex items-center gap-2 text-slate-300 hover:text-white transition-colors">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M13.976 9.15c-2.172-.806-3.356-1.426-3.356-2.409 0-.831.683-1.305 1.901-1.305 2.227 0 4.515.858 6.09 1.631l.89-5.494C18.252.975 15.697.5 12.607.5 6.275.5 2.122 3.754 2.122 8.784c0 6.024 8.289 6.353 8.289 9.61 0 .993-.865 1.517-2.316 1.517-2.73 0-5.719-1.258-7.556-2.327L-.35 23.11c2.19 1.157 5.617 1.89 9.489 1.89 6.741 0 11.237-3.155 11.237-8.472 0-6.48-8.4-6.902-8.4-9.378z"/>
                </svg>
                <span class="font-medium text-xs sm:text-sm tracking-wide">Stripe</span>
              </div>

              <!-- Google Cloud -->
              <div class="flex items-center gap-2 text-slate-300 hover:text-white transition-colors">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/>
                </svg>
                <span class="font-medium text-xs sm:text-sm tracking-wide">Google Cloud</span>
              </div>

              <!-- NVIDIA -->
              <div class="flex items-center gap-2 text-slate-300 hover:text-white transition-colors">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M2.5 7.5C4.2 4.2 7.8 2 12 2s7.8 2.2 9.5 5.5l-2.4 1.4C17.8 6.2 15.1 4.5 12 4.5s-5.8 1.7-7.1 4.4L2.5 7.5zM12 7c2.8 0 5.1 2.3 5.1 5.1s-2.3 5.1-5.1 5.1-5.1-2.3-5.1-5.1S9.2 7 12 7z"/>
                </svg>
                <span class="font-medium text-xs sm:text-sm tracking-wide">NVIDIA AI</span>
              </div>

              <!-- Kubernetes -->
              <div class="hidden sm:flex items-center gap-2 text-slate-300 hover:text-white transition-colors">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M13.98 2.02a2 2 0 0 0-3.96 0L9.4 5.2a10.04 10.04 0 0 0-2.43 1L4.3 4.88a2 2 0 0 0-2.8 2.8l1.32 2.67a10.04 10.04 0 0 0-1 2.43L.02 13.98a2 2 0 0 0 0 3.96l3.2.62c.28.85.62 1.67 1 2.43l-1.32 2.67a2 2 0 0 0 2.8 2.8l2.67-1.32c.76.38 1.58.72 2.43 1l.62 3.2a2 2 0 0 0 3.96 0l.62-3.2c.85-.28 1.67-.62 2.43-1l2.67 1.32a2 2 0 0 0 2.8-2.8l-1.32-2.67c.38-.76.72-1.58 1-2.43l3.2-.62a2 2 0 0 0 0-3.96l-3.2-.62a10.04 10.04 0 0 0-1-2.43l1.32-2.67a2 2 0 0 0-2.8-2.8l-2.67 1.32a10.04 10.04 0 0 0-2.43-1l-.62-3.2z"/>
                </svg>
                <span class="font-medium text-xs sm:text-sm tracking-wide">Kubernetes</span>
              </div>

            </div>

          </div>

        </div>
      </div>

    </section>

    <!-- ========================================================================= -->
    <!-- 2. WHY LEXUR SECTION (EXACT ORBITA AI 3-CARD STRUCTURE & SQUIRCLES)       -->
    <!-- ========================================================================= -->
    <section id="why-lexur" class="py-24 sm:py-32 relative">
      <div class="max-w-5xl mx-auto px-6">
        
        <!-- Header -->
        <div class="flex flex-col items-center text-center mb-16">
          <div class="inline-flex items-center px-3 py-1 rounded-full liquid-glass-pill text-[10px] font-mono font-medium tracking-widest uppercase text-slate-400 mb-3">
            <span data-i18n="whyTag">POR QUÉ LEXUR</span>
          </div>

          <h2 class="text-3xl sm:text-4xl md:text-5xl font-semibold text-white tracking-[-0.02em] max-w-2xl mb-3 leading-tight" data-i18n="whyTitle">
            Ingeniería de Precisión. Cero Deuda Técnica.
          </h2>

          <p class="text-slate-400 max-w-xl text-sm sm:text-base leading-relaxed" data-i18n="whySubtitle">
            Tres razones arquitectónicas por las que líderes globales eligen a LEXUR sobre el desarrollo convencional.
          </p>
        </div>

        <!-- 3 Feature Cards Grid (Orbita AI 1:1) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          
          <!-- Card 1: Instant Response / Lightning -->
          <div class="liquid-glass-card p-7 flex flex-col justify-between">
            <div>
              <div class="orbita-squircle squircle-blue mb-6">
                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
                </svg>
              </div>

              <h3 class="text-lg font-semibold text-white mb-2" data-i18n="whyCard1Title">
                Respuesta Inmediata. En Cada Transacción.
              </h3>

              <p class="text-slate-400 text-xs sm:text-sm leading-relaxed" data-i18n="whyCard1Desc">
                Sistemas reactivos en Go y Rust que procesan más de 100,000 req/s con latencias P99 sub-milisegundo. Cero cuellos de botella ni caídas imprevistas.
              </p>
            </div>
          </div>

          <!-- Card 2: Specialized by Industry / Globe -->
          <div class="liquid-glass-card p-7 flex flex-col justify-between">
            <div>
              <div class="orbita-squircle squircle-purple mb-6">
                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <line x1="2" y1="12" x2="22" y2="12"></line>
                  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                </svg>
              </div>

              <h3 class="text-lg font-semibold text-white mb-2" data-i18n="whyCard2Title">
                Software que Entiende Tu Industria.
              </h3>

              <p class="text-slate-400 text-xs sm:text-sm leading-relaxed" data-i18n="whyCard2Desc">
                Arquitecturas nativas para cumplir normativas bancarias (PCI-DSS), salud (HIPAA) y sincronización logística en tiempo real offline-first.
              </p>
            </div>
          </div>

          <!-- Card 3: Elastic Scale / Growth -->
          <div class="liquid-glass-card p-7 flex flex-col justify-between">
            <div>
              <div class="orbita-squircle squircle-cyan mb-6">
                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
                  <polyline points="17 6 23 6 23 12"></polyline>
                </svg>
              </div>

              <h3 class="text-lg font-semibold text-white mb-2" data-i18n="whyCard3Title">
                Escala Sin Romper tu Equipo.
              </h3>

              <p class="text-slate-400 text-xs sm:text-sm leading-relaxed" data-i18n="whyCard3Desc">
                Infraestructura Cloud-Native en Kubernetes que escala automáticamente de 1,000 a millones de usuarios concurrentes. Código modular y tipado estricto.
              </p>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 3. HOW IT WORKS SECTION (ORBITA AI 4 STEPS + FLOATING CODE CARD)           -->
    <!-- ========================================================================= -->
    <section id="how-it-works" class="py-24 sm:py-32 relative bg-[#040609] border-y border-white/[0.04]">
      <div class="max-w-5xl mx-auto px-6">
        
        <!-- Header -->
        <div class="flex flex-col items-center text-center mb-16">
          <div class="inline-flex items-center px-3 py-1 rounded-full liquid-glass-pill text-[10px] font-mono font-medium tracking-widest uppercase text-slate-400 mb-3">
            <span data-i18n="howTag">CÓMO TRABAJAMOS</span>
          </div>

          <h2 class="text-3xl sm:text-4xl md:text-5xl font-semibold text-white tracking-[-0.02em] max-w-2xl mb-3 leading-tight" data-i18n="howTitle">
            De la Visión a Producción en 4 Fases Claras
          </h2>

          <p class="text-slate-400 max-w-xl text-sm sm:text-base leading-relaxed" data-i18n="howSubtitle">
            Desde el diagnóstico arquitectónico hasta la escala global — más rápido y predecible de lo que imaginas.
          </p>
        </div>

        <!-- 2-Column Split: Steps on Left, Floating Code Card on Right -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
          
          <!-- Column Left: The 4 Steps -->
          <div class="lg:col-span-6 flex flex-col gap-6">
            
            <!-- Step 1 -->
            <div class="flex items-start gap-4 p-3 rounded-xl transition-colors hover:bg-white/[0.02]">
              <div class="w-8 h-8 rounded-lg bg-blue-500/10 border border-blue-500/25 flex items-center justify-center text-blue-400 font-mono text-xs font-semibold shrink-0 mt-0.5">
                1
              </div>
              <div>
                <h4 class="text-base font-semibold text-white mb-1" data-i18n="step1Title">
                  1 — Conectar & Blueprint de Arquitectura
                </h4>
                <p class="text-slate-400 text-xs sm:text-sm leading-relaxed" data-i18n="step1Desc">
                  Mapeamos tus procesos y requerimientos específicos de tu rubro. Definimos el stack técnico, modelos de datos ACID y vectores de seguridad antes de escribir código.
                </p>
              </div>
            </div>

            <!-- Step 2 -->
            <div class="flex items-start gap-4 p-3 rounded-xl transition-colors hover:bg-white/[0.02]">
              <div class="w-8 h-8 rounded-lg bg-indigo-500/10 border border-indigo-500/25 flex items-center justify-center text-indigo-400 font-mono text-xs font-semibold shrink-0 mt-0.5">
                2
              </div>
              <div>
                <h4 class="text-base font-semibold text-white mb-1" data-i18n="step2Title">
                  2 — Desarrollo Modular & Sprints
                </h4>
                <p class="text-slate-400 text-xs sm:text-sm leading-relaxed" data-i18n="step2Desc">
                  Ingeniería ágil en Go, React, Flutter o Rust. Entregas quincenales de software funcional con pipelines CI/CD automatizados y cobertura de pruebas >85%.
                </p>
              </div>
            </div>

            <!-- Step 3 -->
            <div class="flex items-start gap-4 p-3 rounded-xl transition-colors hover:bg-white/[0.02]">
              <div class="w-8 h-8 rounded-lg bg-purple-500/10 border border-purple-500/25 flex items-center justify-center text-purple-400 font-mono text-xs font-semibold shrink-0 mt-0.5">
                3
              </div>
              <div>
                <h4 class="text-base font-semibold text-white mb-1" data-i18n="step3Title">
                  3 — Auditoría Zero-Trust & Pruebas de Carga
                </h4>
                <p class="text-slate-400 text-xs sm:text-sm leading-relaxed" data-i18n="step3Desc">
                  Simulamos picos de tráfico masivo y estrés de infraestructura. Evaluamos vulnerabilidades con escáneres estáticos y aseguramos cumplimiento normativo.
                </p>
              </div>
            </div>

            <!-- Step 4 -->
            <div class="flex items-start gap-4 p-3 rounded-xl transition-colors hover:bg-white/[0.02]">
              <div class="w-8 h-8 rounded-lg bg-emerald-500/10 border border-emerald-500/25 flex items-center justify-center text-emerald-400 font-mono text-xs font-semibold shrink-0 mt-0.5">
                4
              </div>
              <div>
                <h4 class="text-base font-semibold text-white mb-1" data-i18n="step4Title">
                  4 — Despliegue Zero-Downtime & Telemetría
                </h4>
                <p class="text-slate-400 text-xs sm:text-sm leading-relaxed" data-i18n="step4Desc">
                  Lanzamiento suave con despliegues Canary en Kubernetes. Monitoreo continuo de telemetría y soporte técnico con SLA garantizado del 99.99%.
                </p>
              </div>
            </div>

          </div>

          <!-- Column Right: The Floating Code Card (Exact Orbita AI Style) -->
          <div class="lg:col-span-6 relative">
            <div class="bg-[#090D14] rounded-2xl p-6 text-left border border-white/10 shadow-2xl relative">
              
              <!-- Window Dots -->
              <div class="flex items-center justify-between pb-4 mb-4 border-b border-white/5">
                <div class="flex items-center gap-1.5">
                  <span class="w-2.5 h-2.5 rounded-full bg-[#FF5F56]"></span>
                  <span class="w-2.5 h-2.5 rounded-full bg-[#FFBD2E]"></span>
                  <span class="w-2.5 h-2.5 rounded-full bg-[#27C93F]"></span>
                </div>
                <div class="text-[11px] font-mono text-slate-500">
                  lexur_service.go
                </div>
              </div>

              <!-- Code Content -->
              <div class="font-mono text-xs text-slate-300 leading-relaxed space-y-1.5 overflow-x-auto py-1">
                <div class="text-slate-500 text-[11px]">// 01 - Inicialización de Clúster Multirubro</div>
                <div><span class="text-purple-400">package</span> main</div>
                <div class="pt-1"><span class="text-blue-400">import</span> <span class="text-emerald-400">"github.com/lexur/core"</span></div>
                <div class="pt-1"><span class="text-purple-400">func</span> <span class="text-yellow-300">DeploySolution</span>() *core.Mesh {</div>
                <div class="pl-4 text-slate-400">spec := core.NewArchitecture(&core.Config{</div>
                <div class="pl-8 text-blue-300">Sectors:    []string{<span class="text-emerald-400">"fintech"</span>, <span class="text-emerald-400">"health"</span>, <span class="text-emerald-400">"logistics"</span>},</div>
                <div class="pl-8 text-blue-300">ZeroTrust:  <span class="text-purple-400">true</span>,</div>
                <div class="pl-8 text-blue-300">LatencyP99: <span class="text-emerald-400">"1.2ms"</span>,</div>
                <div class="pl-4 text-slate-400">})</div>
                <div class="pl-4 text-purple-400">return <span class="text-white">spec.Initialize()</span></div>
                <div>}</div>
              </div>

              <!-- Action Bar at Bottom -->
              <div class="mt-5 pt-3.5 border-t border-white/5 flex items-center justify-between">
                <div class="flex items-center gap-2 text-[11px] font-mono text-emerald-400">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                  <span>Compilación lista</span>
                </div>

                <div class="flex items-center gap-2">
                  <button onclick="copyTerminalCode()" id="copyCodeBtn" class="p-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-slate-400 hover:text-white transition-colors text-xs" title="Copiar código">
                    <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                  </button>
                </div>
              </div>

            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 4. SERVICES SECTION (6 LIQUID GLASS TILES + GSAP POPUP MODALS)            -->
    <!-- ========================================================================= -->
    <section id="services" class="py-24 sm:py-32 relative">
      <div class="max-w-5xl mx-auto px-6">
        
        <!-- Header -->
        <div class="flex flex-col items-center text-center mb-16">
          <div class="inline-flex items-center px-3 py-1 rounded-full liquid-glass-pill text-[10px] font-mono font-medium tracking-widest uppercase text-slate-400 mb-3">
            <span data-i18n="servicesTag">SERVICIOS DE INGENIERÍA</span>
          </div>

          <h2 class="text-3xl sm:text-4xl md:text-5xl font-semibold text-white tracking-[-0.02em] max-w-2xl mb-3 leading-tight" data-i18n="servicesTitle">
            Soluciones de Software Construidas para Tu Industria
          </h2>

          <p class="text-slate-400 max-w-xl text-sm sm:text-base leading-relaxed" data-i18n="servicesSubtitle">
            Desarrollo de extremo a extremo con los más rigurosos estándares técnicos. Haz clic en cualquier tarjeta para abrir la ficha técnica y entregables.
          </p>
        </div>

        <!-- 6 Services Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          
          <!-- Service 1: Custom Software -->
          <div class="liquid-glass-card p-6 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="font-mono text-xs font-semibold text-blue-400">01 · CORE PLATFORMS</span>
                <span class="w-1.5 h-1.5 rounded-full bg-blue-400"></span>
              </div>
              <h3 class="text-base font-semibold text-white mb-2" data-i18n="srv1Title">Desarrollo de Software a Medida</h3>
              <p class="text-slate-400 text-xs leading-relaxed mb-4" data-i18n="srv1Desc">
                Arquitectura de software modular, APIs REST/gRPC de alta densidad y bases de datos ACID con tipado estricto y testing automatizado.
              </p>
            </div>
            <div>
              <div class="flex flex-wrap gap-1.5 mb-5">
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">Go</span>
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">Rust</span>
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">PostgreSQL</span>
              </div>
              <button onclick="openServiceModal('software')" data-i18n="btnExploreArch" class="w-full py-2.5 rounded-xl bg-white/[0.04] hover:bg-brand-blue hover:text-white text-xs font-medium text-slate-300 transition-all flex items-center justify-center gap-1.5">
                <span>Explorar Arquitectura</span>
                <span>↗</span>
              </button>
            </div>
          </div>

          <!-- Service 2: Cloud Native -->
          <div class="liquid-glass-card p-6 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="font-mono text-xs font-semibold text-indigo-400">02 · CLOUD MESH</span>
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-400"></span>
              </div>
              <h3 class="text-base font-semibold text-white mb-2" data-i18n="srv2Title">Arquitectura Cloud & DevOps</h3>
              <p class="text-slate-400 text-xs leading-relaxed mb-4" data-i18n="srv2Desc">
                Infraestructura como código (Terraform), clústeres elásticos en Kubernetes y despliegues Zero-Downtime con tolerancia a fallos.
              </p>
            </div>
            <div>
              <div class="flex flex-wrap gap-1.5 mb-5">
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">Kubernetes</span>
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">AWS</span>
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">Terraform</span>
              </div>
              <button onclick="openServiceModal('cloud')" data-i18n="btnExploreArch" class="w-full py-2.5 rounded-xl bg-white/[0.04] hover:bg-brand-blue hover:text-white text-xs font-medium text-slate-300 transition-all flex items-center justify-center gap-1.5">
                <span>Explorar Arquitectura</span>
                <span>↗</span>
              </button>
            </div>
          </div>

          <!-- Service 3: Applied AI -->
          <div class="liquid-glass-card p-6 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="font-mono text-xs font-semibold text-purple-400">03 · NEURAL SYSTEMS</span>
                <span class="w-1.5 h-1.5 rounded-full bg-purple-400"></span>
              </div>
              <h3 class="text-base font-semibold text-white mb-2" data-i18n="srv3Title">IA Cognitiva & Pipelines RAG</h3>
              <p class="text-slate-400 text-xs leading-relaxed mb-4" data-i18n="srv3Desc">
                Integración de modelos LLM y visión computacional con bases de datos vectoriales privadas y pipelines de inferencia acelerada local.
              </p>
            </div>
            <div>
              <div class="flex flex-wrap gap-1.5 mb-5">
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">PyTorch</span>
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">vLLM</span>
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">Milvus</span>
              </div>
              <button onclick="openServiceModal('ai')" data-i18n="btnExploreArch" class="w-full py-2.5 rounded-xl bg-white/[0.04] hover:bg-brand-blue hover:text-white text-xs font-medium text-slate-300 transition-all flex items-center justify-center gap-1.5">
                <span>Explorar Arquitectura</span>
                <span>↗</span>
              </button>
            </div>
          </div>

          <!-- Service 4: Mobile & Web -->
          <div class="liquid-glass-card p-6 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="font-mono text-xs font-semibold text-cyan-400">04 · MULTIPLATAFORMA</span>
                <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span>
              </div>
              <h3 class="text-base font-semibold text-white mb-2" data-i18n="srv4Title">Apps Móviles & Plataformas Web</h3>
              <p class="text-slate-400 text-xs leading-relaxed mb-4" data-i18n="srv4Desc">
                Aplicaciones fluidas desarrolladas en Flutter, React y Swift nativo, sincronizadas en tiempo real con arquitecturas offline-first.
              </p>
            </div>
            <div>
              <div class="flex flex-wrap gap-1.5 mb-5">
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">Flutter</span>
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">Next.js</span>
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">SwiftUI</span>
              </div>
              <button onclick="openServiceModal('uiux')" data-i18n="btnExploreArch" class="w-full py-2.5 rounded-xl bg-white/[0.04] hover:bg-brand-blue hover:text-white text-xs font-medium text-slate-300 transition-all flex items-center justify-center gap-1.5">
                <span>Explorar Arquitectura</span>
                <span>↗</span>
              </button>
            </div>
          </div>

          <!-- Service 5: Defensive Cybersecurity -->
          <div class="liquid-glass-card p-6 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="font-mono text-xs font-semibold text-emerald-400">05 · ZERO-TRUST</span>
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
              </div>
              <h3 class="text-base font-semibold text-white mb-2" data-i18n="srv5Title">Ciberseguridad Defensiva & SOC2</h3>
              <p class="text-slate-400 text-xs leading-relaxed mb-4" data-i18n="srv5Desc">
                Blindaje criptográfico en tránsito y reposo, gestión de secretos en Hardware KMS, escaneo de vulnerabilidades y cumplimiento PCI / HIPAA.
              </p>
            </div>
            <div>
              <div class="flex flex-wrap gap-1.5 mb-5">
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">Vault</span>
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">mTLS</span>
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">OAuth2</span>
              </div>
              <button onclick="openServiceModal('security')" data-i18n="btnExploreArch" class="w-full py-2.5 rounded-xl bg-white/[0.04] hover:bg-brand-blue hover:text-white text-xs font-medium text-slate-300 transition-all flex items-center justify-center gap-1.5">
                <span>Explorar Arquitectura</span>
                <span>↗</span>
              </button>
            </div>
          </div>

          <!-- Service 6: High-Frequency & Refactor -->
          <div class="liquid-glass-card p-6 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-4">
                <span class="font-mono text-xs font-semibold text-amber-400">06 · HIGH-FREQUENCY</span>
                <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
              </div>
              <h3 class="text-base font-semibold text-white mb-2" data-i18n="srv6Title">Modernización Legacy & Refactor</h3>
              <p class="text-slate-400 text-xs leading-relaxed mb-4" data-i18n="srv6Desc">
                Desacoplamiento de monolitos antiguos a microservicios autónomos sin suspender operaciones (Strangler Pattern) y refactorización.
              </p>
            </div>
            <div>
              <div class="flex flex-wrap gap-1.5 mb-5">
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">Kafka</span>
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">Redis</span>
                <span class="px-2 py-0.5 rounded bg-white/5 text-[10px] font-mono text-slate-300">CockroachDB</span>
              </div>
              <button onclick="openServiceModal('fintech')" data-i18n="btnExploreArch" class="w-full py-2.5 rounded-xl bg-white/[0.04] hover:bg-brand-blue hover:text-white text-xs font-medium text-slate-300 transition-all flex items-center justify-center gap-1.5">
                <span>Explorar Arquitectura</span>
                <span>↗</span>
              </button>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 5. SECTORS MATRIX SECTION (INTERACTIVE VERTICALS)                          -->
    <!-- ========================================================================= -->
    <section id="sectors" class="py-24 sm:py-32 relative bg-[#040609] border-y border-white/[0.04]">
      <div class="max-w-5xl mx-auto px-6">
        
        <div class="flex flex-col items-center text-center mb-16">
          <div class="inline-flex items-center px-3 py-1 rounded-full liquid-glass-pill text-[10px] font-mono font-medium tracking-widest uppercase text-slate-400 mb-3">
            <span data-i18n="sectorsTag">ESPECIALIZACIÓN SECTORIAL</span>
          </div>

          <h2 class="text-3xl sm:text-4xl md:text-5xl font-semibold text-white tracking-[-0.02em] max-w-2xl mb-3 leading-tight" data-i18n="sectorsTitle">
            Software Hecho a la Medida de Tu Industria
          </h2>

          <p class="text-slate-400 max-w-xl text-sm sm:text-base leading-relaxed" data-i18n="sectorsSubtitle">
            Conocimiento técnico y normativo profundo para resolver los cuellos de botella específicos de cada sector.
          </p>
        </div>

        <!-- Sector Selector Pills -->
        <div class="flex flex-wrap items-center justify-center gap-2 mb-10">
          <button id="sectorBtn_fintech" onclick="switchSector('fintech')" class="px-4 py-2 rounded-full font-mono text-xs font-semibold transition-all bg-brand-blue text-white shadow-md">
            01 · Fintech & Pagos
          </button>
          <button id="sectorBtn_health" onclick="switchSector('health')" class="px-4 py-2 rounded-full font-mono text-xs font-semibold transition-all liquid-glass-pill text-slate-400 hover:text-white">
            02 · Healthtech & Salud
          </button>
          <button id="sectorBtn_logistics" onclick="switchSector('logistics')" class="px-4 py-2 rounded-full font-mono text-xs font-semibold transition-all liquid-glass-pill text-slate-400 hover:text-white">
            03 · Cadena de Suministro
          </button>
          <button id="sectorBtn_retail" onclick="switchSector('retail')" class="px-4 py-2 rounded-full font-mono text-xs font-semibold transition-all liquid-glass-pill text-slate-400 hover:text-white">
            04 · Smart Retail
          </button>
          <button id="sectorBtn_energy" onclick="switchSector('energy')" class="px-4 py-2 rounded-full font-mono text-xs font-semibold transition-all liquid-glass-pill text-slate-400 hover:text-white">
            05 · Industria & IoT
          </button>
        </div>

        <!-- Dynamic Card -->
        <div id="sectorContentCard" class="liquid-glass-card p-8 sm:p-10 transition-all">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
            
            <div class="lg:col-span-7">
              <span id="sectorTag" class="text-xs font-mono font-semibold text-blue-400 tracking-wider uppercase mb-2 block">
                FINANZAS & CRIPTOGRAFÍA ACID
              </span>
              <h3 id="sectorHeading" class="text-xl sm:text-2xl font-semibold text-white mb-3">
                Ecosistemas Financieros y Pagos de Alta Frecuencia
              </h3>
              <p id="sectorDescription" class="text-slate-300 text-xs sm:text-sm leading-relaxed mb-6">
                Desarrollamos pasarelas de pago resilientes, sistemas de billeteras virtuales (wallets), conciliación contable autónoma y motores de detección de anomalías en milisegundos con total cumplimiento PCI-DSS.
              </p>

              <div id="sectorBlueprintList" class="space-y-2 font-mono text-xs text-slate-300">
                <div class="flex items-center gap-2"><span class="text-blue-400">01</span><span>API Gateway Distribuido (Kong / Envoy)</span></div>
                <div class="flex items-center gap-2"><span class="text-blue-400">02</span><span>Microservicios Event-Driven (Apache Kafka + Go)</span></div>
                <div class="flex items-center gap-2"><span class="text-blue-400">03</span><span>Base de Datos ACID Multi-Región (PostgreSQL + CockroachDB)</span></div>
                <div class="flex items-center gap-2"><span class="text-blue-400">04</span><span>Bóveda Criptográfica HSM & Tokens Efímeros</span></div>
              </div>
            </div>

            <!-- Stats Column -->
            <div class="lg:col-span-5 bg-[#090D14] p-6 rounded-xl border border-white/5 flex flex-col gap-4">
              <div>
                <div class="text-[11px] font-mono text-slate-500 uppercase tracking-wider mb-1">Disponibilidad Medida</div>
                <div id="sectorStat1" class="text-2xl sm:text-3xl font-bold text-white">99.999%</div>
              </div>
              <div>
                <div class="text-[11px] font-mono text-slate-500 uppercase tracking-wider mb-1">Latencia P99 de API</div>
                <div id="sectorStat2" class="text-2xl sm:text-3xl font-bold text-blue-400">&lt; 15 ms</div>
              </div>
              <div>
                <div class="text-[11px] font-mono text-slate-500 uppercase tracking-wider mb-1">Estándar de Cumplimiento</div>
                <div id="sectorStat3" class="text-lg font-mono font-semibold text-emerald-400">PCI-DSS L1</div>
              </div>
              <button onclick="openProjectDrawerWithSector()" class="w-full py-2.5 rounded-lg bg-brand-blue text-white text-xs font-semibold hover:bg-blue-600 transition-colors">
                Consultar Solución para este Rubro →
              </button>
            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 6. GLOBAL HUBS SECTION (CAMPUS ARCHITECTURE SHOWCASE)                     -->
    <!-- ========================================================================= -->
    <section id="facilities" class="py-24 sm:py-32 relative">
      <div class="max-w-5xl mx-auto px-6">
        
        <div class="flex flex-col items-center text-center mb-16">
          <div class="inline-flex items-center px-3 py-1 rounded-full liquid-glass-pill text-[10px] font-mono font-medium tracking-widest uppercase text-slate-400 mb-3">
            <span data-i18n="facilitiesTag">SEDES GLOBALES & HUBS</span>
          </div>

          <h2 class="text-3xl sm:text-4xl md:text-5xl font-semibold text-white tracking-[-0.02em] max-w-2xl mb-3 leading-tight" data-i18n="facilitiesTitle">
            Infraestructura Física para Talento de Clase Mundial
          </h2>

          <p class="text-slate-400 max-w-xl text-sm sm:text-base leading-relaxed" data-i18n="facilitiesSubtitle">
            Nuestros centros de ingeniería albergan laboratorios de cómputo distribuido, salas de simulación de ciberseguridad y espacios colaborativos.
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          
          <!-- Building Photo Container -->
          <div class="lg:col-span-7 liquid-glass-card p-2 rounded-2xl overflow-hidden group">
            <div class="relative overflow-hidden rounded-xl">
              <img id="headquartersImg" src="./assets/lexur_building_apex.png" alt="Sede Central LEXUR Apex" class="w-full h-[280px] sm:h-[360px] object-cover filter brightness-95 contrast-105 group-hover:scale-105 transition-transform duration-700">
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
              
              <div class="absolute bottom-3 left-4 right-4 flex items-center justify-between text-xs font-mono text-slate-300">
                <span id="headquartersCaption">Sede Central Apex — Laboratorio de Cómputo Distribuido</span>
                <span class="text-emerald-400 font-medium">● Activa 24/7</span>
              </div>
            </div>
          </div>

          <!-- Locations Details -->
          <div class="lg:col-span-5 flex flex-col gap-3">
            
            <div class="liquid-glass-card p-5 flex items-start gap-3">
              <div class="w-7 h-7 rounded-lg bg-blue-500/10 text-blue-400 flex items-center justify-center font-mono font-semibold text-xs shrink-0 mt-0.5">
                SF
              </div>
              <div>
                <h4 class="text-sm font-semibold text-white mb-0.5">San Francisco, USA</h4>
                <p class="text-slate-400 text-xs leading-relaxed">
                  Hub de Arquitectura Cloud, IA Distribuida y Alianzas Estratégicas Globales.
                </p>
              </div>
            </div>

            <div class="liquid-glass-card p-5 flex items-start gap-3">
              <div class="w-7 h-7 rounded-lg bg-purple-500/10 text-purple-400 flex items-center justify-center font-mono font-semibold text-xs shrink-0 mt-0.5">
                MD
              </div>
              <div>
                <h4 class="text-sm font-semibold text-white mb-0.5">Madrid, España</h4>
                <p class="text-slate-400 text-xs leading-relaxed">
                  Centro de Cumplimiento Regulatorio Europeo (GDPR), Ciberseguridad y Fintech.
                </p>
              </div>
            </div>

            <div class="liquid-glass-card p-5 flex items-start gap-3">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/10 text-emerald-400 flex items-center justify-center font-mono font-semibold text-xs shrink-0 mt-0.5">
                LT
              </div>
              <div>
                <h4 class="text-sm font-semibold text-white mb-0.5">LATAM Innovation Lab</h4>
                <p class="text-slate-400 text-xs leading-relaxed">
                  Núcleo de Ingeniería Ágil, Desarrollo Multiplataforma y Operaciones Nearshore.
                </p>
              </div>
            </div>

          </div>

        </div>

      </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 7. FINAL ATMOSPHERIC CONVERSION BANNER & FOOTER                           -->
    <!-- ========================================================================= -->
    <section class="py-24 sm:py-32 relative overflow-hidden bg-gradient-to-b from-[#05070B] via-[#080D18] to-[#05070B] border-t border-white/[0.06]">
      <div class="absolute inset-x-0 bottom-0 h-96 bg-radial from-blue-600/15 via-purple-600/10 to-transparent blur-3xl pointer-events-none"></div>

      <div class="max-w-3xl mx-auto px-6 text-center relative z-10">
        
        <div class="inline-flex items-center px-3.5 py-1 rounded-full liquid-glass-pill text-[10px] font-mono font-medium tracking-widest uppercase text-slate-400 mb-6">
          <span>INICIA TU TRANSFORMACIÓN</span>
        </div>

        <h2 class="text-3xl sm:text-5xl font-semibold text-white tracking-[-0.02em] mb-4 leading-tight" data-i18n="ctaFinalTitle">
          ¿Listo para Construir Software de Clase Mundial?
        </h2>

        <p class="text-slate-400 text-sm sm:text-base leading-relaxed mb-8 max-w-xl mx-auto" data-i18n="ctaFinalSubtitle">
          Cuéntanos sobre los desafíos de tu industria. Nuestros ingenieros principales diseñarán una propuesta de arquitectura técnica sin compromiso.
        </p>

        <div class="flex items-center justify-center gap-3">
          <button onclick="openProjectDrawer()" data-i18n="ctaFinalBtnStart" class="btn-orbita-primary px-7 py-3 text-xs sm:text-sm font-semibold flex items-center gap-2">
            <span>Iniciar Consulta de Proyecto</span>
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
          </button>
          
          <a href="#services" data-i18n="ctaFinalBtnServices" class="btn-orbita-secondary px-6 py-3 text-xs sm:text-sm font-medium">
            <span>Explorar Servicios</span>
          </a>
        </div>

      </div>
    </section>

  </main>

  <!-- ========================================================================= -->
  <!-- FOOTER                                                                    -->
  <!-- ========================================================================= -->
  <footer class="py-14 bg-[#030508] border-t border-white/5 relative z-10 text-xs text-slate-500">
    <div class="max-w-5xl mx-auto px-6">
      
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 pb-10 border-b border-white/5">
        
        <div class="md:col-span-5">
          <div class="flex items-center gap-2.5 mb-3">
            <img src="./assets/lexur_brand_icon_clean.png" alt="LEXUR Icon" class="w-5 h-auto object-contain">
            <span class="font-semibold text-sm tracking-wide text-white">LEXUR</span>
          </div>
          <p class="text-slate-400 text-xs leading-relaxed max-w-sm mb-3">
            Ingeniería de software de alta calidad y arquitecturas de misión crítica para empresas e industrias globales.
          </p>
          <div class="font-mono text-[10px] text-slate-500">
            © 2026 LEXUR Software Solutions Corp. Todos los derechos reservados.
          </div>
        </div>

        <div class="md:col-span-2">
          <div class="font-mono text-xs font-semibold uppercase tracking-wider text-white mb-3">Navegación</div>
          <div class="flex flex-col gap-2">
            <a href="#hero" class="hover:text-white transition-colors">Inicio</a>
            <a href="#why-lexur" class="hover:text-white transition-colors">Por Qué LEXUR</a>
            <a href="#how-it-works" class="hover:text-white transition-colors">Metodología</a>
            <a href="#services" class="hover:text-white transition-colors">Servicios</a>
            <a href="#sectors" class="hover:text-white transition-colors">Rubros</a>
          </div>
        </div>

        <div class="md:col-span-2">
          <div class="font-mono text-xs font-semibold uppercase tracking-wider text-white mb-3">Servicios</div>
          <div class="flex flex-col gap-2">
            <a href="#services" onclick="openServiceModal('software')" class="hover:text-white transition-colors">Core Systems</a>
            <a href="#services" onclick="openServiceModal('cloud')" class="hover:text-white transition-colors">Cloud & DevOps</a>
            <a href="#services" onclick="openServiceModal('ai')" class="hover:text-white transition-colors">IA Aplicada</a>
            <a href="#services" onclick="openServiceModal('security')" class="hover:text-white transition-colors">Ciberseguridad</a>
          </div>
        </div>

        <div class="md:col-span-3">
          <div class="font-mono text-xs font-semibold uppercase tracking-wider text-white mb-3">Contacto Global</div>
          <div class="flex flex-col gap-1.5">
            <span class="text-slate-300">consultoria@lexur.io</span>
            <span class="text-slate-400">+1 (415) 890-5398 · San Francisco</span>
            <span class="text-slate-400">+34 91 901 8420 · Madrid</span>
          </div>
        </div>

      </div>

      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-3 font-mono text-[10px]">
        <div>
          ISO 27001 Certified · SOC 2 Type II Audited · PCI-DSS Compliant
        </div>
        <div class="flex items-center gap-5">
          <a href="#" class="hover:text-white transition-colors">Términos del Servicio</a>
          <a href="#" class="hover:text-white transition-colors">Política de Privacidad</a>
          <a href="#" class="hover:text-white transition-colors">SLA de Ingeniería</a>
        </div>
      </div>

    </div>
  </footer>

  <!-- ========================================================================= -->
  <!-- GSAP LIQUID GLASS SERVICE POP-UP MODAL                                    -->
  <!-- ========================================================================= -->
  <div id="serviceModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-xl hidden opacity-0 transition-opacity">
    <div id="serviceModalCard" class="liquid-glass-modal max-w-xl w-full p-6 sm:p-8 relative">
      
      <!-- Close Button -->
      <button onclick="closeServiceModal()" class="absolute top-5 right-5 w-7 h-7 rounded-full bg-white/5 hover:bg-white/15 flex items-center justify-center text-slate-300 hover:text-white transition-colors" aria-label="Cerrar ventana">
        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>

      <!-- Category Tag -->
      <span id="modalCategory" class="text-xs font-mono font-semibold text-blue-400 tracking-wider uppercase mb-1.5 block">
        01 · CORE PLATFORMS & BACKENDS
      </span>

      <!-- Title -->
      <h3 id="modalTitle" class="text-xl sm:text-2xl font-semibold text-white mb-3">
        Desarrollo de Software a Medida
      </h3>

      <!-- Description -->
      <p id="modalDescription" class="text-slate-300 text-xs sm:text-sm leading-relaxed mb-5">
        Ingeniería de software de nivel empresarial diseñada con los más altos estándares de rendimiento y fiabilidad.
      </p>

      <!-- Deliverables List -->
      <div class="mb-5 bg-[#090D14] p-4 rounded-xl border border-white/5">
        <h4 class="text-[11px] font-mono font-semibold uppercase text-slate-400 tracking-wider mb-2.5">Entregables de Ingeniería & SLA</h4>
        <ul id="modalDeliverablesList" class="space-y-1.5 text-xs text-slate-300 font-mono">
          <!-- Dynamic -->
        </ul>
      </div>

      <!-- Stack Pills -->
      <div class="mb-5">
        <h4 class="text-[11px] font-mono font-semibold uppercase text-slate-400 tracking-wider mb-2">Stack Tecnológico Implementado</h4>
        <div id="modalStackTags" class="flex flex-wrap gap-1.5">
          <!-- Dynamic -->
        </div>
      </div>

      <!-- Modal CTA -->
      <div class="flex items-center gap-3 pt-3 border-t border-white/5">
        <button onclick="closeServiceModal(); openProjectDrawer();" class="btn-orbita-primary px-5 py-2.5 text-xs font-semibold flex-1 text-center">
          Cotizar Solución con este Stack
        </button>
        <button onclick="closeServiceModal()" class="px-4 py-2.5 rounded-full text-xs font-medium text-slate-400 hover:text-white transition-colors">
          Cerrar
        </button>
      </div>

    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- PROJECT CONSULTATION SLIDE-OUT DRAWER                                     -->
  <!-- ========================================================================= -->
  <div id="projectDrawer" class="fixed inset-0 z-50 overflow-hidden hidden pointer-events-none">
    <div id="drawerBackdrop" onclick="closeProjectDrawer()" class="absolute inset-0 bg-black/80 backdrop-blur-md opacity-0 transition-opacity pointer-events-auto"></div>

    <div class="absolute inset-y-0 right-0 max-w-full flex pl-10 pointer-events-auto">
      <div id="drawerPanel" class="w-screen max-w-md bg-[#090D14] border-l border-white/10 p-6 sm:p-8 flex flex-col justify-between overflow-y-auto transform translate-x-full transition-transform duration-300">
        
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between pb-5 border-b border-white/5 mb-5">
            <div>
              <h3 class="text-lg font-semibold text-white">Consulta de Proyecto</h3>
              <p class="text-slate-400 text-xs mt-0.5">Conecta directamente con nuestros arquitectos</p>
            </div>
            <button onclick="closeProjectDrawer()" class="w-7 h-7 rounded-full bg-white/5 hover:bg-white/15 flex items-center justify-center text-slate-300 hover:text-white" aria-label="Cerrar panel">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
          </div>

          <!-- Form -->
          <form id="consultationForm" onsubmit="handleFormSubmit(event)" class="space-y-3.5 text-xs font-mono">
            <div>
              <label class="block text-slate-400 mb-1">Nombre Completo *</label>
              <input type="text" required placeholder="Alex Mercer" class="w-full bg-[#111722] border border-white/10 rounded-xl px-3.5 py-2 text-white placeholder-slate-500 focus:outline-none focus:border-brand-blue">
            </div>

            <div>
              <label class="block text-slate-400 mb-1">Correo Corporativo *</label>
              <input type="email" required placeholder="alex@empresa.com" class="w-full bg-[#111722] border border-white/10 rounded-xl px-3.5 py-2 text-white placeholder-slate-500 focus:outline-none focus:border-brand-blue">
            </div>

            <div>
              <label class="block text-slate-400 mb-1">Rubro de la Empresa</label>
              <select id="formSectorInput" class="w-full bg-[#111722] border border-white/10 rounded-xl px-3.5 py-2 text-white focus:outline-none focus:border-brand-blue">
                <option value="Fintech & Finanzas">Fintech & Finanzas</option>
                <option value="Healthtech & Salud">Healthtech & Salud</option>
                <option value="Logística & Transporte">Logística & Transporte</option>
                <option value="Retail & E-Commerce">Retail & E-Commerce</option>
                <option value="Industria & IoT">Industria & IoT</option>
                <option value="Otro Rubro">Otro Rubro</option>
              </select>
            </div>

            <div>
              <label class="block text-slate-400 mb-1">Presupuesto Estimado</label>
              <select class="w-full bg-[#111722] border border-white/10 rounded-xl px-3.5 py-2 text-white focus:outline-none focus:border-brand-blue">
                <option value="15k-30k">$15,000 — $30,000 USD</option>
                <option value="30k-75k">$30,000 — $75,000 USD</option>
                <option value="75k+">$75,000+ USD (Enterprise)</option>
              </select>
            </div>

            <div>
              <label class="block text-slate-400 mb-1">Descripción del Desafío</label>
              <textarea rows="3" placeholder="Necesitamos una plataforma de microservicios en Go capaz de soportar 50,000 usuarios concurrentes..." class="w-full bg-[#111722] border border-white/10 rounded-xl px-3.5 py-2 text-white placeholder-slate-500 focus:outline-none focus:border-brand-blue resize-none"></textarea>
            </div>

            <div class="pt-2">
              <button type="submit" id="submitConsultationBtn" class="btn-orbita-primary w-full py-3 text-xs font-semibold text-center">
                Enviar Solicitud de Arquitectura →
              </button>
            </div>
          </form>

          <div id="formSuccessMessage" class="hidden mt-4 p-3.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-mono">
            ✓ Solicitud recibida. Un arquitecto principal de LEXUR responderá en menos de 4 horas hábiles.
          </div>
        </div>

        <div class="pt-4 border-t border-white/5 text-[10px] font-mono text-slate-500">
          Acuerdo de Confidencialidad (NDA) disponible previo al inicio.
        </div>

      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- JAVASCRIPT LOGIC                                                          -->
  <!-- ========================================================================= -->
  <script>
    // 1. Interactive Tesla Cursor
    const dot = document.getElementById('teslaCursorDot');
    const ring = document.getElementById('teslaCursorRing');
    const spotlight = document.getElementById('ambientSpotlight');

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let ringX = mouseX;
    let ringY = mouseY;

    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;

      if (dot) {
        dot.style.left = `${mouseX}px`;
        dot.style.top = `${mouseY}px`;
      }

      if (spotlight) {
        spotlight.style.left = `${mouseX}px`;
        spotlight.style.top = `${mouseY}px`;
      }
    });

    function animateCursorRing() {
      ringX += (mouseX - ringX) * 0.18;
      ringY += (mouseY - ringY) * 0.18;

      if (ring) {
        ring.style.left = `${ringX}px`;
        ring.style.top = `${ringY}px`;
      }
      requestAnimationFrame(animateCursorRing);
    }
    requestAnimationFrame(animateCursorRing);

    // Hover interactive elements
    const interactiveElements = 'a, button, input, select, textarea, [role="button"], .liquid-glass-card';
    document.querySelectorAll(interactiveElements).forEach(el => {
      el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover-active'));
      el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover-active'));
    });

    // 2. Interactive Constellation Canvas Grid
    const canvas = document.getElementById('constellationCanvas');
    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const particleCount = 30;

    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.3,
        vy: (Math.random() - 0.5) * 0.3,
        size: Math.random() * 1.5 + 0.5
      });
    }

    function animateParticles() {
      ctx.clearRect(0, 0, width, height);

      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;
        if (p.y < 0) p.y = height;
        if (p.y > height) p.y = 0;

        ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();

        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (dist < 120) {
            ctx.strokeStyle = `rgba(37, 99, 235, ${0.1 * (1 - dist / 120)})`;
            ctx.lineWidth = 0.7;
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();
          }
        }
      }
      requestAnimationFrame(animateParticles);
    }
    requestAnimationFrame(animateParticles);

    // 3. Sector Switcher
    const sectorData = {
      fintech: {
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
      },
      health: {
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
      },
      logistics: {
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
      },
      retail: {
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
      },
      energy: {
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
      }
    };

    let activeSectorKey = 'fintech';

    function switchSector(key) {
      activeSectorKey = key;
      const data = sectorData[key];
      if (!data) return;

      ['fintech', 'health', 'logistics', 'retail', 'energy'].forEach(k => {
        const btn = document.getElementById(`sectorBtn_${k}`);
        if (k === key) {
          btn.className = "px-4 py-2 rounded-full font-mono text-xs font-semibold transition-all bg-brand-blue text-white shadow-md";
        } else {
          btn.className = "px-4 py-2 rounded-full font-mono text-xs font-semibold transition-all liquid-glass-pill text-slate-400 hover:text-white";
        }
      });

      const card = document.getElementById('sectorContentCard');
      gsap.to(card, {
        opacity: 0.4,
        duration: 0.15,
        onComplete: () => {
          document.getElementById('sectorTag').textContent = data.tag;
          document.getElementById('sectorHeading').textContent = data.title;
          document.getElementById('sectorDescription').textContent = data.desc;
          document.getElementById('sectorStat1').textContent = data.stat1;
          document.getElementById('sectorStat2').textContent = data.stat2;
          document.getElementById('sectorStat3').textContent = data.stat3;

          const listEl = document.getElementById('sectorBlueprintList');
          listEl.innerHTML = data.blueprints.map(bp => {
            const parts = bp.split(' · ');
            return `<div class="flex items-center gap-2 text-slate-300">
              <span class="text-blue-400">${parts[0]}</span>
              <span>${parts[1]}</span>
            </div>`;
          }).join('');

          gsap.to(card, { opacity: 1, duration: 0.25 });
        }
      });
    }

    function openProjectDrawerWithSector() {
      openProjectDrawer();
      const select = document.getElementById('formSectorInput');
      if (select) {
        if (activeSectorKey === 'fintech') select.value = "Fintech & Finanzas";
        if (activeSectorKey === 'health') select.value = "Healthtech & Salud";
        if (activeSectorKey === 'logistics') select.value = "Logística & Transporte";
        if (activeSectorKey === 'retail') select.value = "Retail & E-Commerce";
        if (activeSectorKey === 'energy') select.value = "Industria & IoT";
      }
    }

    // 4. Services Modal Popup (Liquid Glass GSAP)
    const servicesDirectory = {
      software: {
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
      },
      cloud: {
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
      },
      security: {
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
      },
      ai: {
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
      },
      fintech: {
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
      },
      uiux: {
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
      }
    };

    let activeServiceKey = 'software';

    function openServiceModal(key) {
      activeServiceKey = key;
      const data = servicesDirectory[key];
      if (!data) return;

      document.getElementById('modalCategory').textContent = data.category;
      document.getElementById('modalTitle').textContent = data.title;
      document.getElementById('modalDescription').textContent = data.desc;

      const stackContainer = document.getElementById('modalStackTags');
      stackContainer.innerHTML = data.stack.map(s => 
        `<span class="px-2.5 py-1 rounded-md bg-blue-500/10 text-blue-300 font-mono text-xs font-semibold border border-blue-500/20">${s}</span>`
      ).join('');

      const deliverablesContainer = document.getElementById('modalDeliverablesList');
      deliverablesContainer.innerHTML = data.deliverables.map(d => 
        `<li class="leading-relaxed">${d}</li>`
      ).join('');

      const modal = document.getElementById('serviceModal');
      const card = document.getElementById('serviceModalCard');

      modal.classList.remove('hidden');
      gsap.to(modal, { opacity: 1, duration: 0.2 });
      gsap.fromTo(card, 
        { scale: 0.95, opacity: 0, y: 15 }, 
        { scale: 1, opacity: 1, y: 0, duration: 0.3, ease: "power2.out" }
      );
    }

    function closeServiceModal() {
      const modal = document.getElementById('serviceModal');
      const card = document.getElementById('serviceModalCard');

      gsap.to(card, { scale: 0.95, opacity: 0, y: 10, duration: 0.2 });
      gsap.to(modal, {
        opacity: 0,
        duration: 0.2,
        onComplete: () => {
          modal.classList.add('hidden');
        }
      });
    }

    // 5. Drawer Handling
    function openProjectDrawer() {
      const drawer = document.getElementById('projectDrawer');
      const backdrop = document.getElementById('drawerBackdrop');
      const panel = document.getElementById('drawerPanel');

      drawer.classList.remove('hidden');
      gsap.to(backdrop, { opacity: 1, duration: 0.3 });
      gsap.to(panel, { x: '0%', duration: 0.3, ease: "power3.out" });
    }

    function closeProjectDrawer() {
      const drawer = document.getElementById('projectDrawer');
      const backdrop = document.getElementById('drawerBackdrop');
      const panel = document.getElementById('drawerPanel');

      gsap.to(panel, { x: '100%', duration: 0.25, ease: "power3.in" });
      gsap.to(backdrop, {
        opacity: 0,
        duration: 0.25,
        onComplete: () => {
          drawer.classList.add('hidden');
        }
      });
    }

    function handleFormSubmit(e) {
      e.preventDefault();
      const btn = document.getElementById('submitConsultationBtn');
      btn.innerHTML = `<span class="animate-pulse">Transmitiendo...</span>`;
      btn.disabled = true;

      setTimeout(() => {
        document.getElementById('consultationForm').reset();
        document.getElementById('formSuccessMessage').classList.remove('hidden');
        btn.innerHTML = `✓ Solicitud Registrada`;
        setTimeout(() => {
          closeProjectDrawer();
          btn.innerHTML = `Enviar Solicitud de Arquitectura →`;
          btn.disabled = false;
          document.getElementById('formSuccessMessage').classList.add('hidden');
        }, 2000);
      }, 800);
    }

    function toggleMobileMenu() {
      const menu = document.getElementById('mobileMenu');
      if (menu.classList.contains('hidden')) {
        menu.classList.remove('hidden');
        menu.classList.add('flex');
        gsap.fromTo(menu, { opacity: 0, y: -15 }, { opacity: 1, y: 0, duration: 0.2 });
      } else {
        gsap.to(menu, {
          opacity: 0,
          y: -15,
          duration: 0.15,
          onComplete: () => {
            menu.classList.add('hidden');
            menu.classList.remove('flex');
          }
        });
      }
    }

    function copyTerminalCode() {
      const code = `package main\n\nimport "github.com/lexur/core"\n\nfunc DeploySolution() *core.Mesh {\n  spec := core.NewArchitecture(&core.Config{\n    Sectors:    []string{"fintech", "health", "logistics"},\n    ZeroTrust:  true,\n    LatencyP99: "1.2ms",\n  })\n  return spec.Initialize()\n}`;
      navigator.clipboard.writeText(code).then(() => {
        const btn = document.getElementById('copyCodeBtn');
        const original = btn.innerHTML;
        btn.innerHTML = `<span class="text-emerald-400 font-bold text-xs">✓</span>`;
        setTimeout(() => btn.innerHTML = original, 1600);
      });
    }

    // 6. Bilingual i18n
    const i18nData = {
      es: {
        navHome: "Inicio",
        navWhy: "Por Qué LEXUR",
        navProcess: "Metodología",
        navServices: "Servicios",
        navSectors: "Rubros",
        navFacilities: "Sedes",
        navCta: "Iniciar Proyecto",
        heroBadge: "Ingeniería de Software Multirubro",
        heroTitleLine1: "Software de Calidad que",
        heroTitleLine2: "Transforma Industrias Globales",
        heroSubtitle: "LEXUR diseña y construye plataformas digitales de alto impacto, arquitecturas cloud y sistemas críticos para fintech, salud, logística, retail y energía.",
        heroCtaConsult: "Agendar Consulta",
        heroCtaStartText: "Iniciar Proyecto",
        heroProofText: "Arquitecturas en producción integradas con estándares globales",
        whyTag: "POR QUÉ LEXUR",
        whyTitle: "Ingeniería de Precisión. Cero Deuda Técnica.",
        whySubtitle: "Tres razones arquitectónicas por las que líderes globales eligen a LEXUR sobre el desarrollo convencional.",
        whyCard1Title: "Respuesta Inmediata. En Cada Transacción.",
        whyCard1Desc: "Sistemas reactivos en Go y Rust que procesan más de 100,000 req/s con latencias P99 sub-milisegundo. Cero cuellos de botella ni caídas imprevistas.",
        whyCard2Title: "Software que Entiende Tu Industria.",
        whyCard2Desc: "Arquitecturas nativas para cumplir normativas bancarias (PCI-DSS), salud (HIPAA) y sincronización logística en tiempo real offline-first.",
        whyCard3Title: "Escala Sin Romper tu Equipo.",
        whyCard3Desc: "Infraestructura Cloud-Native en Kubernetes que escala automáticamente de 1,000 a millones de usuarios concurrentes. Código modular y tipado estricto.",
        howTag: "CÓMO TRABAJAMOS",
        howTitle: "De la Visión a Producción en 4 Fases Claras",
        howSubtitle: "Desde el diagnóstico arquitectónico hasta la escala global — más rápido y predecible de lo que imaginas.",
        step1Title: "1 — Conectar & Blueprint de Arquitectura",
        step1Desc: "Mapeamos tus procesos y requerimientos específicos de tu rubro. Definimos el stack técnico, modelos de datos ACID y vectores de seguridad antes de escribir código.",
        step2Title: "2 — Desarrollo Modular & Sprints",
        step2Desc: "Ingeniería ágil en Go, React, Flutter o Rust. Entregas quincenales de software funcional con pipelines CI/CD automatizados y cobertura de pruebas >85%.",
        step3Title: "3 — Auditoría Zero-Trust & Pruebas de Carga",
        step3Desc: "Simulamos picos de tráfico masivo y estrés de infraestructura. Evaluamos vulnerabilidades con escáneres estáticos y aseguramos cumplimiento normativo.",
        step4Title: "4 — Despliegue Zero-Downtime & Telemetría",
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
      },
      en: {
        navHome: "Home",
        navWhy: "Why LEXUR",
        navProcess: "Methodology",
        navServices: "Services",
        navSectors: "Industries",
        navFacilities: "Hubs",
        navCta: "Start Project",
        heroBadge: "Multi-Industry Software Engineering",
        heroTitleLine1: "Quality Software that",
        heroTitleLine2: "Transforms Global Industries",
        heroSubtitle: "LEXUR architects and builds high-impact digital platforms, cloud infrastructure, and mission-critical systems for fintech, healthcare, logistics, retail, and energy.",
        heroCtaConsult: "Book Consultation",
        heroCtaStartText: "Start Project",
        heroProofText: "Production architectures integrated with global industry standards",
        whyTag: "WHY LEXUR",
        whyTitle: "Precision Engineering. Zero Technical Debt.",
        whySubtitle: "Three architectural reasons global leaders choose LEXUR over conventional software agencies.",
        whyCard1Title: "Instant Response. Every Time.",
        whyCard1Desc: "Reactive systems in Go and Rust processing 100,000+ req/s with sub-millisecond P99 latency budgets. Zero bottlenecks or unexpected downtime.",
        whyCard2Title: "Software Tailored to Your Industry.",
        whyCard2Desc: "Native architectures built to satisfy banking compliance (PCI-DSS), healthcare standards (HIPAA), and offline-first real-time supply chain sync.",
        whyCard3Title: "Scale Without Breaking Your Team.",
        whyCard3Desc: "Cloud-Native Kubernetes infrastructure that automatically scales from 1,000 to millions of concurrent users. Strict typing and modular code.",
        howTag: "HOW IT WORKS",
        howTitle: "From Vision to Production in 4 Clear Steps",
        howSubtitle: "From initial architecture diagnostics to global scaling — faster and more predictable than you think.",
        step1Title: "1 — Connect & Architecture Blueprint",
        step1Desc: "We map your industry requirements, ACID data models, and zero-trust security postures before writing a single line of code.",
        step2Title: "2 — Modular Engineering & Sprints",
        step2Desc: "Agile sprints in Go, React, Flutter, or Rust. Bi-weekly functional deployments with automated CI/CD pipelines and >85% unit test coverage.",
        step3Title: "3 — Zero-Trust Auditing & Stress Testing",
        step3Desc: "Massive traffic stress simulations, penetration testing, and automated security code scans prior to production sign-off.",
        step4Title: "4 — Zero-Downtime Deployment & Telemetry",
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
      }
    };

    let currentLang = 'es';

    function setLanguage(lang) {
      currentLang = lang;
      const dict = i18nData[lang];
      if (!dict) return;

      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
          el.textContent = dict[key];
        }
      });

      const btnEs = document.getElementById('langBtnEs');
      const btnEn = document.getElementById('langBtnEn');

      if (lang === 'es') {
        btnEs.className = "px-2 py-0.5 rounded-full transition-all bg-brand-blue text-white font-bold";
        btnEn.className = "px-2 py-0.5 rounded-full transition-all text-slate-400 hover:text-white font-bold";
      } else {
        btnEn.className = "px-2 py-0.5 rounded-full transition-all bg-brand-blue text-white font-bold";
        btnEs.className = "px-2 py-0.5 rounded-full transition-all text-slate-400 hover:text-white font-bold";
      }
    }

    // Hash deep linking
    window.addEventListener('load', () => {
      const hash = window.location.hash;
      if (hash.startsWith('#service-')) {
        const key = hash.replace('#service-', '');
        if (servicesDirectory[key]) openServiceModal(key);
      } else if (hash === '#consultoria') {
        openProjectDrawer();
      }
    });
  </script>
</body>
</html>'''

with open(r"f:\LEXUR CORP\landing-page\index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Generated index.html with true Orbita AI 1:1 fidelity and Lexur software focus!")
