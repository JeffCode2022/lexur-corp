// src/app/layout.tsx — raiz LEXUR: dark-first, fuentes self-hosted, tema sin parpadeo.
import type { Metadata, Viewport } from 'next';
import { GeistSans } from 'geist/font/sans';
import { GeistMono } from 'geist/font/mono';
import { ThemeProvider } from 'next-themes';
import './globals.css';

export const metadata: Metadata = {
  title: { default: 'Producto LEXUR', template: '%s · LEXUR' },
  description: 'Describe el producto en una frase.',
};

// Valores = bg.canvas de cada tema (tokens.json).
export const viewport: Viewport = {
  themeColor: [
    { media: '(prefers-color-scheme: dark)', color: '#000000' }, // lexur-allow: viewport themeColor requires literal string
    { media: '(prefers-color-scheme: light)', color: '#FFFFFF' }, // lexur-allow: viewport themeColor requires literal string
  ],
  colorScheme: 'dark light',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html
      lang="es"
      data-theme="dark"
      suppressHydrationWarning
      className={`${GeistSans.variable} ${GeistMono.variable}`}
    >
      <body className="bg-canvas text-fg font-sans text-body antialiased">
        <ThemeProvider attribute="data-theme" defaultTheme="dark" themes={['dark', 'light']} enableSystem disableTransitionOnChange>
          <a href="#main" className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[600] focus:rounded-md focus:bg-inverse focus:px-4 focus:py-2 focus:text-fg-inverse">
            Saltar al contenido
          </a>
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
// Si usas CSP con nonce (lexur-frontend-security), pasa el nonce a <ThemeProvider nonce={nonce}>.
