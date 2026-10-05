// AUTO-GENERADO por lexur-design-system/scripts/generate-tokens.mjs (v1.0.0). NO EDITAR A MANO.
// ignore_for_file: public_member_api_docs
import 'package:flutter/widgets.dart';

@immutable
class LxColorTokens {
  const LxColorTokens({
    required this.bgCanvas,
    required this.bgSurface1,
    required this.bgSurface2,
    required this.bgSurface3,
    required this.bgInverse,
    required this.borderSubtle,
    required this.borderDefault,
    required this.borderStrong,
    required this.borderControl,
    required this.textPrimary,
    required this.textSecondary,
    required this.textTertiary,
    required this.textDisabled,
    required this.textInverse,
    required this.textOnAccent,
    required this.accentDefault,
    required this.accentHover,
    required this.accentPressed,
    required this.accentSubtle,
    required this.accentText,
    required this.statusSuccess,
    required this.statusSuccessSubtle,
    required this.statusWarning,
    required this.statusWarningSubtle,
    required this.statusDanger,
    required this.statusDangerSubtle,
    required this.focusRing,
    required this.overlayScrim,
  });

  final Color bgCanvas;
  final Color bgSurface1;
  final Color bgSurface2;
  final Color bgSurface3;
  final Color bgInverse;
  final Color borderSubtle;
  final Color borderDefault;
  final Color borderStrong;
  final Color borderControl;
  final Color textPrimary;
  final Color textSecondary;
  final Color textTertiary;
  final Color textDisabled;
  final Color textInverse;
  final Color textOnAccent;
  final Color accentDefault;
  final Color accentHover;
  final Color accentPressed;
  final Color accentSubtle;
  final Color accentText;
  final Color statusSuccess;
  final Color statusSuccessSubtle;
  final Color statusWarning;
  final Color statusWarningSubtle;
  final Color statusDanger;
  final Color statusDangerSubtle;
  final Color focusRing;
  final Color overlayScrim;

  static const LxColorTokens dark = LxColorTokens(
    bgCanvas: Color(0xFF000000),
    bgSurface1: Color(0xFF0A0A0A),
    bgSurface2: Color(0xFF141414),
    bgSurface3: Color(0xFF1F1F1F),
    bgInverse: Color(0xFFFAFAFA),
    borderSubtle: Color(0xFF1A1A1A),
    borderDefault: Color(0xFF2A2A2A),
    borderStrong: Color(0xFF404040),
    borderControl: Color(0xFF5E5E5E),
    textPrimary: Color(0xFFF5F5F5),
    textSecondary: Color(0xFFA3A3A3),
    textTertiary: Color(0xFF808080),
    textDisabled: Color(0xFF4D4D4D),
    textInverse: Color(0xFF0A0A0A),
    textOnAccent: Color(0xFFFFFFFF),
    accentDefault: Color(0xFF2E6BFF),
    accentHover: Color(0xFF4A80FF),
    accentPressed: Color(0xFF2457D6),
    accentSubtle: Color(0xFF0B1A3D),
    accentText: Color(0xFF6B9BFF),
    statusSuccess: Color(0xFF32D74B),
    statusSuccessSubtle: Color(0xFF0B2611),
    statusWarning: Color(0xFFFFD60A),
    statusWarningSubtle: Color(0xFF2B2402),
    statusDanger: Color(0xFFFF453A),
    statusDangerSubtle: Color(0xFF2E0E0C),
    focusRing: Color(0xFF2E6BFF),
    overlayScrim: Color(0xB8000000),
  );

  static const LxColorTokens light = LxColorTokens(
    bgCanvas: Color(0xFFFFFFFF),
    bgSurface1: Color(0xFFFAFAFA),
    bgSurface2: Color(0xFFF2F2F2),
    bgSurface3: Color(0xFFE8E8E8),
    bgInverse: Color(0xFF0A0A0A),
    borderSubtle: Color(0xFFEFEFEF),
    borderDefault: Color(0xFFE0E0E0),
    borderStrong: Color(0xFFC2C2C2),
    borderControl: Color(0xFF8F8F8F),
    textPrimary: Color(0xFF0A0A0A),
    textSecondary: Color(0xFF525252),
    textTertiary: Color(0xFF6E6E6E),
    textDisabled: Color(0xFFB3B3B3),
    textInverse: Color(0xFFFAFAFA),
    textOnAccent: Color(0xFFFFFFFF),
    accentDefault: Color(0xFF0A5CFF),
    accentHover: Color(0xFF0050E6),
    accentPressed: Color(0xFF0042BF),
    accentSubtle: Color(0xFFEAF0FF),
    accentText: Color(0xFF0A5CFF),
    statusSuccess: Color(0xFF1E7E34),
    statusSuccessSubtle: Color(0xFFE8F5EB),
    statusWarning: Color(0xFFA15C00),
    statusWarningSubtle: Color(0xFFFFF4E0),
    statusDanger: Color(0xFFD70015),
    statusDangerSubtle: Color(0xFFFFEBEC),
    focusRing: Color(0xFF0A5CFF),
    overlayScrim: Color(0x7A000000),
  );
}

abstract final class LxSpace {
  static const double s0 = 0;
  static const double s2 = 2;
  static const double s4 = 4;
  static const double s8 = 8;
  static const double s12 = 12;
  static const double s16 = 16;
  static const double s20 = 20;
  static const double s24 = 24;
  static const double s32 = 32;
  static const double s40 = 40;
  static const double s48 = 48;
  static const double s64 = 64;
  static const double s80 = 80;
  static const double s96 = 96;
  static const double s128 = 128;
}

abstract final class LxRadius {
  static const double none = 0;
  static const double xs = 4;
  static const double sm = 6;
  static const double md = 10;
  static const double lg = 14;
  static const double xl = 20;
  static const double full = 9999;
}

abstract final class LxControl {
  static const double sm = 32;
  static const double md = 40;
  static const double lg = 48;
  static const double touchMinIos = 44;
  static const double touchMinAndroid = 48;
}

abstract final class LxLayout {
  static const double sidebar = 248;
  static const double sidebarCollapsed = 64;
  static const double header = 56;
  static const double contentMax = 1200;
  static const double readingMax = 680;
  static const double gutterMobile = 16;
  static const double gutterDesktop = 32;
}

abstract final class LxBreakpoint {
  static const double sm = 640;
  static const double md = 768;
  static const double lg = 1024;
  static const double xl = 1280;
  static const double xxl = 1536;
}

abstract final class LxType {
  static const String fontSans = 'Geist';
  static const String fontMono = 'Geist Mono';
  static const TextStyle displayXl = TextStyle(fontFamily: fontSans, fontSize: 72, height: 1.056, letterSpacing: -2.88, fontWeight: FontWeight.w600);
  static const TextStyle display = TextStyle(fontFamily: fontSans, fontSize: 56, height: 1.071, letterSpacing: -1.68, fontWeight: FontWeight.w600);
  static const TextStyle h1 = TextStyle(fontFamily: fontSans, fontSize: 40, height: 1.1, letterSpacing: -1, fontWeight: FontWeight.w600);
  static const TextStyle h2 = TextStyle(fontFamily: fontSans, fontSize: 32, height: 1.188, letterSpacing: -0.64, fontWeight: FontWeight.w600);
  static const TextStyle h3 = TextStyle(fontFamily: fontSans, fontSize: 24, height: 1.25, letterSpacing: -0.36, fontWeight: FontWeight.w600);
  static const TextStyle h4 = TextStyle(fontFamily: fontSans, fontSize: 20, height: 1.3, letterSpacing: -0.2, fontWeight: FontWeight.w600);
  static const TextStyle bodyLg = TextStyle(fontFamily: fontSans, fontSize: 17, height: 1.529, letterSpacing: 0, fontWeight: FontWeight.w400);
  static const TextStyle body = TextStyle(fontFamily: fontSans, fontSize: 15, height: 1.467, letterSpacing: 0, fontWeight: FontWeight.w400);
  static const TextStyle bodySm = TextStyle(fontFamily: fontSans, fontSize: 13, height: 1.385, letterSpacing: 0, fontWeight: FontWeight.w400);
  static const TextStyle label = TextStyle(fontFamily: fontSans, fontSize: 14, height: 1.429, letterSpacing: 0, fontWeight: FontWeight.w500);
  static const TextStyle caption = TextStyle(fontFamily: fontSans, fontSize: 12, height: 1.333, letterSpacing: 0.12, fontWeight: FontWeight.w500);
  static const TextStyle overline = TextStyle(fontFamily: fontSans, fontSize: 11, height: 1.273, letterSpacing: 0.88, fontWeight: FontWeight.w600);
  static const TextStyle metric = TextStyle(fontFamily: fontSans, fontSize: 48, height: 1.083, letterSpacing: -0.96, fontWeight: FontWeight.w500);
}

abstract final class LxDuration {
  static const Duration instant = Duration(milliseconds: 80);
  static const Duration fast = Duration(milliseconds: 150);
  static const Duration base = Duration(milliseconds: 220);
  static const Duration slow = Duration(milliseconds: 320);
  static const Duration deliberate = Duration(milliseconds: 480);
}

abstract final class LxEasing {
  static const Cubic standard = Cubic(0.2, 0, 0, 1);
  static const Cubic enter = Cubic(0.05, 0.7, 0.1, 1);
  static const Cubic exit = Cubic(0.3, 0, 0.8, 0.15);
}
